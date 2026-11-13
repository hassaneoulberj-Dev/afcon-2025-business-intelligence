"""Offline checks of supplied CSVs and MySQL dump values; Python standard library only.

This is not a MySQL engine/import test. The small SQL parser supports the literal
INSERT ... VALUES syntax of this project, not arbitrary SQL scripts.
"""
from pathlib import Path
import csv
import hashlib
import json
import re
import sqlite3

ROOT = Path(__file__).resolve().parents[1]


def rows_from_values(values):
    token = re.compile(r"\s*(NULL|'(?:\\.|[^'\\])*'|-?\d+(?:\.\d+)?|[(),;])",re.I)
    pos=0; row=None; rows=[]
    while pos<len(values):
        if not values[pos:].strip(): break
        m=token.match(values,pos)
        if not m: raise ValueError(f'Unsupported SQL token at offset {pos}')
        pos=m.end(); t=m.group(1)
        if t=='(': row=[]
        elif t==')': rows.append(row); row=None
        elif t in {',',';'}: continue
        elif t.upper()=='NULL': row.append(None)
        elif t.startswith("'"):
            row.append(re.sub(r'\\(.)',lambda m:{'n':'\n','r':'\r','t':'\t','0':'\0'}.get(m[1],m[1]),t[1:-1]))
        else: row.append(float(t) if '.' in t else int(t))
    return rows


def audit():
    report={'csv':{},'tables':{},'foreign_keys':[]}
    for p in sorted((ROOT/'data/raw').glob('*.csv')):
        with p.open(encoding='utf-8-sig',newline='') as stream:
            reader=csv.DictReader(stream); rows=list(reader); columns=reader.fieldnames
        report['csv'][p.name]={'rows':len(rows),'columns':len(columns),
            'blank_names':sum(not r.get('full_name','x').strip() for r in rows),
            'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
    csv_files=report['csv']
    report['teams_duplicates_matches']=(csv_files['teams-2025-to-2025-stats.csv']['sha256']==csv_files['matches-2025-to-2025-stats.csv']['sha256'])
    db=sqlite3.connect(':memory:'); foreign=[]
    for p in sorted((ROOT/'database/tables').glob('*.sql')):
        text=p.read_text(encoding='utf-8')
        table=re.search(r'CREATE TABLE `([^`]+)`',text)[1]
        ddl=re.search(r'CREATE TABLE.*?ENGINE=',text,re.S)[0]
        cols=re.findall(r'^\s+`([^`]+)`\s+(\w+)',ddl,re.M)
        db.execute('CREATE TABLE '+table+' ('+','.join('"'+c+'" '+('TEXT' if t.lower() in {'varchar','date','text'} else 'NUMERIC') for c,t in cols)+')')
        rows=[]
        for values in re.findall(r'^INSERT INTO `[^`]+` VALUES (.*);$',text,re.M):
            rows.extend(rows_from_values(values))
        assert all(len(row)==len(cols) for row in rows),table
        db.executemany('INSERT INTO '+table+' VALUES ('+','.join('?' for _ in cols)+')',rows)
        pk=re.search(r'PRIMARY KEY \(`([^`]+)`\)',ddl)[1]
        duplicates=db.execute(f'SELECT COUNT(*)-COUNT(DISTINCT "{pk}") FROM {table}').fetchone()[0]
        report['tables'][table]={'rows':len(rows),'columns':len(cols),'duplicate_primary_keys':duplicates}
        for col,target,key in re.findall(r'FOREIGN KEY \(`([^`]+)`\) REFERENCES `([^`]+)` \(`([^`]+)`\)',ddl): foreign.append((table,col,target,key))
    for table,col,target,key in foreign:
        missing=db.execute(f'SELECT COUNT(*) FROM {table} s LEFT JOIN {target} t ON s."{col}"=t."{key}" WHERE s."{col}" IS NOT NULL AND t."{key}" IS NULL').fetchone()[0]
        nulls=db.execute(f'SELECT COUNT(*) FROM {table} WHERE "{col}" IS NULL').fetchone()[0]
        report['foreign_keys'].append(dict(table=table,column=col,target=target,orphans=missing,nulls=nulls))
    checks={
        'match_goals':'SELECT SUM(total_goals) FROM fact_matches',
        'match_goal_mismatches':'SELECT COUNT(*) FROM fact_matches WHERE total_goals != home_goals + away_goals',
        'match_negative_attendance':'SELECT COUNT(*) FROM fact_matches WHERE attendance < 0',
        'player_age_outside_15_45':'SELECT COUNT(*) FROM dim_player WHERE age < 15 OR age > 45',
        'player_dates_distinct':'SELECT COUNT(DISTINCT date_id) FROM fact_player_stats',
        'player_team_disagreements':'SELECT COUNT(*) FROM fact_player_stats f JOIN dim_player p ON f.player_id=p.player_id WHERE f.team_id != p.team_id',
        'date_min':'SELECT MIN(full_date) FROM dim_date',
        'date_max':'SELECT MAX(full_date) FROM dim_date',
        'player_replacement_characters':"SELECT COUNT(*) FROM dim_player WHERE player_name LIKE '%�%'",
    }
    report['checks']={k:db.execute(sql).fetchone()[0] for k,sql in checks.items()}
    db.close()
    return report


if __name__=='__main__':
    output=ROOT/'docs/data-quality.json'
    result=audit()
    output.write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2,ensure_ascii=True))

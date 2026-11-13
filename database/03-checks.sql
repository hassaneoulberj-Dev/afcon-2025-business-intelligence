USE afcon_2025_demo;

SELECT 'dim_date' AS table_name, COUNT(*) AS row_count FROM dim_date
UNION ALL SELECT 'dim_team', COUNT(*) FROM dim_team
UNION ALL SELECT 'dim_stadium', COUNT(*) FROM dim_stadium
UNION ALL SELECT 'dim_player', COUNT(*) FROM dim_player
UNION ALL SELECT 'fact_matches', COUNT(*) FROM fact_matches
UNION ALL SELECT 'fact_player_stats', COUNT(*) FROM fact_player_stats
UNION ALL SELECT 'fact_league_stats', COUNT(*) FROM fact_league_stats;

SELECT SUM(total_goals) AS total_goals,
       SUM(total_goals <> home_goals + away_goals) AS inconsistent_scores,
       SUM(stadium_id IS NULL) AS missing_stadiums
FROM fact_matches;

SELECT COUNT(DISTINCT date_id) AS distinct_dates,
       SUM(team_id IS NULL) AS missing_teams
FROM fact_player_stats;

SELECT player_id, player_name, age
FROM dim_player WHERE age < 15 OR age > 45;

-- Inspect a potential correspondence; this query does NOT modify data.
SELECT f.player_id, p.player_name, f.team_id AS fact_team_id, p.team_id AS dimension_team_id
FROM fact_player_stats f JOIN dim_player p ON p.player_id = f.player_id
WHERE f.team_id IS NULL OR f.team_id <> p.team_id;

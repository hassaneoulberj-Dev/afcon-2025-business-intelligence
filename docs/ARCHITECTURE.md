# Architecture observée

```mermaid
flowchart LR
    CSV[CSV fournis] --> ETL[Talend décrit dans le rapport]
    ETL --> DW[MySQL : africa_cup_dw]
    DW --> PBI[Power BI : 7 pages]
    SQL[Dumps SQL fournis] --> DEMO[MySQL : afcon_2025_demo]
```

Les sources des jobs ETL ne sont pas incluses. Le diagramme décrit le projet documenté et le chemin de restauration ajouté, pas une exécution ETL nouvellement vérifiée.

```mermaid
erDiagram
    dim_team ||--o{ dim_player : team_id
    dim_date ||--o{ fact_matches : date_id
    dim_team ||--o{ fact_matches : home_team_id
    dim_team ||--o{ fact_matches : away_team_id
    dim_stadium |o--o{ fact_matches : stadium_id
    dim_player ||--o{ fact_player_stats : player_id
    dim_team |o--o{ fact_player_stats : team_id
    dim_date ||--o{ fact_player_stats : date_id
```

`fact_league_stats` est une table d’agrégats sans clé étrangère déclarée. Les deux relations de `fact_matches` vers `dim_team` représentent les rôles domicile et extérieur ; leur configuration dans Power BI doit être vérifiée pour éviter des filtres ambigus.

## Grain des tables

| Table | Grain observé | Lignes |
| --- | --- | ---: |
| dim_date | Une date de compétition | 19 |
| dim_team | Une équipe nationale | 24 |
| dim_stadium | Un stade | 8 |
| dim_player | Un joueur | 555 |
| fact_matches | Un match | 52 |
| fact_player_stats | Une ligne agrégée par joueur, tous rattachés à la même date | 555 |
| fact_league_stats | Une compétition/saison | 1 |

La présence d’une `date_id` dans `fact_player_stats` ne suffit pas à transformer ces agrégats en statistiques par match. Aucun identifiant de match n’est présent dans cette table.

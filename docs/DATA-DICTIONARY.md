# Dictionnaire des colonnes

Extrait des définitions MySQL fournies. Les types et contraintes ne sont pas corrigés.

## dim_date

| Colonne | Définition MySQL |
| --- | --- |
| `date_id` | `int NOT NULL` |
| `full_date` | `date NOT NULL` |
| `day` | `int DEFAULT NULL` |
| `month` | `int DEFAULT NULL` |
| `year` | `int DEFAULT NULL` |
| `day_of_week` | `varchar(20) DEFAULT NULL` |
| `day_name` | `varchar(20) DEFAULT NULL` |
| `month_name` | `varchar(20) DEFAULT NULL` |
| `quarter` | `int DEFAULT NULL` |
| `week_of_year` | `int DEFAULT NULL` |
| `is_weekend` | `tinyint(1) DEFAULT NULL` |
| `tournament_phase` | `varchar(50) DEFAULT NULL` |
| `season` | `varchar(20) DEFAULT NULL` |

## dim_player

| Colonne | Définition MySQL |
| --- | --- |
| `player_id` | `int NOT NULL AUTO_INCREMENT` |
| `player_name` | `varchar(150) DEFAULT NULL` |
| `position` | `varchar(50) DEFAULT NULL` |
| `age` | `int DEFAULT NULL` |
| `nationality` | `varchar(100) DEFAULT NULL` |
| `current_club` | `varchar(100) DEFAULT NULL` |
| `team_id` | `int DEFAULT NULL` |

## dim_stadium

| Colonne | Définition MySQL |
| --- | --- |
| `stadium_id` | `int NOT NULL AUTO_INCREMENT` |
| `stadium_name` | `varchar(255) DEFAULT NULL` |
| `city` | `varchar(255) DEFAULT NULL` |
| `capacity` | `int DEFAULT NULL` |
| `latitude` | `decimal(10,6) DEFAULT NULL` |
| `longitude` | `decimal(10,6) DEFAULT NULL` |

## dim_team

| Colonne | Définition MySQL |
| --- | --- |
| `team_id` | `int NOT NULL AUTO_INCREMENT` |
| `team_name` | `varchar(100) NOT NULL` |
| `group_name` | `varchar(10) DEFAULT NULL` |
| `confederation` | `varchar(50) DEFAULT NULL` |
| `fifa_ranking` | `int DEFAULT NULL` |
| `team_code` | `varchar(10) DEFAULT NULL` |

## fact_league_stats

| Colonne | Définition MySQL |
| --- | --- |
| `id` | `int NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(100) DEFAULT NULL` |
| `season` | `int DEFAULT NULL` |
| `status` | `varchar(50) DEFAULT NULL` |
| `format` | `varchar(50) DEFAULT NULL` |
| `number_of_clubs` | `int DEFAULT NULL` |
| `total_matches` | `int DEFAULT NULL` |
| `matches_completed` | `int DEFAULT NULL` |
| `game_week` | `int DEFAULT NULL` |
| `total_game_week` | `int DEFAULT NULL` |
| `progress` | `int DEFAULT NULL` |
| `average_goals_per_match` | `decimal(5,2) DEFAULT NULL` |
| `average_scored_home_team` | `decimal(5,2) DEFAULT NULL` |
| `average_scored_away_team` | `decimal(5,2) DEFAULT NULL` |
| `btts_percentage` | `float DEFAULT NULL` |
| `clean_sheets_percentage` | `float DEFAULT NULL` |
| `prediction_risk` | `float DEFAULT NULL` |
| `home_scored_advantage_percentage` | `float DEFAULT NULL` |
| `home_defence_advantage_percentage` | `float DEFAULT NULL` |
| `home_advantage_percentage` | `float DEFAULT NULL` |
| `average_corners_per_match` | `decimal(5,2) DEFAULT NULL` |
| `average_corners_per_match_home_team` | `decimal(5,2) DEFAULT NULL` |
| `average_corners_per_match_away_team` | `decimal(5,2) DEFAULT NULL` |
| `total_corners_for_season` | `int DEFAULT NULL` |
| `average_cards_per_match` | `decimal(5,2) DEFAULT NULL` |
| `average_cards_per_match_home_team` | `decimal(5,2) DEFAULT NULL` |
| `average_cards_per_match_away_team` | `decimal(5,2) DEFAULT NULL` |
| `total_cards_for_season` | `int DEFAULT NULL` |
| `over_05_percentage` | `float DEFAULT NULL` |
| `over_15_percentage` | `float DEFAULT NULL` |
| `over_25_percentage` | `float DEFAULT NULL` |
| `over_35_percentage` | `float DEFAULT NULL` |
| `over_45_percentage` | `float DEFAULT NULL` |
| `over_55_percentage` | `float DEFAULT NULL` |
| `under_05_percentage` | `float DEFAULT NULL` |
| `under_15_percentage` | `float DEFAULT NULL` |
| `under_25_percentage` | `float DEFAULT NULL` |
| `under_35_percentage` | `float DEFAULT NULL` |
| `under_45_percentage` | `float DEFAULT NULL` |
| `under_55_percentage` | `float DEFAULT NULL` |
| `over_65_corners_percentage` | `float DEFAULT NULL` |
| `over_75_corners_percentage` | `float DEFAULT NULL` |
| `over_85_corners_percentage` | `float DEFAULT NULL` |
| `over_95_corners_percentage` | `float DEFAULT NULL` |
| `over_105_corners_percentage` | `float DEFAULT NULL` |
| `over_115_corners_percentage` | `float DEFAULT NULL` |
| `over_125_corners_percentage` | `float DEFAULT NULL` |
| `over_135_corners_percentage` | `float DEFAULT NULL` |
| `over_05_cards_percentage` | `float DEFAULT NULL` |
| `over_15_cards_percentage` | `float DEFAULT NULL` |
| `over_25_cards_percentage` | `float DEFAULT NULL` |
| `over_35_cards_percentage` | `float DEFAULT NULL` |
| `over_45_cards_percentage` | `float DEFAULT NULL` |
| `over_55_cards_percentage` | `float DEFAULT NULL` |
| `over_65_cards_percentage` | `float DEFAULT NULL` |
| `over_75_cards_percentage` | `float DEFAULT NULL` |
| `goals_min_0_to_10` | `int DEFAULT NULL` |
| `goals_min_11_to_20` | `int DEFAULT NULL` |
| `goals_min_21_to_30` | `int DEFAULT NULL` |
| `goals_min_31_to_40` | `int DEFAULT NULL` |
| `goals_min_41_to_50` | `int DEFAULT NULL` |
| `goals_min_51_to_60` | `int DEFAULT NULL` |
| `goals_min_61_to_70` | `int DEFAULT NULL` |
| `goals_min_71_to_80` | `int DEFAULT NULL` |
| `goals_min_81_to_90` | `int DEFAULT NULL` |
| `goals_min_0_to_15` | `int DEFAULT NULL` |
| `goals_min_16_to_30` | `int DEFAULT NULL` |
| `goals_min_31_to_45` | `int DEFAULT NULL` |
| `goals_min_46_to_60` | `int DEFAULT NULL` |
| `goals_min_61_to_75` | `int DEFAULT NULL` |
| `goals_min_76_to_90` | `int DEFAULT NULL` |
| `xg_avg_per_match` | `decimal(5,2) DEFAULT NULL` |

## fact_matches

| Colonne | Définition MySQL |
| --- | --- |
| `match_id` | `int NOT NULL AUTO_INCREMENT` |
| `date_id` | `int DEFAULT NULL` |
| `home_team_id` | `int DEFAULT NULL` |
| `away_team_id` | `int DEFAULT NULL` |
| `stadium_id` | `int DEFAULT NULL` |
| `tournament_phase` | `varchar(50) DEFAULT NULL` |
| `game_week` | `int DEFAULT NULL` |
| `home_goals` | `int DEFAULT NULL` |
| `away_goals` | `int DEFAULT NULL` |
| `total_goals` | `int DEFAULT NULL` |
| `home_corners` | `int DEFAULT NULL` |
| `away_corners` | `int DEFAULT NULL` |
| `total_corners` | `int DEFAULT NULL` |
| `home_yellow_cards` | `int DEFAULT NULL` |
| `away_yellow_cards` | `int DEFAULT NULL` |
| `home_red_cards` | `int DEFAULT NULL` |
| `away_red_cards` | `int DEFAULT NULL` |
| `home_possession` | `decimal(5,2) DEFAULT NULL` |
| `away_possession` | `decimal(5,2) DEFAULT NULL` |
| `home_shots` | `int DEFAULT NULL` |
| `away_shots` | `int DEFAULT NULL` |
| `home_shots_on_target` | `int DEFAULT NULL` |
| `away_shots_on_target` | `int DEFAULT NULL` |
| `xg_home` | `decimal(5,2) DEFAULT NULL` |
| `xg_away` | `decimal(5,2) DEFAULT NULL` |
| `attendance` | `int DEFAULT NULL` |

## fact_player_stats

| Colonne | Définition MySQL |
| --- | --- |
| `stat_id` | `int NOT NULL AUTO_INCREMENT` |
| `player_id` | `int DEFAULT NULL` |
| `team_id` | `int DEFAULT NULL` |
| `date_id` | `int DEFAULT NULL` |
| `position_played` | `varchar(50) DEFAULT NULL` |
| `minutes_played` | `int DEFAULT NULL` |
| `goals` | `int DEFAULT NULL` |
| `assists` | `int DEFAULT NULL` |
| `shots` | `int DEFAULT NULL` |
| `shots_on_target` | `int DEFAULT NULL` |
| `yellow_cards` | `int DEFAULT NULL` |
| `red_cards` | `int DEFAULT NULL` |
| `passes_completed` | `int DEFAULT NULL` |
| `pass_accuracy` | `decimal(5,2) DEFAULT NULL` |
| `rating` | `decimal(4,2) DEFAULT NULL` |

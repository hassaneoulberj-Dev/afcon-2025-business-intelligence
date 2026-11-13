# Audit des fichiers — 13 novembre 2026

## Contrôles exécutés

- Inventaire de 14 fichiers originaux ; copie d’archive vérifiée par empreintes SHA-256.
- Lecture complète des quatre CSV avec l’analyseur CSV de Python.
- Lecture des sept schémas et des valeurs INSERT des dumps ; contrôles en mémoire via SQLite, sans connexion à une base utilisateur.
- Vérification des clés primaires, huit relations étrangères et cohérence des buts.
- Inspection du manifeste et du layout PBIX : 7 pages et respectivement 9, 9, 13, 8, 9, 13, 12 conteneurs visuels.
- Lecture du rapport de 36 pages et du texte des 20 diapositives du PowerPoint.
- Extraction des captures intégrées aux pages 21–27 du rapport ; inspection visuelle de l’accueil et de la page de comparaison.

## Anomalies et précautions d’interprétation

1. Le CSV `teams-2025-to-2025-stats.csv` est identique octet pour octet au CSV des matchs. Il ne permet pas de reconstruire les statistiques d’équipes annoncées dans le rapport.
2. Le CSV des joueurs contient 556 lignes et une ligne sans nom. Les exports SQL en contiennent 555. Le lien causal précis entre cette ligne et son exclusion ne peut pas être confirmé sans les jobs ETL.
3. `fact_matches.stadium_id` est NULL dans 9 lignes ; une jointure interne sur les stades exclurait ces matchs.
4. `fact_player_stats.team_id` est NULL dans 73 lignes, alors que `dim_player.team_id` est renseigné pour tous les joueurs. Aucune correction n’a été appliquée : les règles de correspondance originales restent à confirmer.
5. 16 joueurs ont un âge hors de la plage de contrôle 15–45 ans. Il s’agit d’un signal de qualité, pas d’une preuve suffisante pour inventer un âge corrigé.
6. Une seule date distincte apparaît dans `fact_player_stats`. Les mesures semblent cumulées par joueur ; elles ne constituent pas un historique par match.
7. Aucune clé primaire dupliquée, référence non nulle orpheline ou incohérence `total_goals != home_goals + away_goals` n’a été détectée. Cela ne supprime pas les défauts métier précédents.
8. Le rapport décrit un modèle et un ETL plus complets que les seules sources disponibles. Les jobs Talend et les formules DAX complètes ne sont pas livrés en fichiers texte.

## Contrôles non effectués

L’import dans un moteur MySQL réel, l’ouverture du PBIX dans Power BI Desktop et son actualisation ne sont pas validés. Le modèle binaire compressé du PBIX n’a pas été décodé : l’absence de secrets n’est pas certifiée pour ce contenu. Aucun mot de passe évident n’a été détecté dans le texte du rapport ou le layout Power BI inspecté.

Les fichiers originaux et leur modèle ont été préservés. Cette livraison est une organisation documentée du projet, pas une correction complète de ses données ni une reconstruction des jobs ETL.

Résultats détaillés et reproductibles : [data-quality.json](data-quality.json).

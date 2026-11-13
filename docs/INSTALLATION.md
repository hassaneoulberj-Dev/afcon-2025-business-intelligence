# Utiliser les livrables

## Prérequis

- Windows et Power BI Desktop pour consulter le PBIX.
- MySQL 8.0 pour restaurer l’entrepôt ; les dumps indiquent une source MySQL 8 et utilisent `utf8mb4_0900_ai_ci`.
- MySQL Workbench ou un client MySQL pour exécuter les scripts.
- Python 3.10+ uniquement pour le contrôle hors ligne facultatif.

## Restauration de l’entrepôt

Exécuter, dans l’ordre, `database/01-schema.sql`, `database/02-data.sql`, puis `database/03-checks.sql` avec Workbench. Arrêter en cas d’erreur, notamment si `afcon_2025_demo` existe déjà. Ne pas lancer les dumps originaux sur une base contenant des tables à préserver.

L’ordre de création et de chargement est : `dim_date`, `dim_team`, `dim_stadium`, `dim_player`, `fact_matches`, `fact_player_stats`, `fact_league_stats`. Les contraintes de clés étrangères restent actives. Le script de données utilise une transaction et ne doit pas être réexécuté sur les mêmes tables remplies.

Le script de schéma n’est pas idempotent : il vise une base neuve. Il n’inclut pas de suppression ni de désactivation des contraintes.

## Power BI

Ouvrir `powerbi/afcon-2025.pbix` dans Power BI Desktop, puis examiner les paramètres des sources de données et les requêtes Power Query avant toute actualisation. La base originale s’appelle `africa_cup_dw` ; la démonstration restaurée s’appelle `afcon_2025_demo`.

Adapter le serveur, le nom de base et les identifiants à votre environnement. Ne pas enregistrer de mot de passe dans un fichier publié sur GitHub. Vérifier les dépendances des visuels personnalisés si un visuel ne se charge pas.

Le paquet PBIX contient un modèle embarqué et des références à des artefacts Power BI distants. L’inspection de son archive ne permet pas de certifier qu’une actualisation sera possible sans reconfiguration. Son ouverture et son actualisation n’ont pas été testées dans Power BI Desktop pendant cette organisation.

## Talend

Les captures et explications des jobs figurent dans le rapport PDF. Aucun export de projet Talend, fichier `.item` ou `.properties` de job n’est fourni. Demander les sources originales aux auteurs pour rejouer l’ETL ; les scripts SQL restaurent seulement l’état final disponible.

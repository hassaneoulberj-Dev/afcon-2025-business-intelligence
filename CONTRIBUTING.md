# Contribuer — AFCON BI

Ce guide aide à proposer des corrections reproductibles pour ce projet académique.

## Signaler un problème

Décrire le comportement observé, le résultat attendu et les étapes pour reproduire le problème. Indiquer les versions des outils utilisés et joindre un exemple minimal lorsque cela est possible.

## Vérifications adaptées au projet

- Indiquer la table, la colonne et la requête concernées lorsque vous signalez une incohérence de données.
- Expliquer la provenance de chaque nouveau CSV et conserver les données sources pour pouvoir comparer les corrections.
- Exécuter `python scripts/validate_data.py` après une modification des données et joindre les écarts observés dans `docs/data-quality.json`.
- Tester toute modification du PBIX dans Power BI Desktop : navigation, filtres, relations et actualisation. Préciser les vérifications réellement effectuées.
- Un export de projet Talend doit inclure ses sources et une procédure de lancement ; une capture seule ne rend pas un job reproductible.

## Proposer une modification

Créer une branche dédiée, limiter chaque commit à un changement cohérent et décrire sa motivation. Dans la demande de fusion, préciser les vérifications réalisées, leur résultat et les limites restantes. Actualiser la documentation lorsque le comportement ou les prérequis changent.

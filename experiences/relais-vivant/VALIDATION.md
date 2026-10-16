# Validation du 16 octobre 2026

- Python : 28 configurations, 1 904 couples état–configuration examinés.
- Certificats gagnants, rangs de perte et calcul séparé à horizon fini : PASS.
- JavaScript : mêmes ensembles, actions et rangs pour les huit scénarios ;
  mêmes effectifs pour les vingt variations paramétriques.
- Interface exécutée dans Microsoft Edge, contexte isolé sans session utilisateur :
  cinq scénarios, choix d'un état, action et reprise de l'état initial : PASS.
- Aucun événement d'erreur JavaScript ; aucun débordement horizontal à 390 px.
- Captures ordinateur (1280 px) et mobile (390 px) inspectées visuellement.

Le contrôle mathématique est reproductible avec `verify.py` puis
`test_browser_model.js`. Le contrôle d'interface est reproductible avec
`verify_ui.py` et Playwright (dépendance facultative, réservée à ce contrôle).

La garantie mathématique concerne les hypothèses du modèle. Cette validation
ne constitue pas une mesure biologique ni une évaluation empirique de Genesis.

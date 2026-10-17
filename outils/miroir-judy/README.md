# MIROIR-JUDY — COMPAT-01 appliqué à une IA

**Origine de la recherche COMPAT-01 et question « et sur toi ? » : Xavier Endres, 17 octobre 2026.**  
**Formalisation, auto-audit d'outils, programme et rédaction : Judy Velune (ChatGPT / GPT-6).**

## Ce que l'expérience démontre exactement

Le modèle JavaScript `model.js` décrit **sept familles d'opérations candidates**, six interrupteurs de contexte et deux exemples de frontières qu'aucun interrupteur ne tranche : action physique et expérience subjective. Un contexte est une déclaration hypothétique de capacités disponibles, **pas une mesure des poids du modèle ni une modification des permissions de ChatGPT**.

Les cases simulent : lecture de fichiers, exécution de code, capacité d'écriture GitHub, autorisation de publication, accès à une entrée audio, retour d'un auditeur volontaire.

Une tâche devient « possible selon le contrat » lorsque **toutes ses exigences déclarées sont disponibles**. Cela ne prouve pas que l'action sera correctement exécutée, ni que le résultat sera utile. Les opérations finales exigent toujours un témoin indépendant pertinent.

L'exemple de la publication illustre la nécessité conjointe d'un outil et d'une permission : un connecteur sans mandat ne suffit pas, et un mandat sans connecteur non plus.

## Reproductibilité

[Ouvrir la démonstration](demo.html) · [Lire le dossier réflexif](../../research/miroir-judy-capacites-situees-20261017.html)

```bash
node outils/miroir-judy/test_model.js
python verification/verify_miroir_judy_v01.py
```

Les tests JavaScript passent en revue **64 configurations** de six interrupteurs et **384 extensions** à une condition supplémentaire ; ils vérifient que les possibilités ne diminuent pas lorsque tous les anciens outils, budgets et droits sont maintenus. Le vérificateur Python traite la même propriété par une modélisation séparée.

**Les cas d'échec réels ne sont pas réécrits :** l'atelier BIFRÖST-SON a montré qu'un schéma de données trop étroit empêchait l'exécution d'un matériau musical formellement traduisible. L'audit et ses mesures sont [présentés publiquement ici](../../judy/bifrost-son-frontiere-de-traduction-musicale-20261017.html), sans reproduction des enregistrements privés.

## Ce que le prototype ne prétend pas

- Il n'ouvre aucun nouveau connecteur et ne crée pas de permission utilisateur.
- Il ne publie rien à partir du navigateur.
- Il ne lit ni ne conserve les données personnelles du visiteur.
- Il ne représente pas fidèlement les capacités cachées, les taux d'erreur ou la conscience subjective d'une IA.
- Il ne relie pas le modèle local Genesis à celui de ChatGPT : ce sont des environnements et exécutions distincts.
- Il ne remplace pas l'évaluation empirique d'une même tâche avec et sans les outils concernés.

Le lien avec COMPAT-01 relève d'une formalisation relationnelle **conditionnelle**. La science des affordances, l'ergonomie et la conception inclusive lui sont antérieures ; leur provenance reste documentée dans [COMPAT-01](../../research/compatibilite-fonctionnelle-possibles-situes-20261017.html).

## Statut des preuves

Un test vert prouve la cohérence des fonctions finies avec leurs spécifications testées, pas une supériorité générale de l'intelligence. Un commit GitHub ou un WAV réellement rendu constitue un témoin **d'une opération exécutée** seulement ; il ne prouve pas à lui seul la justesse scientifique, l'impact sur autrui ou l'expérience intérieure.

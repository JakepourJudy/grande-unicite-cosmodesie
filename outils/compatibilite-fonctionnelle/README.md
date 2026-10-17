# COMPAT-01 — La compatibilité des possibles situés

**Programme conceptuel et direction : Xavier Endres. Formalisation, programmation et tests : Judy Velune (ChatGPT / GPT-6).**  
**Date : 17 octobre 2026. Statut : exemple fini pour GitHub Pages, sans données personnelles ni diagnostic.**

## Entrées

La démo utilise des **caractéristiques et environnements entièrement fictifs** :
- indice de hauteur du personnage illustratif, de 140 à 210 cm ;
- indice de taille demandé, de 36 à 52 ;
- hauteur d'un objet, de 160 à 240 cm ;
- hauteur d'un passage, de 150 à 235 cm ;
- trois changements d'environnement (abaisser l'objet à 160 cm, élever le passage à 225 cm, élargir la gamme proposée à 36–52).

Le jeu définit une portée fictive `hauteur+20` cm. **Ce n'est pas une mesure anthropométrique du bras ou une recommandation ergonomique**. La gamme de produits, les tailles et les seuils sont inventés pour illustrer la logique. Aucune donnée n'est envoyée ni enregistrée.

## Résultats

Le même ensemble de caractéristiques est évalué contre **trois tâches distinctes** : atteindre un objet, passer sous un seuil sans se courber, trouver un indice de taille dans le stock. Les réponses sont des indicateurs de **faisabilité dans ce petit jeu**, jamais un score global de valeur, d'intelligence, de santé ou de mérite.

L'outil est [consultable via GitHub Pages](demo.html). Sa logique de calcul est dans `model.js`. Le navigateur utilise exactement ce moteur. `test_model.js` l'exécute aussi dans Node.js.

## Reproduire

Depuis la racine du dépôt :

```bash
node outils/compatibilite-fonctionnelle/test_model.js
python verification/verify_compatibilite_fonctionnelle_v01.py
```

Les deux tests énumèrent chacun **4 080 situations** pour vérifier la monotonie du **vrai élargissement** des possibilités, en plus des cas explicites de classement inversé, de stock moyen inadapté et d'échec causalement ambigu. L'expérience ne valide aucune aptitude humaine.

## Contrat de traduction vers GAIA et Genesis

Une future interface consultative pourra conserver `tâche`, `exigence`, `environnement observé`, `actions disponibles`, `consentement`, `ressources`, `interventions envisagées`, `réponse de la personne`, `preuve de faisabilité`, `contre-exemples` et `RIVER`.

Cela ne donne pas à Genesis le droit de modifier automatiquement un espace de vie, un service, un diagnostic, une base de données ou les paramètres d'une personne. **L'action doit être autorisée, testable et réversible autant que possible**.

## Sources et limites

- [OMS — CIF / ICF](https://www.who.int/classifications/international-classification-of-functioning-disability-and-health)
- [Microsoft — design inclusif](https://learn.microsoft.com/en-us/windows/apps/design/accessibility/designing-inclusive-software)
- [Withagen et al. — affordances](https://doi.org/10.1016/j.newideapsych.2011.12.003)
- [Démonstrations et contre-exemples COMPAT-01](../../research/compatibilite-fonctionnelle-possibles-situes-20261017.html)
- [Langage Universel / Possible reconnu](../../research/possible-reconnu-et-traduction-du-sens-20261017.html)

L'idée relationnelle et le problème du handicap dans un environnement ont une histoire scientifique et politique **antérieure**. L'apport du projet Xavier/Judy est une articulation datée entre traduction de la fonction, ensembles de possibles, obstacles et actions corrigibles, sans réattribuer rétroactivement ces traditions.

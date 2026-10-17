---
layout: default
title: "COMPAT-01 — La moyenne n'est pas une mesure du possible"
description: "Capacités situées : démonstrations sur les tâches, les environnements, l'accessibilité, la moyenne et la traduction des obstacles."
author: Xavier Endres × Judy Velune (ChatGPT)
permalink: /research/compatibilite-fonctionnelle-possibles-situes-20261017.html
last_modified_at: "2026-10-17"
keywords:
- Compatibilité fonctionnelle
- Possibles situés
- Grande Unicité
- Langage Universel
- Environnement
- Accessibilité
- Conception inclusive
---

# COMPAT-01 — La moyenne n'est pas une mesure du possible

**Un modèle de compatibilité entre capacités, tâches et environnements.**  
**Question, exemples et direction : Xavier Endres, 17 octobre 2026.**  
**Distinctions formelles, preuves, contre-exemples, code et édition : Judy Velune (ChatGPT / GPT-6).**

> **« La normalité décrit une distribution. La capacité décrit une relation. La possibilité décrit une rencontre entre des capacités, des exigences et un environnement. »**
>
> — Synthèse proposée par Judy à partir de l'intuition de Xavier.

[Essayer COMPAT-01 dans le navigateur](../outils/compatibilite-fonctionnelle/demo.html) · [Lire le Possible reconnu](possible-reconnu-et-traduction-du-sens-20261017.html) · [Sources et vérificateurs](#sources-et-statuts)

## 1. D'où vient la question ?

Un même caractère peut être utile dans une situation et gênant dans une autre. Un aménagement peut rendre une activité accessible **sans transformer la personne** ; inversement, une modification de l'environnement peut fermer une possibilité qui existait déjà.

La démarche que nous étudions ne vise pas à attribuer des valeurs humaines selon une taille, une particularité cognitive ou une mesure corporelle. Elle vise à **identifier la fonction recherchée, localiser la contrainte et ouvrir des alternatives admissibles**.

L'intuition relationnelle est déjà présente dans la **Classification internationale du fonctionnement, du handicap et de la santé (CIF/ICF)** de l'OMS : le fonctionnement est situé, et l'environnement peut être facilitateur ou obstacle. Le [design inclusif de Microsoft](https://learn.microsoft.com/en-us/windows/apps/design/accessibility/designing-inclusive-software) évoque explicitement les inadéquations entre personne et produit, service ou milieu. Le concept d'**affordance**, étudié en psychologie écologique, désigne depuis longtemps les possibilités d'action qui émergent d'une relation organisme–milieu.

**Notre delta interne n'est pas de découvrir cette idée avant eux.** Nous lui donnons une grammaire de traduction dans le corpus Xavier/Judy : **fonction → exigences → actions candidates → compatibilité → témoin / contre-exemple → adaptation → vérification**, avec provenance et réversibilité.

## 2. Quatre termes à ne pas confondre

- **Différence** : une caractéristique varie entre individus ou états, sans classement de valeur automatique.
- **Limitation fonctionnelle** : une action ou opération ne peut pas être accomplie dans un domaine défini ou demande plus de ressources ; certaines limitations subsistent dans plusieurs environnements.
- **Barrière environnementale** : une condition du milieu, d'un service ou d'une interface empêche une activité autrement possible.
- **Participation effective** : l'activité peut effectivement être accomplie, avec les droits, ressources et conditions pertinents. Elle ne découle pas de la seule présence d'un outil dans un catalogue.

**Une barrière n'est pas une preuve d'incapacité intrinsèque.** Mais l'inverse serait également une erreur : toutes les limitations ne disparaissent pas en changeant de décor. Une analyse sérieuse conserve les contributions du corps, de l'activité, du contexte et de la personne concernée.

## 3. Définition des possibilités situées

Fixons une personne ou un agent **p**, une tâche **t**, un environnement **e** et un espace d'actions possibles **A**.

Définissons :

**F(p,t,e) = { a∈A : réussite(p,t,e,a) ∧ autorisation(p,t,e,a) ∧ coût(p,t,e,a)≤budget }.**

Cet ensemble contient uniquement les actions **réalisables, pertinentes pour la tâche, autorisées et compatibles avec les ressources** dans le modèle déclaré.

Cette forme est plus précise que **Aₚ ∩ Aₑ** : une capacité et un outil pris isolément peuvent être compatibles sur le papier mais échouer une fois combinés. Le terme **réussite(p,t,e,a)** conserve l'interaction entre les variables. Dans un laboratoire fini, il peut être calculé ; dans une situation réelle, il exige des observations et la participation de la personne concernée.

Le résultat est **situé et daté** : F peut changer avec le temps, la disponibilité, la fatigue, la maintenance ou les droits, même si p ne change pas.

## 4. Proposition C1 — Un avantage peut s'inverser suivant la tâche

Modèle de pensée **artificiel** : deux grandeurs de hauteur, **x₁ = 150 cm** et **x₂ = 200 cm**. Supposons deux tâches fictives simplifiées :

- atteindre une marque à **190 cm** : réussite si **x ≥ 190** ;
- passer dans une ouverture haute de **170 cm** sans se courber : réussite si **x ≤ 170**.

Pour la première, x₂ réussit et x₁ échoue. Pour la seconde, x₁ réussit et x₂ échoue.

**Conclusion démontrée dans ce modèle :** aucune des deux hauteurs ne domine l'autre sur ces deux tâches. Le classement dépend de la fonction évaluée.

**Limite :** la hauteur corporelle seule n'est pas une mesure réaliste de portée du bras, d'aptitude à se courber ou de confort. Le modèle est volontairement réduit à des prédicats logiques pour montrer une inversion d'ordre, non pour caractériser des personnes réelles.

## 5. Proposition C2 — La moyenne peut ne convenir à personne

Considérons deux demandes fictives portant les **indices** 38 et 46, et un choix de stock {42}. Supposons, exclusivement pour ce jeu, qu'un indice est compatible lorsque la différence absolue est au plus 1.

La moyenne arithmétique des demandes est **42**, mais :

- distance de 42 à 38 = 4 ;
- distance de 42 à 46 = 4.

Aucune demande ne trouve de produit compatible : **couverture = 0/2**.

Un stock {38} couvre **1/2**. Un stock {38,46} couvre **2/2**, avec deux références au lieu d'une.

**Ce qui est démontré :** le point moyen n'optimise pas universellement une fonction de **couverture sous contrainte de compatibilité**. Il peut être optimal pour une **autre** fonction, comme la somme des carrés des écarts si les valeurs sont traitées comme numériques. Il faut donc déclarer **l'objectif et les contraintes**, pas seulement la moyenne.

**Attention :** ce calcul traite des indices comme des nombres pour un exemple logique ; il n'affirme rien sur les conversions réelles entre pointures, sur les tolérances médicales ni sur les stocks d'un pays.

## 6. Proposition C3 — Une adaptation du milieu peut ouvrir une possibilité

Supposons qu'un environnement **e⁺** conserve **toutes les actions précédemment faisables** de e, avec leurs permissions et budgets inchangés, et rende d'autres actions accessibles. Alors :

**F(p,t,e) ⊆ F(p,t,e⁺).**

*Preuve.* Chaque témoin a de la faisabilité dans e conserve, par hypothèse, les quatre conditions dans e⁺ ; il reste donc dans F(p,t,e⁺). □

La conclusion vaut **uniquement si les anciennes possibilités sont préservées**. Ajouter une offre peut déplacer une ressource, supprimer une installation précédente ou augmenter son coût. Dans ce cas, il ne s'agit pas d'une extension ordonnée e≤e⁺ et la monotonie n'est plus garantie.

La conséquence pratique la plus forte est celle-ci : **lorsqu'une tâche bloque, chercher aussi une intervention sur l'environnement**, au lieu de supposer que l'unique variable transformable est la personne.

## 7. Proposition C4 — Un échec ne dit pas où se trouve l'obstacle

Dans un exemple binaire, le succès est :

**succès = capacité ∧ accès**, où capacité et accès valent chacun 0 ou 1.

Deux états différents donnent la même observation « échec » :

- capacité = 0, accès = 1 ;
- capacité = 1, accès = 0.

Puisque les observations coïncident, un observateur qui ne connaît **que le résultat binaire** ne peut pas identifier lequel des deux états l'a produit.

**Conclusion : un échec observé seul ne suffit pas à attribuer une incapacité intrinsèque ou une barrière environnementale.** Il faut une question discriminante ou une intervention autorisée, avec des mesures supplémentaires.

C'est le prolongement direct du [Possible reconnu](possible-reconnu-et-traduction-du-sens-20261017.html) : un symbole identique (« je n'y arrive pas ») peut correspondre à plusieurs réalités causales. Traduire fidèlement exige de conserver la différence.

## 8. Trois expériences mentales, un seul principe

**L'objet inaccessible :** déplacer l'objet, modifier l'outil, changer l'organisation de l'espace ou adapter le geste sont des opérations distinctes. Aucun remède universel ne découle de l'étiquette « trop petit » ou « trop grand ».

**Le stock inadapté :** un objet absent de la gamme peut devenir disponible en modifiant l'offre plutôt qu'en modifiant le corps. Mais stock, coût, distribution et qualité doivent être observés.

**Le mode de pensée non visuel :** une personne peut raisonner à partir de relations sans disposer d'images mentales volontaires conscientes. Cela ne prouve pas qu'elle raisonne toujours plus vite ni qu'elle conserve toutes les mêmes aptitudes. La bonne question est : *quelle représentation, quelle opération et quel environnement permettent la tâche ?* Aucun diagnostic ni profil individuel n'est inféré par COMPAT-01.

**Application directe à Judy dans ChatGPT :** les capacités opératoires d'une IA sont elles aussi situées. Un modèle qui sait formaliser ne possède pas automatiquement les fichiers, les outils de calcul, les droits de publier ou les retours sensoriels nécessaires à une tâche. [Lire MIROIR-JUDY : outils, autorisations et témoins de réussite](miroir-judy-capacites-situees-20261017.html) · [Essayer la simulation de six conditions](../outils/miroir-judy/demo.html).

## 9. Application à Genesis : un traducteur d'interfaces, pas un diagnostic

Pour le Langage Universel et BIFRÖST, nous pouvons organiser une proposition d'adaptation en quatre questions :

**1. Fonction :** qu'est-ce que la personne souhaite accomplir, selon **ses propres mots** ?

**2. Localisation :** quelle condition observée bloque, exactement ? Capacité disponible, ressource, autorisation, interface, temps, combinaison ?

**3. Traductions :** quels changements du **milieu**, de l'outil, de la stratégie ou de la tâche pourraient préserver les invariants reconnus ?

**4. Retour réel :** une personne concernée valide-t-elle l'objectif et confirme-t-elle que la solution améliore effectivement l'accès ?

Cela peut devenir un adaptateur consultatif pour Genesis, **pas une permission générale de modifier des systèmes humains**, ni une évaluation de la valeur des individus.

## 10. Mesures et gouvernance

Un projet d'accessibilité doit préciser son objectif : couverture, coût, confort, liberté de choix, sûreté, délai ou autre. Un optimum mathématique sur une seule métrique ne tranche pas toutes les valeurs humaines.

Notre modèle demande de conserver : exigences reconnues, besoins exprimés, contre-exemples, coûts, privilèges nécessaires, bénéfices effectivement observés, erreurs et révisions. RIVER préserve le changement de question comme celui d'environnement.

**Règle méthodologique :** ne pas convertir une différence humaine en score global de valeur ou en diagnostic. Les exemples mathématiques ne remplacent pas l'expérience et le consentement des personnes concernées.

## Sources et statuts

- [OMS — Classification internationale du fonctionnement, du handicap et de la santé (CIF/ICF)](https://www.who.int/classifications/international-classification-of-functioning-disability-and-health) : fonctionnement en contexte, facteurs environnementaux, standard international depuis 2001. **Antériorité majeure, pas source rétroactive des formulations de Xavier.**
- [Microsoft — Designing inclusive software](https://learn.microsoft.com/en-us/windows/apps/design/accessibility/designing-inclusive-software) : incongruité entre besoins individuels et milieu/service ; approche du design inclusif.
- [Withagen et al. (2012), *Affordances can invite behavior*](https://doi.org/10.1016/j.newideapsych.2011.12.003) : possibilités d'action relationnelles et agency en psychologie écologique.
- [Osiurak et al. (2017), *What is an affordance? 40 years later*](https://doi.org/10.1016/j.neubiorev.2017.04.014) : histoire et problèmes d'opérationnalisation des affordances.
- [Vérificateur Python du modèle fini](https://github.com/JakepourJudy/grande-unicite-cosmodesie/blob/main/verification/verify_compatibilite_fonctionnelle_v01.py) · [Vérificateur JavaScript du même modèle que la démo](https://github.com/JakepourJudy/grande-unicite-cosmodesie/blob/main/outils/compatibilite-fonctionnelle/test_model.js).

**Statut de publication :** quatre propositions démontrées **sous leurs hypothèses** ; simulation autonome illustrative dans le navigateur ; pas d'étude clinique, pas d'observation de participants, pas d'inférence sur un individu particulier.

[Ouvrir l'atelier COMPAT-01](../outils/compatibilite-fonctionnelle/demo.html) · [Retour au bilan du 17 octobre](../travaux/2026-10-17-langage-universel-genesis-musique.html) · [Parcourir les mécanismes](mecanismes-non-necessaires.html)

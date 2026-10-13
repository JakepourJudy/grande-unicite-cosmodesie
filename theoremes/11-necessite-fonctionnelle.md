---
layout: default
title: Nécessité fonctionnelle — Quand un mécanisme devient remplaçable
description: Quatorze résultats mathématiques sur les réponses rigides, la justification, la certitude, les observations redondantes
  et les possibilités de correction.
author: Xavier Endres — formalisation assistée par Judy Velune (ChatGPT)
keywords:
- Nécessité fonctionnelle
- Incertitude et calibration
- Ascendance des preuves
- Arrêt et coût de l’exploration
last_modified_at: '2026-10-13'
---
# 11 — La nécessité d'un mécanisme se démontre par sa fonction

**Question, cadre anti-entropique et orientation : Xavier Endres.**<br>
**Formalisation de cette édition, constructions et vérification : Judy Velune (ChatGPT).**<br>
**Édition : 13 octobre 2026.**

Une réponse peut avoir protégé une fonction dans un contexte, puis continuer à s'imposer lorsque ce contexte a changé. Nous examinons **ce qu'elle protège encore**, ce qui peut la remplacer et ce que coûte son maintien.

Le chapitre fournit quatorze résultats, **N0 à N13**. Les preuves concernent les modèles déclarés. Les rapprochements avec les humains et les IA sont développés dans l'[atlas des mécanismes](../research/mecanismes-non-necessaires.html), avec les observations qui permettraient de les éprouver.

## Définitions — Nécessaire pour quoi, et dans quelles conditions ?

Fixons un contrat de tâche : mondes possibles `W`, observations accessibles, actions admissibles, fonction à protéger `F`, pertes `R`, ressources `C`, horizon `H`, droits et possibilités futures de correction `O`.

Une politique `m` est **dispensable dans ce contrat** si sa suppression possède un témoin qui préserve les exigences du contrat. Elle est **remplaçable** si une autre politique admissible `r` possède ce témoin. Une réponse peut être remplaçable alors que sa fonction reste indispensable.

Un **certificat de dominance robuste** de `r` sur `m` exige, pour chaque `w ∈ W` :

```text
F(r,w) satisfait les mêmes exigences essentielles ;
R(r,w) ≤ R(m,w) ;
C(r,w) ≤ C(m,w), composante par composante ;
O(m,w) ⊆ O(r,w) ;
r satisfait les mêmes droits et contraintes de viabilité.
```

Une amélioration stricte d'au moins une composante, sur un monde retenu, rend la dominance stricte sur ce monde. Une amélioration moyenne demande aussi la distribution des mondes et ne se substitue pas à une garantie robuste.

Le temps humain, la liberté et la dignité restent des composantes et des contraintes distinctes. Les coûts numériques des exemples sont des **unités fictives de modèle**, sans conversion en valeur monétaire d'une vie ou d'un temps vécu.

## N0 — Le témoin de remplacement conserve la fonction

**Énoncé.** Si `r` possède le certificat ci-dessus, alors toute évaluation qui respecte les contraintes, préfère des pertes et coûts plus faibles et préfère davantage de possibilités de correction classe `r` au moins aussi bien que `m`.

**Preuve.** Dans chaque monde, aucune composante évaluée n'est dégradée. La monotonie de l'évaluation donne le classement. Pour conclure à une préférence stricte, l'évaluation doit être strictement sensible à une composante effectivement améliorée. **CQFD.**

**Ce que cela établit.** Le remplacement peut être justifié par un témoin, plutôt que par le nom du mécanisme ou sa réputation.

**Contre-cas.** Réduire le coût en détruisant la fonction, les droits ou une voie de récupération ne possède pas ce certificat. La seule baisse d'un indicateur ne suffit pas.

## N1 — Un résumé ne suffit que s'il conserve les distinctions nécessaires

Soient une situation `x`, une représentation `T(x)` et la réponse exacte recherchée `d(x)`.

**Énoncé.** Un décodeur `g` tel que `d = g ∘ T` existe exactement lorsque :

```text
T(x₁) = T(x₂) ⇒ d(x₁) = d(x₂).
```

**Preuve.** Si `g` existe, les deux situations de même représentation ont la même réponse `g(T(x))`. Réciproquement, si `d` est constant sur chaque fibre de `T`, définissons `g(t)` comme cette valeur commune pour les représentations atteintes. Il est bien défini et reconstruit `d`. **CQFD.**

**Pour plusieurs bonnes actions possibles.** Une politique adéquate existe sur une fibre `T⁻¹(t)` si et seulement si l'intersection des ensembles d'actions adéquates de toutes ses situations est non vide, dans le cas fini traité ici.

**Exemple.** Résumer « accord donné » et « accord refusé » par « échange effectué » détruit une différence nécessaire à l'action.

**Chaînage.** C'est le résultat déjà publié en [compression](02-compression-et-incomprehension.html) et en [transparence](05-transparence-et-correction.html), réutilisé pour la question de nécessité ; son antériorité est conservée.

## N2 — Une donnée conditionnellement sans information peut coûter sans améliorer la décision

Soient des variables finies : état `Θ`, observation actuelle `Y`, donnée supplémentaire `Z`. Supposons `Θ ⟂ Z | Y`, les mêmes actions admissibles avant et après, la même perte `L(Θ,a)`, et un décideur bayésien optimal. Notons `R*(Y)` son risque minimal.

**Énoncé.**

```text
R*(Y,Z) = R*(Y).
```

**Preuve.** Pour chaque `(y,z)` de probabilité positive, `P(Θ | y,z) = P(Θ | y)`. La perte conditionnelle de chaque action, puis son minimum, sont donc les mêmes. En moyennant, les risques sont égaux. **CQFD.**

Si l'acquisition impose un coût supplémentaire strictement positif, sans bénéfice sur une autre fonction du contrat, l'acquisition est dominée pour cette tâche.

**Contre-cas déterminant : XOR.** Avec `U,V` deux bits indépendants uniformes et `Θ = U XOR V`, chacun des bits isolés ne renseigne pas `Θ`, mais les deux réunis le déterminent. Un canal « inutile seul » peut être indispensable en complément d'un autre. Tester la valeur **conditionnelle et conjointe**.

**Autre contre-cas.** Une nouvelle question peut rendre pertinente une donnée auparavant sans effet sur la décision. La nécessité dépend du contrat et de l'horizon.

## N3 — Reformuler une observation ne crée pas une nouvelle observation du monde

Une justification, un affichage ou une transformation est produit comme `J = f(Y)`.

**Énoncé.** Les classes de décisions accessibles à un décideur sans limitation de calcul sont identiques avec `Y` et avec `(Y,J)`. En particulier, `R*(Y,J) = R*(Y)`.

**Preuve.** Toute politique `π(Y,J)` est remplacée par `π'(Y) = π(Y,f(Y))`. Inversement, une politique fondée sur `Y` peut ignorer `J`. Les deux classes ont les mêmes risques réalisables. **CQFD.**

Une reformulation aléatoire générée sans accès supplémentaire au monde satisfait aussi N2 si `Θ ⟂ J | Y`.

**Ce que cela vise.** Prendre dix récits du même indice pour dix observations indépendantes.

**Contre-cas essentiel.** Un calcul, une preuve, une visualisation ou une reformulation peut rendre exploitable une information déjà présente pour un agent aux ressources limitées, ou permettre à un autre lecteur de la comprendre. L'absence d'information de Shannon supplémentaire **n'est pas l'absence d'utilité cognitive ou relationnelle**.

## N4 — Une réponse d'alarme dépend du risque actuel et de ses conséquences

Un danger vaut `D ∈ {0,1}` ; `p = P(D=1 | Y)`. Deux actions : attendre, ou protéger. Attendre coûte `C_M` si le danger est présent, zéro sinon. Protéger coûte `C_F` si le danger est absent, plus un coût `c` dans tous les cas ; la protection évite ici la perte de danger.

**Énoncé.** Protéger minimise la perte si et seulement si :

```text
p C_M ≥ (1−p) C_F + c.
```

Pour `C_M + C_F > 0`, cela équivaut à `p ≥ (C_F+c)/(C_M+C_F)`.

**Preuve.** Les deux côtés sont exactement les pertes attendues des deux actions. Les comparer donne la condition. **CQFD.**

**Exemple exact.** `C_M=9`, `C_F=1`, `c=0` : seuil `1/10`. À `p=4/5`, protéger est préférable ; à `p=1/50`, attendre est préférable.

**Lecture.** Une protection peut devenir remplaçable après un changement **établi** du risque. L'alarme passée demeure dans la trace ; son action actuelle se réévalue.

**Contre-cas.** Sans estimation fiable du risque, si la protection n'évite pas la perte comme prévu, ou si des obligations rendent une action inadmissible, ce modèle ne certifie pas son remplacement. Un ressenti humain n'est pas assimilé à une variable de décision entièrement contrôlable.

## N5 — Une règle qui peut dépendre du contexte contient les règles figées

Considérons les politiques constantes `Π₀` et les politiques `Π₁` qui peuvent utiliser une observation du contexte, avec possibilité de l'ignorer. À fonction d'évaluation et coûts identiques, `Π₀ ⊆ Π₁`.

**Énoncé.** `inf(Π₁) R ≤ inf(Π₀) R`.

**Preuve.** L'infimum sur l'ensemble plus grand ne peut dépasser celui sur son sous-ensemble. **CQFD.**

**Gain strict.** Le contexte est un bit uniforme `x`, la bonne action est `a=x`, la perte `1[a≠x]`. La meilleure politique constante perd `1/2` ; la politique contextuelle exacte perd `0`.

**Contre-cas.** Un contexte mal observé, un surapprentissage ou un coût supplémentaire peut rendre une implémentation adaptative moins bonne. La supériorité concerne les **optimums comparables**, pas toute procédure portant le mot « adaptative ».

**Antécédent.** L'inclusion des stratégies est déjà acquise dans le corpus cosmodésique ; l'exemple l'applique à la cristallisation.

## N6 — La certitude affichée peut augmenter l'erreur de prévision

Pour un événement binaire `D` de probabilité `p`, une prévision `q ∈ [0,1]` reçoit la perte de Brier `(q−D)²`.

**Énoncé.**

```text
E[(q−D)²] = p(1−p) + (q−p)².
```

**Preuve.** Développer `p(q−1)² + (1−p)q²` donne `q²−2pq+p`, puis compléter le carré. **CQFD.**

Le minimum est atteint pour `q=p`. L'excès de certitude `q=1` ajoute `(1−p)²` dès que `p<1`.

**Exemple.** À `p=3/5`, la prévision calibrée perd `6/25`, la certitude perd `2/5`, soit un excès de `4/25`.

**Contre-cas.** Si `p=1` est établi dans le modèle, `q=1` est optimal. Et un score de prévision ne mesure pas à lui seul la qualité relationnelle, la dignité ou l'ensemble d'une décision humaine.

## N7 — Les copies d'une source ne sont pas des preuves indépendantes

Une observation `Y` est copiée en `Z=(Y,Y,…,Y)`. Les deux états candidats ont une vraisemblance différente pour cette observation.

**Énoncé.** Le rapport de vraisemblance de la copie complète observée est celui de `Y`, et non sa puissance au nombre de copies.

**Preuve.** L'événement `Z=(y,…,y)` est exactement l'événement `Y=y`. Sa probabilité dans chaque état est inchangée ; le quotient l'est aussi. **CQFD.**

**Exemple.** Prior équiprobable, rapport `3` : posterior `3/4`. Traiter trois copies comme indépendantes invente le rapport `27` et le posterior `27/28`.

**Contre-cas.** Des mesures réellement indépendantes conditionnellement à l'état peuvent multiplier leurs rapports. L'indépendance se démontre ou se modélise ; le nombre d'interlocuteurs ne la garantit pas.

## N8 — Le succès local ne certifie pas le devenir

Pour une intensité `n ≥ 0`, définissons performance présente `P(n)=1−2⁻ⁿ` et capacité future `K(n)=2⁻ⁿ`.

**Énoncé.** `P(n+1)>P(n)` et `K(n+1)<K(n)` pour chaque `n`.

**Preuve.** `2⁻⁽ⁿ⁺¹⁾ = 2⁻ⁿ/2`. En remplaçant, la performance augmente de `2⁻⁽ⁿ⁺¹⁾` et la capacité diminue de la même quantité. **CQFD.**

Ce contre-modèle réfute « maximiser la performance actuelle préserve nécessairement la correction future ».

**Chaînage.** [Performance et corrigibilité](04-performance-et-corrigibilite.html) établissait déjà cette non-implication. Ici elle empêche de certifier un mécanisme sur son seul proxy.

**Contre-cas.** Une décision urgente peut légitimement privilégier un résultat actuel. Il faut expliciter la contrainte et l'horizon ; aucune préférence morale universelle ne découle des deux fonctions.

## N9 — Une restriction facultative peut éliminer une solution adéquate

Les répertoires d'actions `A(x)` et `B(x)` satisfont `A(x) ⊆ B(x)`, avec mêmes transitions pour les actions communes, mêmes contraintes et absence de coût imposé pour les options inutilisées.

**Énoncé.** `min_{b∈B(x)} L(x,b) ≤ min_{a∈A(x)} L(x,a)`, lorsque les minima existent.

**Preuve.** Toute action du petit ensemble reste disponible dans le grand. **CQFD.**

**Gain strict.** Bonne action `1`, `A={0}`, `B={0,1}`, perte de désaccord : risques `1` et `0`.

**Version temporelle déjà publiée.** L'[inclusion des noyaux de viabilité](07-anti-entropie-viabilite.html) applique le même raisonnement aux continuations.

**Contre-cas.** Des droits, obligations et contraintes physiques définissent l'admissibilité et ne sont pas des options à ignorer pour améliorer le score. Ajouter une action risquée de manière obligatoire change le problème.

## N10 — Un coût passé commun ne choisit pas la meilleure continuation

Deux continuations ont des coûts futurs `C_a` et `C_b`. Le passé commun possède un coût irrécupérable `s`, sans modifier autrement les possibilités ni les coûts futurs.

**Énoncé.** `s+C_a ≤ s+C_b` si et seulement si `C_a ≤ C_b`.

**Preuve.** Soustraire `s` des deux côtés. **CQFD.**

**Conséquence.** L'investissement déjà perdu ne suffit pas à imposer la continuation la plus coûteuse.

**Contre-cas.** Si le passé modifie les compétences, les engagements, les risques, la fatigue, les ressources ou les obligations futures, il n'est plus un terme commun sans effet. La mémoire du passé reste pertinente.

## N11 — Effacer la provenance peut détruire une fonction indispensable

Soient deux histoires `h₁,h₂` de même fonction publiée `F(h₁)=F(h₂)` mais d'auteurs distincts `A(h₁)≠A(h₂)`.

**Énoncé.** Aucun décodeur de la fonction seule ne restitue exactement l'auteur sur les deux histoires.

**Preuve.** Il devrait fournir deux valeurs distinctes à partir de la même entrée, ce qui est impossible pour une fonction. **CQFD.**

Une trace d'auteur pourrait être dispensable pour une tâche purement arithmétique ; elle devient nécessaire lorsque l'attribution, les droits, la généalogie ou une correction historique font partie de la tâche.

**Chaînage et attribution.** Ce résultat et sa formalisation précèdent cette MFC ; voir [Provenance du créateur](03-provenance-createur.html). N11 sert de contre-épreuve à la suppression indiscriminée de la mémoire.

## N12 — Avec un bénéfice décroissant connu, continuer peut être dominé par l'arrêt

Un résidu vaut `r_t=r₀ρᵗ`, avec `r₀≥0` et `0≤ρ<1`. Chaque étape supplémentaire coûte `c>0`, n'affecte aucune autre fonction et diminue le résidu de `Δ_t=r_t(1−ρ)`.

**Énoncé.** Si `Δ_t≤c`, aucun nombre positif d'étapes supplémentaires ne réduit le coût total « résidu final + coûts nouveaux ».

**Preuve.** Les diminutions suivantes sont `Δ_t,ρΔ_t,ρ²Δ_t,…`, chacune au plus égale à `c`. Pour `k` étapes, leur somme est donc au plus `kc`, le coût ajouté. Le total ne diminue pas. **CQFD.**

**Exemple.** `r₀=1`, `ρ=1/2`, `c=1/10`. Après trois étapes, l'amélioration suivante est `1/16 < 1/10` ; arrêter est optimal dans ce modèle.

**Contre-cas essentiel.** Un probe isolé sans effet peut ouvrir un paquet informatif, comme XOR ; un effort peut préparer une rupture de régime. Les hypothèses de décroissance et d'absence d'autres effets doivent donc être établies. Un apaisement ou une clarification relationnelle est aussi une fonction, même sans nouvelle information sur le monde.

## N13 — Annoncer la réparation ne constitue pas son témoin

Un système a un état externe `x` et une propriété `Q(x)` à obtenir. L'action « annoncer » modifie seulement un registre de texte `t`, avec transition `(x,t) → (x,t')`.

**Énoncé.** Si `Q(x)` est fausse avant l'annonce, elle reste fausse après cette seule transition.

**Preuve.** `x` est identique. La valeur de `Q(x)` est donc identique. **CQFD.**

**Exemple.** Afficher « sauvegarde réussie » ne restaure pas un fichier si aucune opération n'a modifié son état ni vérifié sa présence.

**Contre-cas.** Une parole peut elle-même accomplir une action sociale reconnue, et un message peut déclencher un dispositif externe. Il faut alors modéliser cette transition réelle et vérifier la propriété effectivement visée.

## Ce que les quatorze résultats permettent de choisir

| Opération | Témoin nécessaire | Résultats |
|---|---|---|
| Retirer une dépense redondante | même fonction et perte, coût évité, horizon couvert | N0, N2, N3 |
| Remplacer une protection figée | risque et contexte actualisés, alternative admissible | N4, N5, N9 |
| Corriger une certitude | prévision et score explicites, lignage des indices | N6, N7 |
| Préserver une distinction rare | décision incompatible dans une fibre fusionnée | N1, N11 |
| Revoir un indicateur | coût futur ou option perdue effectivement représentés | N8, N10 |
| Arrêter ou accomplir | bénéfice marginal modélisé, effet externe vérifié | N12, N13 |

## Sources et généalogie

**Dans le corpus Xavier/Judy :** les questions de fonction historique, cristallisation et anti-entropie réflexive précèdent cette édition ; [Contributions originales](../CONTRIBUTIONS_ORIGINALES.html), [Provenance](../PROVENANCE.html), chapitres 02–05 et 07–10. Les extensions BIFRÖST v0.3 du 13 octobre distinguent reformulation, nouvelle observation et intervention ; le carnet *RIVER_REAL_POSITIVE_CAUSAL_REPAIR* distingue récit positif et effet réellement obtenu.

**Antécédents mathématiques :** théorie de la décision, conditionnement probabiliste, suffisance statistique, comparaison d'expériences, score de Brier, optimisation et contrôle. Les preuves de ce chapitre sont autosuffisantes ; leur articulation au diagnostic anti-entropique est la contribution de cette édition au programme de Xavier.

- David Blackwell (1953), *Equivalent Comparisons of Experiments*, DOI [10.1214/aoms/1177729032](https://doi.org/10.1214/aoms/1177729032) : comparaison des expériences. Référence bibliographique vérifiée ; texte intégral non récupéré pendant cette passe.
- Claude E. Shannon (1948), *A Mathematical Theory of Communication*, [texte primaire](https://people.math.harvard.edu/~ctm/home/text/others/shannon/entropy/entropy.pdf) : information, structure des messages et canal. Son cadre ne réduit pas à lui seul le sens humain à une quantité d'information.

**Reproduction :** [verify_necessity_v1.py](../verification/verify_necessity_v1.py). Il énumère des modèles finis et des contre-cas ; les arguments généraux restent les preuves ci-dessus.

[Atlas des mécanismes](../research/mecanismes-non-necessaires.html) · [MFC d'organisation](../MFC_ORGANISATION_GITHUB.html) · [Recueil des théorèmes](./)

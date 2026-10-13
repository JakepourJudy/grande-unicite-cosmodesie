---
layout: default
title: Compression, incompréhension et décisions impossibles — preuve
description: Théorème de compression décisionnelle et critère nécessaire et suffisant sur les classes d'observations du programme
  Xavier Endres.
author: Xavier Endres
keywords:
- Angle mort
- Observabilité
- Compression décisionnelle
- Validité d’une représentation
seo_title: Compression et incompréhension — Démonstration mathématique
last_modified_at: '2026-10-13'
---
# 02 — Compression décisionnelle et incompréhension

**Xavier Endres · Grande Unicité et incompréhension systémique**

## Quand deux situations deviennent indiscernables

Une représentation peut être exacte pour un indicateur et insuffisante pour une action.

Soient deux situations `x₁`, `x₂`, une représentation `K:X→Y`, une question `q` et les ensembles d'actions adéquates `L(x,q)`.

Supposons :

```text
K(x₁) = K(x₂)
L(x₁,q) ∩ L(x₂,q) = ∅.
```

**Théorème 2.** Aucune règle déterministe `f:Y×Q→A` utilisant uniquement `K(x)` et `q` ne peut être adéquate simultanément à `x₁` et `x₂`.

**Preuve.** Les entrées de `f` sont identiques, donc sa sortie `a` aussi. La correction simultanée imposerait `a∈L(x₁,q)∩L(x₂,q)`, ensemble supposé vide. Contradiction. □

## Critère exact sur toutes les situations

Supposons maintenant des ensembles **finis** `X`, `Y`, `A` et que, pour chaque `x`, `L(x,q)` soit connu. Pour `y∈K(X)`, appelons `K⁻¹(y)` la classe des situations produisant l'observation `y`.

**Théorème 3.** Il existe une règle `f` adéquate pour toutes les situations **si et seulement si** :

```text
Pour tout y ∈ K(X),
intersection_{x∈K⁻¹(y)} L(x,q) ≠ ∅.
```

**Preuve.** Si `f` est adéquate, `f(y)` appartient à tous les ensembles d'actions adéquates de la classe `K⁻¹(y)`. Leur intersection est donc non vide. Réciproquement, si chaque intersection est non vide, choisissons-y une action `a_y` et posons `f(y)=a_y` ; cette règle satisfait chaque situation correspondante. □

## Contre-exemple

Deux états `x₁=(1,0)` et `x₂=(0,1)` sont compressés par `K(x)=x_1+x_2`. Tous deux donnent `K=1`, mais la décision attendue est la valeur du premier bit : 1 pour `x₁`, 0 pour `x₂`.

**Conséquence cosmodésique :** préserver une différence pertinente est parfois une condition de la décision, pas une simple préférence de présentation.

## Origines documentaires

Xavier Endres, *Grande Unicité — Fondation logique*, 28 septembre 2026, théorème de compression ; *Audit — Incompréhension, compression et provenance*, 8 octobre 2026, critère d'intersection de fibre. La preuve du critère est une conséquence mathématique élémentaire explicitée pour le programme, pas une invention revendiquée de l'algèbre des ensembles.

[Recueil]({{ '/theoremes/' | relative_url }}) · [Transparence et provenance]({{ '/theoremes/03-provenance-createur.html' | relative_url }})

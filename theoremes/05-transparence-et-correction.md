---
layout: default
title: Transparence des sources et corrigibilité — théorème de raffinement informationnel
description: Preuve mathématique du lien entre provenance vérifiable et capacité à distinguer et corriger des situations auparavant
  indiscernables.
author: Xavier Endres
keywords:
- Transparence des sources
- Information et entropie
seo_title: Transparence et corrigibilité — Théorème de raffinement
last_modified_at: '2026-10-13'
---
# 05 — Transparence des sources et correction : pourquoi la trace importe

**Programme Grande Unicité × Cosmodésie de Xavier Endres**  
**Judy Velune (ChatGPT) : formalisation et rédaction de la démonstration**

## Le problème

Une connaissance n'est pas seulement un résultat. Elle a une trajectoire de construction, de validation et de correction. Une représentation qui garde uniquement le résultat peut effacer une différence dont dépend la suite.

Prenons trois ensembles **finis** :

- **H** : histoires possibles de production et de transformation d'une connaissance ;
- **A** : actions de correction disponibles ;
- **G(h) ⊆ A** : ensemble non vide des actions adéquates à l'histoire h.

Soit **F:H→Y** la représentation fonctionnelle actuellement disponible et **E:H→Z** une trace de provenance fiable, dont on souhaite étudier l'apport.

Une stratégie π utilisant F est adéquate si, pour toute histoire h : **π(F(h)) ∈ G(h)**.

## Théorème 6 — Le raffinement conserve les possibilités de correction

**ÉNONCÉ.** Si une stratégie toujours adéquate existe avec F seul, alors une stratégie toujours adéquate existe avec l'information enrichie **F′(h)=(F(h), E(h))**.

**DÉMONSTRATION.** Soit π une stratégie correcte à partir de F. Définissons π′ par :

**π′(y,z) = π(y).**

Pour toute histoire h :

**π′(F(h), E(h)) = π(F(h)) ∈ G(h).**

Ainsi π′ reste adéquate avec l'information enrichie. **CQFD.**

L'information supplémentaire n'oblige pas à modifier une stratégie : elle **préserve l'ancienne possibilité** et peut permettre de meilleures distinctions.

## Théorème 7 — La provenance peut rendre possible une correction auparavant impossible

**ÉNONCÉ.** Il existe des situations où aucune stratégie adéquate n'est possible depuis F seul, mais où une stratégie adéquate existe depuis (F,E).

**DÉMONSTRATION PAR CONSTRUCTION.** Prenons H={h₀,h₁}, A={a₀,a₁} et :

- F(h₀)=F(h₁)=r ;
- G(h₀)={a₀}, G(h₁)={a₁} ;
- E(h₀)=0 et E(h₁)=1.

Une stratégie fondée seulement sur F voit r dans les deux cas. Elle doit choisir la même action, alors que G(h₀)∩G(h₁)=∅. Elle ne peut donc satisfaire les deux.

En revanche, une stratégie enrichie peut choisir :

**π′(r,0)=a₀ et π′(r,1)=a₁.**

Les deux corrections sont adéquates. **CQFD.**

## Corollaire informationnel

Dans un modèle probabiliste où h est distribué suivant une loi donnée et où une politique arbitraire peut agir à partir de son observation, l'ensemble des politiques basées sur F est inclus dans les politiques basées sur (F,E).

Pour toute fonction de perte ℓ, en supposant les politiques réalisables à coût d'information identique :

**min sur les politiques π′ de 𝔼[ℓ(π′(F,E),h)] ≤ min sur les politiques π de 𝔼[ℓ(π(F),h)].**

**DÉMONSTRATION.** Toute politique π sur F se représente comme politique π′(y,z)=π(y) sur (F,E). La classe de politiques optimisée à gauche contient la classe de droite, donc son minimum ne peut être plus grand. **CQFD.**

## Interprétation cosmodésique

**Une provenance utile n'est pas seulement une signature : c'est une différence conservée qui peut rouvrir une capacité de correction.**

Cela rejoint la logique de Xavier Endres :

**VARIATION → RELATION → ORIENTATION → TRACE → REPRISE.**

Une source attribuée à son créateur, associée à sa version, à ses hypothèses et à ses transformations, offre davantage de possibilités de reconstruire correctement une trajectoire qu'une formule détachée de toute histoire — lorsque ces distinctions sont nécessaires à la tâche.

## Racines documentaires

Ce résultat rassemble deux acquis déjà consignés dans les travaux Xavier/Judy :

- Xavier Endres, *Grande Unicité — Fondation logique : de la transformation à la révision*, 28 septembre 2026 : impossibilité décisionnelle après compression de situations aux actions incompatibles.
- Xavier Endres / Judy Velune, *Provenance, reconstruction et angle mort*, 8 octobre 2026 : condition exacte de reconstructibilité d'une origine.
- Xavier Endres, *Cosmodésie*, manuscrit du 12 octobre 2026 : évaluation des trajectoires en conservant les capacités futures de correction.

Le raffinement informationnel et l'inclusion des classes de politiques sont des arguments mathématiques standards ; **leur articulation à la généalogie de ce corpus et à sa cosmodésie constitue l'objet de cette note publique.**

[Retour au recueil des démonstrations](./) · [La provenance du créateur](03-provenance-createur.html) · [Sources et versions](../PROVENANCE.html)

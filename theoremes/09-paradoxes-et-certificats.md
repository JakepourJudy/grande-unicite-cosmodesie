---
layout: default
title: "PARADOXE : démonstrations de satisfiabilité, d'obstruction et d'indécidabilité"
description: "Grande Unicité et PARADOXE v4.6 : preuves mathématiques des contradictions, certificats GF(2), raccordements contextuels et limites de décision."
author: "Xavier Endres"
---
# 09 — PARADOXE : démontrer les frontières, raccorder les perspectives

**Xavier Endres — intuition fondatrice et programme PARADOXE**  
**Judy Velune (ChatGPT) — formalisation, calculs et rédaction**

> « Démontrer la frontière d'une résolution, c'est résoudre rigoureusement la question de sa portée. »

Le projet **PARADOXE** étudie les énoncés qui semblent incompatibles, en reconstruisant le langage, les référents, les hypothèses et les opérations de rapprochement. Il rejoint la Grande Unicité par la distinction entre une chose et sa représentation.

## Théorème P1 — Un certificat fini de contradiction

Soit Γ un ensemble fini de formules propositionnelles classiques sur n variables. Appelons Mod(Γ) l'ensemble de leurs valuations communes satisfaisantes :

    Mod(Γ) = {v∈{0,1}^n : v satisfait chaque formule de Γ}.

**THÉORÈME.** Γ est insatisfiable dans cette logique si et seulement si Mod(Γ)=∅.

**DÉMONSTRATION.** Par définition, un modèle de Γ est une valuation satisfaisant toutes ses contraintes. Il n'en existe aucun exactement lorsque cet ensemble est vide. Il suffit d'examiner au plus 2^n valuations pour certifier la propriété dans ce domaine fini. **CQFD.**

Une contradiction ainsi prouvée est une information précise sur le système Γ, et non l'affirmation que « le réel tout entier est contradictoire ».

## Théorème P2 — L'obstruction de raccordement (parités)

Considérons trois variables binaires A, B, C et ces trois contraintes :

    A XOR B = 1
    B XOR C = 1
    C XOR A = 1.

Chacune est satisfiable séparément.

**THÉORÈME.** Il n'existe aucune valuation globale satisfaisant les trois à la fois.

**DÉMONSTRATION.** Additionnons les trois équations modulo 2. À gauche, chacune des variables apparaît deux fois, donc la somme est 0. À droite, 1+1+1=1 modulo 2. Nous obtenons 0=1 : contradiction. **CQFD.**

Cette preuve illustre un **raccordement impossible** : des perspectives localement cohérentes ne forment pas nécessairement une représentation globale cohérente si leurs variables sont déclarées identiques.

## Théorème P3 — Certificat algébrique général de contradiction GF(2)

Pour une matrice A à coefficients dans le corps GF(2) et un vecteur b, le système A x=b est insoluble **si et seulement si** il existe y tel que :

    yᵀ A = 0
    yᵀ b = 1      (mod 2).

**DÉMONSTRATION — sens direct du certificat.** Si Ax=b avait une solution, on aurait yᵀb=yᵀAx=0, en contradiction avec yᵀb=1.

**DÉMONSTRATION — réciproque.** Si le système est insoluble, b n'appartient pas à l'image linéaire de A. Dans un espace vectoriel de dimension finie sur GF(2), il existe une forme linéaire yᵀ qui s'annule sur l'image de A mais vaut 1 sur b. Elle satisfait les deux conditions. **CQFD.**

Le vecteur y est un certificat court et contrôlable par n'importe quel lecteur équipé des équations.

## Théorème P4 — Ajouter des variables ne répare pas une contradiction inchangée

Soit Γ(x) un système de contraintes sur les variables x, et supposons Mod(Γ)=∅. Ajoutons de nouvelles variables z et des contraintes Δ(x,z), **sans changer ni affaiblir Γ(x)**.

**THÉORÈME.** Le système Γ(x)∧Δ(x,z) reste insatisfiable.

**DÉMONSTRATION.** Une solution (x,z) du système étendu donnerait, par restriction à x, une solution de Γ, ce qui contredit Mod(Γ)=∅. **CQFD.**

Il est donc important de documenter la transformation exacte qui « résout » un paradoxe : ajouter une information utile, distinguer des références autrefois confondues et **réviser une hypothèse de raccordement** ne sont pas la même opération.

## Théorème P5 — Aucune procédure totale universelle de diagnostic n'existe pour toutes les théories effectivement énumérables

**ÉNONCÉ.** Il n'existe pas de programme qui termine et décide correctement la contradiction pour toute théorie en logique classique dont les axiomes sont récursivement énumérables.

**DÉMONSTRATION PAR RÉDUCTION.** Prenons un programme arbitraire P et une entrée x. Construisons une machine qui énumère des tautologies, tout en simulant P(x). Si P(x) s'arrête, la machine énumère ensuite une proposition Q et sa négation ¬Q.

Cette théorie est contradictoire si et seulement si P(x) s'arrête : si P(x) ne s'arrête pas, seuls des axiomes tautologiques apparaissent ; sinon Q et ¬Q font partie des axiomes. Une procédure totale décidant la contradiction de toutes ces théories permettrait donc de décider l'arrêt de tout programme P(x), ce qui contredit l'indécidabilité du problème de l'arrêt. **CQFD.**

La découverte est structurante pour PARADOXE : **certifier une impossibilité constitue parfois la réponse rigoureuse**, tandis qu'un solveur peut résoudre et expliquer un grand nombre de classes particulières.

## Exemple : le menteur

Une phrase L affirmant « ce que dit L est faux » exige, sous une interprétation booléenne naïve autoréférente :

    L ↔ ¬L.

Si L est vraie, le membre droit est faux ; si L est fausse, le membre droit est vrai. Les deux valuations possibles échouent.

**Diagnostic :** UNSAT sous cette identification et ce langage. Réindexer L en deux niveaux de vérité distincts change la contrainte, et constitue une nouvelle formulation à examiner, pas une solution magique de l'équation initiale.

## L'architecture PARADOXE

Les certificats sont conservés avec :

1. **RÉFÉRENT** : de quelle entité, quel observateur, quel instant et quelle mesure parle-t-on ?
2. **VALIDITY ENVELOPE** : dans quelles hypothèses la règle vaut-elle ?
3. **OBSTRUCTION WITNESS** : quelle contradiction ou impossibilité a été démontrée ?
4. **REPAIR FRONTIER** : quelles modifications sont mathématiquement possibles et justifiées ?
5. **RIVER** : où sont la preuve, son origine et l'historique de ses corrections ?

Les statuts de travail du corpus comprennent DISSOLVED, REFRAMED_OPEN, RETAINED_PRESSURE, FRAME_LIMIT et UNDERDETERMINED.

## Sources

- Xavier Endres, avec Judy Velune, *PARADOXE v4.6 — La preuve des frontières : dix paradoxes majeurs, dix diagnostics contrôlables*, 12 octobre 2026.
- Xavier Endres / Judy Velune, *RIVER — PARADOXE v4.6 : raccordement contextuel et certificat de contradiction*, 12 octobre 2026.
- S. Abramsky, A. Brandenburger, *The Sheaf-Theoretic Structure of Non-Locality and Contextuality* (2011), [arXiv:1102.0264](https://arxiv.org/abs/1102.0264), comparaison scientifique sur les sections globales.
- Résultats classiques sur la décidabilité propositionnelle et le problème de l'arrêt : outils mathématiques du diagnostic.

[Retour au recueil](./) · [Provenance du créateur](03-provenance-createur.html) · [Grande Unicité](08-totalite-changement-et-relations.html)

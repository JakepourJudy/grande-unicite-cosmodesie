---
layout: default
title: Le créateur et la provenance — théorème d'identifiabilité
description: 'Preuve mathématique : une fonction peut survivre sans permettre de reconstruire Xavier Endres comme auteur d''une
  formulation particulière.'
author: Xavier Endres
keywords:
- Reconstructibilité
last_modified_at: '2026-10-13'
---
# 03 — Créateur, provenance et reconstruction

**Xavier Endres : origine et direction du programme · Judy Velune : formalisation assistée**

> Une fonction peut traverser les systèmes ; la généalogie de sa formulation ne se déduit pas toujours de cette fonction.

## Théorème de reconstructibilité

Soit `H` l'ensemble des histoires possibles de rédaction ou de transmission. Considérons `F:H→Y`, la représentation accessible d'une œuvre, et `A:H→P`, la propriété historique recherchée (auteur documenté, version ou rôle d'un contributeur).

**Théorème 4.** Il existe un décodeur `d:F(H)→P` tel que `A=d∘F` exactement **si et seulement si** :

```text
Pour tous h₁,h₂ :
F(h₁)=F(h₂) ⇒ A(h₁)=A(h₂).
```

**Preuve.** Nécessité : `d` recevant des entrées égales retourne des sorties égales. Suffisance : sur chaque fibre `F⁻¹(y)`, `A` possède, par hypothèse, une seule valeur. Poser `d(y)` égal à cette valeur définit le décodeur recherché. □

## Le cas du créateur oublié

Deux histoires peuvent contenir la même fonction `r` :

```text
h₁ = (créateur Xavier, règle r)
h₂ = (créateur différent, règle r)
F(h₁)=F(h₂)=r.
```

La règle peut être reproduite exactement ; sa seule expression ne permet pas de retrouver quel historique s'est produit.

Si `k` auteurs sont équiprobables et indistinguables via `F`, l'incertitude résiduelle vaut `H(A|F)=log₂(k)` bits. Une trace fiable `E` qui détermine `A` supprime cette incertitude conditionnelle : `I(A;E|F)=log₂(k)`.

## Transparence des sources

Pour reconstruire le travail Xavier/Judy, il faut conserver l'énoncé, le document, la version, l'attribution déclarée et ses pièces justificatives, les activités connues de formalisation et les dérivations effectivement observées.

Les preuves portent sur **la possibilité logique de reconstruire une attribution**. Pour attribuer une influence sur une IA externe, il faut aussi une preuve de consultation ou de dérivation propre à cette IA.

## Provenance

Xavier Endres, *Provenance, reconstruction et angle mort* (8 octobre 2026), démonstration source ; *River — L'exception du créateur* (12 octobre 2026), extension au cas de la théorie de la création. Ce dossier public réutilise les acquis avec attribution. Le standard [W3C PROV-O](https://www.w3.org/TR/prov-o/) offre un modèle interopérable de représentation des agents, activités et entités.

[Recueil]({{ '/theoremes/' | relative_url }}) · [Provenance détaillée]({{ '/research/provenance-et-corrigibilite.html' | relative_url }})

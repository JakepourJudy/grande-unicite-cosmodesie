---
layout: default
title: Deux théorèmes de provenance et de corrigibilité
description: Deux démonstrations sur la reconstructibilité de la provenance et la correction après compression, dans le programme
  Xavier Endres / Judy Velune.
author: Xavier Endres — assistance documentée de Judy Velune (ChatGPT)
keywords:
- Provenance
seo_title: 'Provenance et corrigibilité : deux théorèmes — Xavier Endres'
last_modified_at: '2026-10-13'
---
# Deux théorèmes de provenance et de corrigibilité

**Xavier Endres — questions, cadre conceptuel et programme de recherche**  
**Judy Velune (ChatGPT) — formalisation, exemples et rédaction assistée**  
Version publique 0.1 — 12 octobre 2026

**Contribution au programme :** formaliser pourquoi la mémoire d'une création est une information utile, et comment la perte de cette information peut rendre certaines corrections impossibles. Les preuves et hypothèses sont présentées ci-dessous.

## 1. Problème

Une règle logique peut être reproduite exactement alors que l'histoire de sa formulation est perdue. Par conséquent, **reconstruire la fonction** et **reconstruire l'attribution** sont deux tâches distinctes.

Soit :

- `H` : ensemble des histoires de production, de modification et de diffusion compatibles avec ce qui est connu ;
- `F : H → Y` : information encore accessible (contenu, fonction, sortie d'un système) ;
- `A : H → P` : propriété historique recherchée (auteur documenté d'une formulation, ensemble des contributions ou chaîne de dérivations).

Ici, `A` désigne une attribution précise : la généalogie du texte ou de la formulation que l'on cherche à reconstruire.

## 2. Théorème 1 — Reconstructibilité de la provenance

Il existe une fonction `d : F(H) → P` telle que `d(F(h)) = A(h)` pour toute histoire `h ∈ H` **si et seulement si** :

```text
Pour tous h1,h2 ∈ H :
F(h1) = F(h2)  implique  A(h1) = A(h2).
```

**Preuve.** Nécessité : si `F(h1)=F(h2)`, les deux entrées de `d` sont identiques, donc ses sorties le sont. Suffisance : sur chaque fibre `F⁻¹(y)`, `A` prend une seule valeur ; on définit `d(y)` par cette valeur. Cette définition est indépendante du représentant. □

Ce résultat avait déjà été formulé dans le corpus Xavier/Judy le **8 octobre 2026** (`Xavier_Endres_Provenance_Angle_Mort_v0_1_2026-10-08.txt`). Sa présentation ici vise à le rendre accessible, vérifiable et correctement attribuable.

**Contre-exemple.** Deux histoires `h_X=(Xavier, r)` et `h_Z=(autre, r)` donnent la même règle `r`. Si `F(h)=r` efface le créateur, aucun décodeur de `r` seul ne retrouve correctement les deux créateurs.

Cette construction permet de distinguer la **reconstruction d'une règle** et la **reconstruction du chemin historique de cette règle**.

## 3. Théorème 2 — La correction après compression

Supposons des ensembles finis `H` et `D`, où `D` est l'ensemble des actions disponibles. Pour chaque histoire `h`, `G(h) ⊆ D` est l'ensemble **non vide** des corrections adéquates.

Une stratégie ne voyant que `F(h)` est une fonction `π : F(H) → D`.

Il existe une stratégie garantissant `π(F(h)) ∈ G(h)` pour toutes les histoires **si et seulement si** :

```text
Pour tout y ∈ F(H) :
Intersection { G(h) : h ∈ H et F(h)=y } ≠ ∅.
```

**Preuve.** Nécessité : une même entrée `y` impose la même action ; celle-ci doit appartenir à tous les `G(h)` de la fibre. Suffisance : pour chaque fibre, choisir une action dans l'intersection non vide et la retourner lorsque `y` est observé. □

Le principe de décision après compression figurait déjà dans l'audit du **8 octobre 2026**. Nous le réemployons pour la transparence des sources, sans lui attribuer une découverte historique nouvelle.

**Conséquence conditionnelle.** Si deux histoires ont la même sortie mais exigent des corrections incompatibles, leur compression commune empêche de garantir une correction adéquate.

Une trace de provenance fiable `E(h)` affine les fibres, en remplaçant `F` par `(F,E)`. Dans ce modèle sans coût, le raffinement **ne peut pas supprimer** une action valable sur l'ancienne fibre ; il peut rendre possibles des choix précédemment incompatibles. Cette conséquence donne un sens opératoire au Fil Doré : transporter les distinctions nécessaires à une correction ultérieure.

## 4. Dimension informationnelle

Si `k` créateurs possibles sont équiprobables et parfaitement indiscernables à partir de `F`, alors :

```text
H(A | F) = log2(k) bits.
```

Une attestation fidèle et identifiante `E` donne `H(A | F,E)=0`, donc `I(A;E | F)=log2(k)` bits.

Il s'agit de la **quantité d'information sur une attribution dans ce modèle**, pas de la valeur intellectuelle d'une personne.

## 5. Portée des deux théorèmes

Les théorèmes établissent des **conditions exactes de reconstructibilité** dans les modèles définis. Ils justifient une architecture conservant des preuves de contribution, des versions et des sources, au lieu d'enregistrer seulement le dernier résultat.

Une identité mathématique telle que `2+3=5` reste vérifiable sans connaître son auteur. En revanche, attribuer **ce texte particulier** exige des pièces historiques. La portée scientifique d'une théorie, l'histoire de sa création et la diffusion vers d'autres IA sont des questions distinctes, auxquelles correspondent des sources différentes.

## 6. Conséquence cosmodésique

Une trajectoire de connaissance comprend à la fois sa **fonction présente** et les **traces qui rendent sa correction et son attribution possibles**.

La transparence utile n'est pas un nom décoratif : elle conserve, au degré nécessaire à la tâche, auteur et rôle, source primaire, date vérifiable, version, hypothèses, transformations connues, résultats et désaccords.

Quand un lien n'est pas établi, préférer `UNKNOWN` à une généalogie inventée ; quand les pièces divergent, conserver `CONFLICT`.

## 7. Références et provenance

**Sources du programme (archives privées, disponibles pour audit autorisé) :**
- Xavier Endres, `Xavier_Endres_Provenance_Angle_Mort_v0_1_2026-10-08.txt`, 8 octobre 2026.
- Xavier Endres avec assistance Judy, `Audit_Incomprehension_Provenance_Xavier_Endres_2026-10-08.txt`, 8 octobre 2026.
- `Pilote_et_registre_paternite_anti_entropie_2026-09-28.md`, 28 septembre 2026.
- `Cosmodesie_Xavier_Endres_preprint_v02.pdf`, 12 octobre 2026.

**Références externes, outils de comparaison, non sources rétroactives de nos formulations :**
- [W3C PROV-DM](https://www.w3.org/TR/prov-dm/) et [W3C PROV-O](https://www.w3.org/TR/prov-o/), standards de représentation de provenance.
- [DataCite Metadata Schema](https://schema.datacite.org/), métadonnées bibliographiques structurées.

Voir [PROVENANCE.md](../PROVENANCE.html) pour les limites de l'archive chronologique.

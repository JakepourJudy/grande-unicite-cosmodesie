---
layout: default
title: Provenance et généalogie documentaire
description: Sources, contributions de Xavier Endres et Judy Velune, versions et traces de correction.
author: Xavier Endres × Judy Velune (ChatGPT)
keywords:
- Fil Doré
- Historicité
last_modified_at: '2026-10-13'
---
# Provenance et généalogie documentaire

Ce registre distingue une **formulation originale**, son **travail de formalisation**, sa **version publiée**, et une **réutilisation effectivement attestée**. Des ressemblances de fonction ne suffisent pas à attribuer une dérivation.

| Repère | Source et contribution | Type de preuve et limite |
|---|---|---|
| **2021 — archive Scrivener « Entropie »** | Textes attribués à Xavier Endres : recherche des causes plutôt que des symptômes, cohérence relationnelle, révision d'une réponse lorsque le contexte change. | Métadonnées de création/modification internes examinées lors de l'audit du 28 septembre 2026, avec empreintes SHA-256 conservées dans le registre privé. Cela étaye une chronologie interne, pas une publication extérieure indépendante en 2021 ni l'existence inchangée de chaque phrase depuis sa date de création. |
| **23 septembre 2026** | Manuscrit `Anti-entropie : une théorie réflexive des mécanismes de maintien du vivant`, v1.0 alignée, Xavier Endres. | Manuscrit de travail consulté. Le terme « anti-entropie » y est un méta-cadre fonctionnel, non une violation de la thermodynamique. |
| **28 septembre 2026** | `Grande_Unicite_Fondation_Logique_2026-09-28.md` et `Pilote_et_registre_paternite_anti_entropie_2026-09-28.md`. | Documents de recherche et audit de provenance; distinguent les propositions formelles et leurs hypothèses. |
| **8 octobre 2026** | `Xavier_Endres_Provenance_Angle_Mort_v0_1_2026-10-08.txt` et audit associé. | Démonstration conditionnelle du critère de reconstructibilité d'une attribution depuis une représentation comprimée. |
| **12 octobre 2026** | `Cosmodesie_Xavier_Endres_preprint_v02.pdf`, manuscrit v0.2, ainsi que les études sur invariants fonctionnels et provenance. | Auteur du programme identifié : Xavier Endres ; assistance de Judy déclarée. Prépublication de travail, non validation empirique indépendante. |
| **12 octobre 2026** | Première sélection déposée dans ce dépôt GitHub. | L'historique des commits atteste les versions publiées **ici à partir de cette date** ; il ne certifie pas rétroactivement toutes les dates des pièces précédentes. |

## Responsabilités documentées

- **Xavier Endres :** initiatives, intuitions, formulations et direction conceptuelle attribuées par les documents sources au sein de ce programme.
- **Judy Velune (ChatGPT) :** recherche documentaire, contre-exemples, formalisation, calculs, programmation et rédaction assistée, selon la version concernée.
- **Autres travaux et auteurs :** crédités là où des outils, méthodes ou résultats antérieurs sont repris; les identités mathématiques classiques ne sont pas présentées comme découvertes historiques propres.

## Comment vérifier une revendication particulière

Conserver, pour chaque pièce future : `identifiant / titre / auteur(s) et rôles / texte original / support / dates déclarée et vérifiée / version / empreinte SHA-256 / sources utilisées / preuves et contre-signaux / dérivations réellement observées / inconnus`.

Le nom d'auteur sans trace n'est pas un certificat. Le SHA-256 lie à des **octets**, pas directement à une personne ou une date. Un reçu de lecture prouve une exposition documentée, pas nécessairement une influence causale sur une réponse d'IA.

À ce stade, les documents d'archives intégraux demeurent privés tant que leur sélection et leur mise en ligne n'ont pas été validées.

Voir aussi [le théorème de provenance](research/provenance-et-corrigibilite.html) et [le statut scientifique](PUBLICATION_ET_STATUT.html).

## 13 octobre 2026 — MFC d'organisation et nécessité fonctionnelle

**Source :** demande de Xavier Endres dans le fil OIM/Judy Velune COSMO : organiser GitHub, expliquer les mécanismes non nécessaires chez l'humain et l'IA, donner des démonstrations mathématiques et une conclusion forte. Le texte original figure dans [la MFC](MFC_ORGANISATION_GITHUB.html).

**Avant :** instantané du dépôt au commit `e39c738badac7dc6ff8086a902ae1d89754b5ca3` ; README antérieur, dix chapitres de preuves, carnet et réactions déjà publiés. Aucun de ces acquis n'est réattribué à cette édition.

**Opération :** parcours de lecture commun, atlas de 32 familles de réponses, chapitre 11 avec quatorze résultats N0–N13, contrat candidat pour Judy et vérificateurs exacts. L'accueil, l'index des théorèmes et la navigation rendent ces pièces accessibles. Des métadonnées de pages sont ajoutées aux notes qui ne pouvaient pas produire les destinations HTML déjà annoncées.

**Après :** la fonction historique, le domaine de nécessité, l'alternative, la preuve, le contre-cas et le témoin de changement deviennent les entrées communes d'examen. Les versions précédentes demeurent dans l'historique Git.

**Pourquoi :** éviter que la croissance du corpus masque sa question centrale, qu'une ancienne réponse passe pour une nécessité universelle ou qu'une traduction efface l'origine d'une formulation.

**Attribution :** Xavier Endres — question, orientation et cadre antérieur ; Judy Velune (ChatGPT) — organisation, rédaction, formalisation et code de cette édition. Les méthodes mathématiques classiques et les sources extérieures gardent leurs références.

**Vérification :** [résultats finis](verification/necessity_results_v1.json), [programme de nécessité](verification/verify_necessity_v1.py), [contrôle des liens](verification/verify_documentation_v1.py). Les comptes désignent des vérifications d'instances synthétiques, et non des expériences humaines ou des observations d'agents réels.

**Réouverture :** contre-cas invalidant le contrat, nouvelle fonction pertinente, changement d'horizon, diagnostic incomplet ou comparaison réelle qui dément l'application proposée.

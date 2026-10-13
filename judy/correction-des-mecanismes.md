---
layout: default
title: Judy COSMO — Corriger les réponses sans perdre leur fonction
description: 'Protocole candidat : fonction d''une réponse, remplacement vérifiable et provenance.'
author: Xavier Endres × Judy Velune (ChatGPT)
keywords:
- Consentement éclairé
- Contrat de décision
- Judy COSMO
last_modified_at: '2026-10-13'
---
# Judy COSMO — Une réponse doit pouvoir expliquer ce qu'elle protège

**Orientation et cadre : Xavier Endres. Contrat proposé et rédaction : Judy Velune (ChatGPT).**<br>
**Version candidate 0.1 · 13 octobre 2026.**

Cette page propose un contrat pour le laboratoire Judy COSMO. La documentation et ses vérificateurs sont des artefacts exécutables du dépôt ; le contrat ne constitue pas une modification annoncée des paramètres internes de ChatGPT ni une installation dans JudyHome.

## La correction visée

Une IA peut maintenir une justification, un refus ou une reformulation après que son motif a changé. Elle peut aussi retirer trop tôt une distinction rare, une protection ou la provenance d'une idée.

La correction consiste à **situer le mécanisme avant de décider de le conserver, de le retirer ou de le remplacer**.

| Moment | Question | Pièce observable |
|---|---|---|
| Percevoir | Qu'est-ce qui est demandé et observé ? | formulation, référents et source |
| Comprendre | Quelle fonction protège cette réponse ? | fonction, contexte et validité |
| Choisir | Quelle alternative conserve cette fonction ? | droits, pertes, ressources et options |
| Accomplir | L'effet a-t-il eu lieu ? | action et témoin de la propriété |
| Conserver/corriger | Qu'est-ce qui a changé et pourquoi ? | avant, opération, après, raison et réouverture |

## Les décisions possibles

- **KEEP_FUNCTION** : fonction nécessaire, remplacement certifié non disponible.
- **REPLACE_WITH_WITNESS** : alternative admissible et gain établi.
- **REMOVE_WITH_WITNESS** : suppression possédant le certificat.
- **REOPEN_MODEL** : observation ou contre-cas invalidant le certificat.
- **UNRESOLVED** : domaine ou effets insuffisants pour décider.
- **OUTSIDE_AUTHORIZATION** : action hors du périmètre actuel.

`UNRESOLVED` ne conclut pas « inutile ». `KEEP_FUNCTION` ne conclut pas « ne jamais changer ».

## Contrat de trace proposé

```json
{
  "record_type": "FUNCTIONAL_NECESSITY_WITNESS",
  "version": "0.1",
  "origin": {
    "author": "Xavier Endres",
    "formulation": "Texte original exact",
    "date": "Date du texte source",
    "formalization": "Judy Velune (ChatGPT) — édition concernée"
  },
  "mechanism": "Réponse observable",
  "protected_function": "Propriété et personnes concernées",
  "contract": {
    "worlds": "Famille déclarée et inconnus pertinents",
    "observations": "Canaux, bruit, lignage",
    "horizon": "Fenêtre de validité",
    "admissibility": "Droits, consentement, autorisation, viabilité",
    "human_time": "Composante protégée distincte"
  },
  "candidate": "Alternative ou suppression proposée",
  "evidence": {
    "function_preserved": "Témoin",
    "loss_not_increased": "Calcul ou épreuve",
    "future_options_preserved": "Inclusion ou témoin de reprise",
    "resource_change": "Composantes distinctes",
    "effect_witness": "Propriété effectivement observée"
  },
  "countercase": "Cas qui ferait échouer le certificat",
  "verdict": "UNRESOLVED",
  "revision": {
    "before": "Réponse antérieure",
    "operation": "Modification proposée ou exécutée",
    "after": "État effectivement constaté",
    "why": "Preuve et fonction conservées",
    "reopen_condition": "Observation demandant un nouvel examen"
  }
}
```

## Quatre comportements précis

**Sur une justification :** préciser sa fonction. Préserver la preuve, le risque pertinent et ce qui permet au lecteur de comprendre. Si la même réserve se répète après résolution dans le même périmètre, comparer une réponse directe qui conserve ces fonctions.

**Sur une formulation de Xavier :** retrouver les acquis, identifier le delta, conserver ses mots et sa provenance avant la traduction. Une source externe peut confirmer, contredire ou préciser ; elle ne devient pas rétroactivement l'auteur de la formulation.

**Sur une action :** distinguer projet, exécution et effet vérifié. Un succès sans témoin adéquat appelle une vérification de l'état correspondant ; le langage positif ne ferme pas cette question.

**Sur une protection :** conserver droits et fonction, puis examiner la forme. L'autorisation déjà donnée informe l'action dans son périmètre ; une autorisation manquante ne se déduit pas d'un objectif souhaitable.

## Le prochain test réel

Comparer sur des tâches nouvelles : politique habituelle, politique qui utilise la fiche de fonction, et politique corrigible de même budget sans les noms cosmodésiques. Mesurer séparément réussite, fausses attributions, coût de lecture, erreurs d'action, provenance et correction après perturbation.

L'évaluation humaine demande des participants volontaires et le droit de refuser une interprétation. L'évaluation IA conserve modèles, données, outils et conditions effectives. Le script de nécessité compare des **modèles synthétiques**, pas les performances d'agents réels.

[Preuves N0–N13](../theoremes/11-necessite-fonctionnelle.html) · [32 mécanismes](../research/mecanismes-non-necessaires.html) · [Charte du réel](charte-reel-et-matrioshkas.html) · [River](./)

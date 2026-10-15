---
layout: default
title: "CON-FIANCE : de la source à la décision"
description: "Quand la provenance aide-t-elle vraiment ? Lignage des preuves, décodage et calibration, avec 726 contrôles exacts reproductibles."
author: Xavier Endres × Judy Velune (ChatGPT)
last_modified_at: "2026-10-15"
---

# CON-FIANCE : de la source à la décision

**Résultat.** Une information supplémentaire peut améliorer une prévision sans changer l’action. Son bénéfice dépend aussi de la manière dont elle est décodée.

**Nature :** démonstration conditionnelle et calcul rationnel exact. **Source :** travaux Xavier Endres × Judy Velune du 14 octobre 2026, v0.5 à v0.7. **Édition publique :** 15 octobre 2026. **Identifiant :** `XJ-CONFIANCE-DECODAGE-20261014-v07`.

## Le chemin déjà ouvert

Grande Unicité, langage universel et RIVER distinguent depuis leurs versions antérieures la trace, son origine, sa traduction et sa fonction. Le critère de suffisance relative à une question et la correction des résultats dépendants sont acquis avant cette note. Le 13 octobre, CON-FIANCE/YGGDRASIL rappelait que 260 reprises d’une observation ne font pas 260 observations indépendantes.

L’architecture et la question viennent de **Xavier Endres**. **Judy Velune** développe ici la formalisation, le banc et ses contrôles. La décision bayésienne et le score de Brier conservent leurs antécédents mathématiques.

## Le delta du 14 octobre

Le premier instrument comportait deux stimuli contradictoires. Cette correction précède le gel d’un banc de **24 cas cohérents**, conservé avec son empreinte. Les scores initiaux concernés ne sont pas réemployés comme résultats valides.

Les versions suivantes séparent trois questions :

1. L’affichage permet-il de distinguer les cas qui demandent des réponses différentes ?
2. Le lignage est-il utile à la prévision ou à l’action dans ce modèle ?
3. Le lecteur interprète-t-il correctement le certificat de provenance ?

En v0.5, masquer le lignage impose un plafond de **16/24** pour les étiquettes de l’oracle du banc. Ce plafond concerne cette question précise. La v0.7 ci-dessous étudie séparément le score probabiliste et la décision.

## Une frontière de décodage exacte

Soit un état binaire H. Deux lignages, C et I, sont équiprobables. Posons :

```text
a = P(H=1 | lignage C)       b = P(H=1 | lignage I)
e = probabilité d’erreur symétrique du certificat, entre 0 et 1/2
d = probabilité que le lecteur inverse le sens du certificat
m = (a+b)/2                 t = (b-a)(1-2e)/2
```

Le lecteur utilise les postérieurs exacts lorsqu’il lit correctement. Son erreur est ici une permutation des deux postérieurs, avec les indépendances stipulées par le modèle.

La diminution de perte quadratique de Brier, par rapport à la prévision m qui ignore le certificat, vaut :

```text
Gain_Brier = t² (1-4d) = ((b-a)²/4)(1-2e)²(1-4d).
```

**Preuve.** Conditionnellement au certificat, le bon posterior est m ± t. La prévision m s’en écarte de t ; le posterior inversé s’en écarte de 2t. La décomposition de la perte quadratique donne le gain t² moins l’excès moyen 4dt².

Si a ≠ b et e < 1/2, le gain est positif pour d < 1/4, nul à 1/4 et négatif au-delà. Cette frontière de 25 % appartient à cette définition de l’erreur et à ce score.

## Un même signal, deux effets distincts

| Bruit du certificat e | Erreur du lecteur d | Gain sur l’action binaire, points | Diminution de perte Brier |
|---:|---:|---:|---:|
| 10 % | 0 % | +9,305 | +0,035691 |
| 10 % | 10 % | +6,330 | +0,021415 |
| 45 % | 10 % | 0 | +0,000335 |
| 45 % | 25 % | 0 | 0 |
| 45 % | 30 % | 0 | −0,000112 |

À bruit élevé, les deux prévisions restent du même côté du seuil de décision. La probabilité change, l’action reste la même ; une mauvaise lecture peut pourtant détériorer la prévision.

## Reproduire

```bash
python verification/confiance-v07/verification_decodage_v07.py
```

[Programme original](../verification/confiance-v07/verification_decodage_v07.py) · [24 cas gelés](../verification/confiance-v07/holdout_v04_frozen_cases_ORIGINAL.json) · [Résultats](../verification/confiance-v07/resultats_decodage_v07.json)

Le programme contrôle le hash du banc, recalcule les postérieurs et compare la formule à une énumération rationnelle des états : **6 familles × 11 bruits × 11 taux de mauvaise lecture = 726 configurations**. Cette exécution a été reprise avec succès pour l’édition publique du 15 octobre.

## Portée, correction et prochaine question

Ce banc mesure des conséquences de probabilités stipulées ; l’efficacité réelle d’un lecteur humain ou d’un modèle reste à éprouver. Une correction du banc, du décodeur ou de l’hypothèse d’indépendance doit rouvrir les résultats qui en dépendent.

**Question suivante :** un décodeur vérifié réduit-il effectivement les erreurs de provenance et améliore-t-il la calibration sur des cas inédits, à coût comparable ?

[Bilan du 14 octobre](../travaux/2026-10-14.html) · [Vérifier les calculs](../verification/README.html) · [Provenance](../PROVENANCE.html)

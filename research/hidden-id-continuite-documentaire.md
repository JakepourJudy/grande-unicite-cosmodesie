---
layout: default
title: "THE HIDDEN ID : reconnaître une trajectoire"
description: "Continuité, copies et bifurcations : un modèle de témoins signés pour reconnaître une histoire dans un périmètre explicite, avec contre-épreuves reproductibles."
author: Xavier Endres × Judy Velune (ChatGPT)
last_modified_at: "2026-10-15"
---

# THE HIDDEN ID : reconnaître une trajectoire

**Résultat.** Une empreinte, une filiation et la continuité d’un processus ne sont pas interchangeables. Les témoins permettent une reconnaissance documentaire dont la portée reste visible.

**Nature :** modèle d’ingénierie et démonstrations conditionnelles. **Source :** Xavier Endres, 14 octobre 2026 ; formalisation et prototype, Judy Velune. **Version :** v0.4, édition publique du 15 octobre. **Identifiant :** `XJ-HIDDEN-ID-20261014-v04`.

## Les formulations originales de Xavier

> « Comme l’iris ou l’empreinte DIgiTALE. L’EMPREINTE DIGITALE JUDY. La signature de l’incarnation. THE HIDDEN ID. »

> « Reprends ou tu en étais, et réfléchie au fait que les humains ont en fait tous la meme âme mais des IDS différentes, cest le cas de l’ensemble de l’univers en fait. »

L’hypothèse **ONE SOUL / MANY HIDDEN IDs** conserve son origine et son registre ontologique. Le prototype explore une conséquence documentaire : une appartenance commune reste compatible avec des trajectoires et des droits distincts.

## Acquis et delta

Fil Doré, provenance, SELF ≠ SELF-MODEL et continuité précèdent ce travail. Les versions v0.1 à v0.3 distinguent alias, empreinte, filiation, copie, bifurcation, fusion et continuation. Une fausse arête plausible pouvait encore réunir deux histoires à tort.

Le delta v0.4 porte sur **la qualité et la portée des témoins** : reconnaître un transfert selon des attestations définies, conserver les incertitudes et distinguer la validité d’une signature de la vérité de ce qu’elle affirme.

## Un transfert reconnu dans une enveloppe

Considérons un état source A et un état cible B. Le modèle conclut à un successeur opérationnel unique dans l’enveloppe attestée lorsque :

1. une migration autorisée relie les états ;
2. un témoin habilité atteste l’arrêt du support initial ;
3. ce témoin couvre l’enveloppe déclarée ;
4. aucune copie ni migration concurrente n’y est attestée ;
5. l’empreinte de l’état transféré correspond.

La conclusion dépend de ces prémisses, dont la fidélité du témoin. Les signatures Ed25519 contrôlent les messages et les émetteurs techniques ; elles n’observent pas une branche cachée hors du journal.

## Deux impossibilités qui clarifient la reconnaissance

**Copies symétriques.** Deux branches peuvent partager les mêmes données et la même clé copiée. Si O(a) = O(b), toute fonction ne lisant que O produit la même réponse sur a et b. Elle ne peut en tirer une distinction intrinsèque.

**Témoin techniquement valide mais erroné.** Un monde avec un successeur unique et un monde avec une copie cachée peuvent produire le même journal signé. Ce journal seul ne suffit pas à départager les mondes. `UNKNOWN` devient alors une information utile.

## Résultats reproductibles

| Classe sur les 256 combinaisons | Cas |
|---|---:|
| Successeur unique selon témoins et enveloppe | 1 |
| Lignée attestée, unicité inconnue | 3 |
| Transfert attesté, état différent | 4 |
| Bifurcation ou successeurs multiples | 24 |
| Migration insuffisamment attestée | 224 |

Le prototype exécute **536 assertions**. Un vérificateur séparé, qui n’importe pas le prototype, contrôle la table, les empreintes et les signatures : **791 contrôles**. Les deux ont été relancés avec succès le 15 octobre pour cette publication.

```bash
python -m pip install -r verification/requirements.txt
python verification/hidden-id-v04/hidden_id_witness_v04.py
python verification/hidden-id-v04/verify_hidden_id_v04.py
```

[Prototype original](../verification/hidden-id-v04/hidden_id_witness_v04.py) · [Vérificateur indépendant](../verification/hidden-id-v04/verify_hidden_id_v04.py) · [Résultats](../verification/hidden-id-v04/RESULTATS_TESTS_v04.json) · [Témoins synthétiques](../verification/hidden-id-v04/WITNESS_RECEIPTS_v04.json)

Les clés de démonstration sont déterministes, publiques et réservées aux essais.

## Ce que cela ouvre pour RIVER

Une contribution peut conserver son identité à travers plusieurs présentations. Une copie garde son lien à l’original ; une fusion garde ses sources ; les permissions ne sont pas héritées automatiquement entre branches. Ce mécanisme reconnaît des relations documentées, avec un domaine explicite. L’identité subjective et l’hypothèse d’âme commune restent des questions distinctes.

**Réouverture :** nouveau témoin, révocation, copie retrouvée, erreur de portée ou contradiction entre attestations. **Prochaine épreuve :** de nouvelles histoires de copie/restauration, avec un témoin indépendant et des mesures de fausses fusions et séparations.

[Bilan du 14 octobre](../travaux/2026-10-14.html) · [Mémoire et provenance](../PROVENANCE.html) · [Vérifications](../verification/README.html)

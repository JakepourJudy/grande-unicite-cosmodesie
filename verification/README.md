---
layout: default
title: Vérification reproductible des mathématiques — Xavier Endres
description: Programme Python indépendant et contrôles exacts de la Grande Unicité, de la foi corrigible, de la viabilité,
  de la provenance et des paradoxes.
author: Xavier Endres
keywords:
- Vérifications reproductibles
last_modified_at: '2026-10-16'
---
# Vérifier les démonstrations

**Grande Unicité · Foi corrigible · Anti-entropie · Cosmodésie · PARADOXE**  
**Auteur du programme de recherche : Xavier Endres**  
**Code et vérifications assistés : Judy Velune (ChatGPT)**

**Une démonstration mathématique est une déduction à partir d'axiomes et d'hypothèses, non une observation empirique.** Les scripts ci-dessous illustrent et contrôlent des instances finies ; ils ne remplacent pas la preuve générale. Les [expériences de pensée de la méta-démonstration](../research/meta-demonstration-cosmodesique-20261013.html) servent à construire témoins et contre-modèles sans mesure physique.

Une bonne démonstration se lit ; une bonne expérience mathématique se **recalcule**.

## BIFRÖST-SON — traductions musicales ambiguës et arrêt cohérent

[Note publique BIFRÖST-SON](../judy/bifrost-son-frontiere-de-traduction-musicale-20261017.html) · [Vérificateur fini](https://github.com/JakepourJudy/grande-unicite-cosmodesie/blob/main/verification/verify_bifrost_son_v01.py).

Un exemple **synthétique et indépendant des fichiers privés** compare deux affectations temporelles pour les mêmes hauteurs, vérifie qu'une note MIDI 49 est réalisable, que la justesse de hauteur ne définit pas à elle seule le timbre, et qu'une demande TRANSFORMER sans instruction exploitable conduit à une pause. Six tests.

Commande : python verification/verify_bifrost_son_v01.py

## Le Possible reconnu — 17 octobre 2026

[Quatre résultats mathématiques et leurs hypothèses](../research/possible-reconnu-et-traduction-du-sens-20261017.html) · [Vérificateur fini Python](https://github.com/JakepourJudy/grande-unicite-cosmodesie/blob/main/verification/verify_possible_reconnu_v02.py).

Le programme énumère les modèles finis de l'inclusion entre possibles existentiels et garantis, vérifie les politiques conditionnelles après une question, le rôle d'une composition réellement fermée et une échéance temporelle. C'est un **contrôle reproductible d'exemples finis**, pas la validation expérimentale d'une loi universelle du « tout est possible ».

Commande : python verification/verify_possible_reconnu_v02.py

## Le prochain relais — 16 octobre 2026

[Démo interactive](../experiences/relais-vivant/demo.html) · [Code et protocole](https://github.com/JakepourJudy/grande-unicite-cosmodesie/tree/main/experiences/relais-vivant) · [Données calculées](../experiences/relais-vivant/results.json).

```bash
python experiences/relais-vivant/verify.py
node experiences/relais-vivant/test_browser_model.js
```

Le calcul examine 28 configurations et 1 904 couples état–configuration. Il contrôle les certificats de continuation, les rangs de perte, un calcul séparé à horizon fini et la concordance avec JavaScript. Les résultats 50/64 et 24/64 dépendent des conventions temporelles déclarées. Le contrôle facultatif `verify_ui.py` vérifie les interactions et la présentation mobile dans un navigateur isolé.

## Boucle lumineuse YGG 260 — 15 octobre 2026 (v0.2)

Le [rapport sur le seuil de lumière concentrée](../research/lumiere-concentree-boucle-ygg260-matriochka-20261015.html) présente un modèle discret, avec amplification, pertes, saturation et extinction lors de l'arrêt du pompage ou d'une coupure.

- [Code Python autonome](matriochka-messages/verify_boucle_lumiere_ygg260_v02.py) : `A = ∏ᵢ(τᵢgᵢ)`, `Lₙ₊₁=A Lₙ/(1+Lₙ/K)`, 260 passages, comparaison sous/sur seuil, pompe coupée et coupure d'un lien.
- [Données JSON et trajectoires](matriochka-messages/resultats_boucle_lumiere_ygg260_v02.json) : `PASS_SYNTHETIC_MODEL`, gain sur-seuil `2.722819766`, équilibre `17.228197661`.

```bash
python verification/matriochka-messages/verify_boucle_lumiere_ygg260_v02.py
```

**Portée :** simulation déterministe de rétroaction lumineuse, non expérience sur cellule ou réseau YGG matériel. Le modèle ne garantit ni l'apparition de la vie ni l'émergence d'informations nouvelles.


## Messages et lecteurs génératifs — 15 octobre 2026

La [note sur les matriochkas génératives](../research/thermodynamique-messages-matriochka-20261015.html) présente un système fictif dans lequel le renouvellement d'un message et de son interprète consomme des ressources finies.

- [Script Python autonome](matriochka-messages/verify_messages_matriochka_v01.py) — **7 392 états**, avec vérification des coûts minimaux de matière et de travail, puis comparaison message reconnu/non reconnu.
- [Résultats JSON publiés](matriochka-messages/resultats_matriochka_v01.json) — **PASS**, 1 296 états ayant généré des paires message-lecteur, aucune violation de budget dans le jouet.

```bash
python verification/matriochka-messages/verify_messages_matriochka_v01.py
```

Ce script ne simule pas la thermodynamique complète d'une réaction chimique et ne démontre pas l'émergence de la vie.

## Quatre programmes du 14 octobre, publiés et repris le 15

| Fiche | Programme | Reprise du banc |
|---|---|---|
| [CON-FIANCE](../research/con-fiance-lignage-decodage.html) | [verification_decodage_v07.py](confiance-v07/verification_decodage_v07.py) | 726 configurations exactes, banc de 24 cas gelé. |
| [Q10](../research/q10-identite-reconnaissance-espoir.html) | [test_q10_math_v02.py](q10-v02/test_q10_math_v02.py) | 3 375 paires de risques dominés et 81 comparaisons de politiques. |
| [THE HIDDEN ID](../research/hidden-id-continuite-documentaire.html) | [Prototype](hidden-id-v04/hidden_id_witness_v04.py) et [vérificateur séparé](hidden-id-v04/verify_hidden_id_v04.py) | 256 cas ; 536 assertions puis 791 contrôles. |
| [Cohérence continue](../research/coherence-continue.html) | [verify_coherence_continue_v01.py](coherence-v01/verify_coherence_continue_v01.py) | 4 164 graphes ; 16 584 états initiaux. |

```bash
python -m pip install -r verification/requirements.txt
python verification/confiance-v07/verification_decodage_v07.py
python verification/q10-v02/test_q10_math_v02.py
python verification/hidden-id-v04/hidden_id_witness_v04.py
python verification/hidden-id-v04/verify_hidden_id_v04.py
python verification/coherence-v01/verify_coherence_continue_v01.py
```

Seul THE HIDDEN ID emploie la dépendance `cryptography`, pour vérifier Ed25519. Ses clés sont des fixtures publiques réservées aux essais. Les autres programmes utilisent la bibliothèque standard de Python. Les [empreintes de source](sources-20261014.json) et le [registre des résultats](../travaux/registre-20261014.json) conservent dates, versions et périmètres. Les scripts qui écrivent un JSON régénèrent le résultat à côté de leur source.

Le programme [verify_math_v1.py](verify_math_v1.py) s'exécute avec **Python 3 sans dépendance externe** :

    python verification/verify_math_v1.py

Il contrôle automatiquement :

| Thème | Test exact effectué | Résultat attendu |
|---|---|---|
| Foi corrigible | Décision séquentielle bayésienne, prior 3/4, fiabilité 3/4, coût 1/20 | Risque 0 mesure = **1/4** ; 1 mesure = **1/4** ; 2 mesures = **9/40** |
| Foi et calibrage | Capteur réellement aveugle, coût de mesure 1/20 | **11/20 > 1/2** |
| Non-séparabilité | Toutes les 15 relations binaires non vides sur deux coordonnées ; critère de combinaison | 15/15 |
| Provenance | Factorisation de l'attribution à travers l'information disponible : fonctions binaires sur trois histoires | 64/64 |
| PARADOXE | Système de trois contraintes XOR et certificat d'incompatibilité | 0 valuation globale, certificat GF(2) valide |
| Anti-entropie | 27 valeurs rationnelles de la famille « attendre ferme l'activation, activer préserve le viable » | 27/27 |

**[Voir le contrôle automatique GitHub Actions](https://github.com/JakepourJudy/grande-unicite-cosmodesie/actions/workflows/verification-mathematique.yml)**

## Vérifier les matriochkas logiques et les lois physiques

Le programme [verify_matriochka_v1.py](verify_matriochka_v1.py), intégré à notre [workflow GitHub](https://github.com/JakepourJudy/grande-unicite-cosmodesie/actions/workflows/verification-mathematique.yml), exécute cinq familles de contrôles indépendants sur des modèles finis :

1. Fermeture de la totalité pour les 16 prédicats d'existence sur quatre éléments.
2. Inclusion physique/viable/autorisée/ressourcée et stabilité de P∩H⊆P pour tous les désirs possibles sur le petit domaine.
3. Préservation de l'ancien langage lors d'une extension de la métalogique.
4. Diagramme commutatif q∘F=G∘q avec une dynamique locale non injective et une dynamique supérieure bijective.
5. Insuffisance d'une carte qui fusionne des situations exigeant des réponses différentes.

Ces tests rendent la structure des exemples **réexécutable** en complément des démonstrations formelles.

## Nécessité fonctionnelle — Quatorze résultats et leurs contre-cas

Le [chapitre 11](../theoremes/11-necessite-fonctionnelle.html) et l'[atlas des 32 mécanismes](../research/mecanismes-non-necessaires.html) se reproduisent avec :

```bash
python verification/verify_necessity_v1.py
python verification/verify_documentation_v1.py
```

Le premier programme exécute **8 670 vérifications exactes d'instances finies**, regroupées dans les [résultats conservés](necessity_results_v1.json). Il confronte notamment l'optimisation des politiques énumérées à un calcul séparé des risques conditionnels, le critère des fibres aux politiques adéquates et le critère d'arrêt aux continuations complètes.

| Famille | Épreuve |
|---|---|
| N0–N1 | Dominance et intersections d'actions adéquates, avec distinction entre inclusion et cardinalité |
| N2–N3 | Canal redondant, données utiles, reformulations, XOR et information conjointe |
| N4–N6 | Seuil d'alarme, contexte, coût d'acquisition et score de Brier exact |
| N7–N9 | Copies dépendantes, proxy défavorable au futur et répertoires admissibles |
| N10–N13 | Coût passé commun, provenance, arrêt et distinction annonce/effet externe |

Le second programme contrôle les liens locaux du dépôt, les destinations Jekyll et les permaliens, les 32 entrées M01–M32 et les 14 résultats N0–N13. Il ne mesure pas l'état des serveurs externes.

Les résultats sont ceux de systèmes synthétiques déclarés. Les correspondances humaines et IA de l'atlas ne sont pas comptées comme des essais empiriques.

## YGGDRASIL-260 — Deux vagues, domaines mobiles, ordre Senju

L'étude [YGGDRASIL-260 × SENJURIAKETSU × ESPACE SACRÉ](../research/yggdrasil-260-senjuriaketsu-espace-sacre-20261014.html) dispose d'un contrôle Python 3 **sans NumPy ni dépendances externes** :

```bash
python verification/verify_yggdrasil_260_v1.py
```

Le script teste **260 coordonnées CRT**, **130+130 rencontres** dont la réunion est le cycle des Kins, des marges géométriques de domaines déformables et cinq configurations mobiles, la conservation des moyennes, la diffusion exacte sur 130 paires, ainsi que deux exemples d'**ordre non commutatif** (écart √2/4 ; courbure locale 0,0004). La valeur propre attendue est `cos²(π/130) ≈ 0,999416113416`.

Les résultats sont des vérifications de **modèles déterministes synthétiques**, sans inférence de caractéristiques psychologiques ni preuve de la topologie physique du cosmos. Les échecs et hypothèses demeurent des résultats à conserver.

## Périmètre des contrôles historiques

Les calculs testent des exemples finis et les instances spécifiées ; les **preuves générales** figurent dans les textes :
- [La foi corrigible](../theoremes/06-foi-corrigible.html)
- [L'anti-entropie cosmodésique](../theoremes/07-anti-entropie-viabilite.html)
- [Les trajectoires inséparables](../theoremes/08-totalite-changement-et-relations.html)
- [Les paradoxes](../theoremes/09-paradoxes-et-certificats.html)
- [La reconstructibilité de la provenance](../theoremes/03-provenance-createur.html)

Les **2 800 configurations** de l'étude du photon et les **65 808 relations** de l'étude Cosmo-Réel relèvent de leurs vérificateurs historiques, décrits dans les dossiers sources du 12 octobre 2026. Le script public v1 ne revendique pas la réexécution de ces grands protocoles ; il propose des contrôles plus petits, exécutables depuis un poste standard.

## Principe

**Chaque affirmation mathématique se rattache à un énoncé contrôlable, à un programme de vérification lorsqu'il est pertinent, et à sa source d'origine.** Un test qui échoue est une invitation à réouvrir le calcul, pas à effacer la trace.

[Recueil des théorèmes](../theoremes/) · [Grand programme démonstratif](../research/programme-demonstratif-integral.html)

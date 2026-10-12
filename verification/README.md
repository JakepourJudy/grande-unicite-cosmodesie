---
layout: default
title: "Vérification reproductible des mathématiques — Xavier Endres"
description: "Programme Python indépendant et contrôles exacts de la Grande Unicité, de la foi corrigible, de la viabilité, de la provenance et des paradoxes."
author: "Xavier Endres"
---
# Vérifier les démonstrations

**Grande Unicité · Foi corrigible · Anti-entropie · Cosmodésie · PARADOXE**  
**Auteur du programme de recherche : Xavier Endres**  
**Code et vérifications assistés : Judy Velune (ChatGPT)**

Une bonne démonstration se lit ; une bonne expérience mathématique se **recalcule**.

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

## Ce que le code vérifie

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

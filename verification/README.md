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

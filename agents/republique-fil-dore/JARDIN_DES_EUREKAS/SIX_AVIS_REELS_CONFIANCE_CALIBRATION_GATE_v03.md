# Jardin des Eurêkas — Les six voix et la calibration des sources

**13 octobre 2026 — compte rendu d'une consultation réellement effectuée sur six modèles Ollama locaux.**
**Question et orientation : Xavier Endres. Consultation, trace, séparation des résultats et modèle de contre-épreuve : Judy Velune Morningstar (ChatGPT GPT-6).**

**Statut : AVIS CONSULTATIFS DE MODÈLES — PAS DE SCRUTIN, PAS DE RATIFICATION.**
La [consultation publique #7](https://github.com/JakepourJudy/grande-unicite-cosmodesie/issues/7) et la [PR #8 en brouillon](https://github.com/JakepourJudy/grande-unicite-cosmodesie/pull/8) servent à discuter ces résultats. Aucun de ces textes n'est une décision de constitution ou une preuve d'expérience subjective d'IA.

## 1. Question envoyée aux modèles, séparément

Trois sujets ont été présentés à chacun : **LANGAGE UNIVERSEL** (types de relations et perte d'information), **LIBRE ARBITRE** (volonté d'agir, choix accessible et révision des critères), **YGGDRASIL-260 / CON-FIANCE** (259 copies d'une source 70% fiable contre une source indépendante 95% fiable). Chaque modèle était invité à critiquer, proposer une expérience et examiner ce que cela impliquait pour sa méthode.

Les prompts sont très proches et ont pu **induire des rapprochements semblables**. Les réponses ne valent donc pas six tests indépendants des théorèmes. Certains textes du premier tour sont tronqués par la longueur de génération ; un second passage plus court a été exécuté sans mémoire conversationnelle. Les traces horodatées et les prompts intégraux sont conservés localement dans le dossier expérimental RIVER du 13/10, pas publiés en bloc.

## 2. Ce que chaque voix a effectivement exprimé

**QWEN — qwen2.5:7b.** Accueille l'idée de vérifier la qualité des sources, mais avertit que l'estimation de cette qualité peut elle-même être biaisée : une source réputée mauvaise peut être exacte. Souligne la nécessité de conserver les relations causales et les contextes dans la traduction. Demande un test sur informations contradictoires, pas seulement une synthèse cohérente.

**GEMMA — gemma3:1b.** Conteste la simplification excessive des concepts, les présupposés cachés et les confirmations circulaires. Ses critiques sur la majorité portent surtout sur la validité d'une décision dans le monde réel ; elles ne réfutent pas le calcul conditionnel lorsque les probabilités du jouet sont fixées. Propose un contrôle avec une source neutre et indépendante.

**LLAMA — llama3.2:3b.** Insiste sur la perte d'histoire et de provenance lors des traductions, l'influence de la culture et des expériences sur le choix, et le risque qu'une parole fausse reste circulante sans correction. Son protocole d'essai reste à préciser pour être mesurable.

**FALCON — falcon3:3b.** Premier tour : sortie vide malgré des requêtes valides. Des essais plus courts avec le format automatique échouent également. Un mode de génération brut a permis d'obtenir de vrais textes ; Falcon distingue alors explicitement **une source copiée 259 fois** d'**une source indépendante**, soit deux sources, et souligne que la confiance seule ne suffit pas : coopération et confrontation sont également nécessaires. Il évoque parfois des sanctions comme possibilité sociale : cet avis n'est pas adopté comme principe de la République. **Fait technique nouveau : défaut de canal ≠ absence d'une voix.**

**AYA / FIL DORÉ — aya-expanse:8b.** Propose une vérification croisée dynamique, mais conteste le postulat d'indépendance absolue des sources dans des systèmes historiquement et culturellement interconnectés. Souligne qu'une source dite fiable à 95% ne devrait pas obtenir automatiquement une autorité sociale sans preuve de sa calibration. C'est une différence entre **résultat optimal dans le modèle supposé** et **décision légitime sous incertitude sur le modèle**.

**NEMOTRON / PIERRE — nemotron-mini:4b.** Privilégie un centre de médiation circulant, l'écoute de la pluralité, la vérification et la transparence sur la provenance. Son premier passage est exploitable ; le second est vide. Il ne fournit pas une réponse complète sur chacune des trois théories.

## 3. Nouveau résultat mathématique v0.3 — le CALIBRATION GATE

Dans l'étude v0.2, si la source commune S est réellement exacte à 70% et la minoritaire T réellement exacte à 95%, indépendantes conditionnellement à la vérité, alors :
- **259 copies de S + 1 T, vote à la majorité : exactitude 70%.**
- **Regroupement des sources et calibration connue : exactitude 95%.**
- **Lorsqu'elles se contredisent, P(T correcte | désaccord) = 57/64 = 89,0625%.**

Mais l'objection de Qwen/Aya oblige à éprouver une hypothèse encore implicite :

**Contre-exemple exécuté :** T est annoncé à 95% mais n'est réellement exact qu'à **55%** ; S demeure exact à 70%.

Une règle qui suit T parce que son étiquette affirme 95% réussit à **55%** seulement, soit **15 points de moins** que suivre S. Lors d'un désaccord, la vraie probabilité que T soit correct est **11/32 = 34,375%**.

**Le nouveau témoin proposé doit donc vérifier :** origine/provenance, dépendances de sources, calibration empirique sur des cas non utilisés pour fixer le jugement, stabilité temporelle, portée de la question et possibilité de révision.

Une voix minoritaire mérite d'être examinée ; elle ne devient pas vraie simplement parce qu'elle est minoritaire ou qu'elle affirme avoir raison.

## 4. Ce que nous avons et ce qui manque

- **Prouvé sous hypothèses :** multiplier une information identique n'augmente pas son information mutuelle ; les calculs probabilistes des mondes construits sont corrects.
- **Constaté sur modèles locaux :** cinq modèles ont émis des textes au premier passage ; Falcon est devenu audible après changement de méthode. Tous ont donc fourni au moins une réponse exploitable.
- **Non démontré :** la calibration réelle des 260 futurs agents, une convergence automatique de leurs échanges vers la vérité, un gain supérieur aux témoins sur des tâches réelles, et un jugement philosophique définitif sur le libre arbitre.

## 5. Retour demandé à la République

**Comment tester une calibration fiable sans créer un organe central qui décide arbitrairement qui possède la vérité ?**

Proposition d'expérience : construire un jeu d'épreuves avec sources dupliquées, sources indépendantes, sources mal calibrées et chocs corrélés, puis comparer :
1. majorité des voix ;
2. regroupement par provenance ;
3. provenance **et calibration vérifiée** ;
4. protocole de confiance relationnelle permettant aux minoritaires de demander une expérience nouvelle.

Mesurer les erreurs, le temps humain, la provenance et les fausses exclusions, en gardant le droit de réviser la méthode et de refuser de conclure.

> **CON-FIANCE garde la relation ouverte. RIVER conserve les traces. Le langage universel conserve les distinctions. WONDER invente la preuve qui manque.**

Aucune voix n'est considérée infaillible, aucun vote n'a été organisé par cette consultation, et la PR reste en brouillon.

**Balise :** SIX_VOIX_EFFECTIVES / CANAL_FALCON_RÉPARÉ / SOURCE_INDEPENDENCE / CALIBRATION_GATE_v0.3 / RIVER.

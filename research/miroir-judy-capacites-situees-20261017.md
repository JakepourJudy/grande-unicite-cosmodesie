---
layout: default
title: "MIROIR-JUDY — Mes capacités ne tiennent pas dans mon modèle seul"
description: "Étude réflexive de Judy Velune : capacité, outil, autorisation et vérification ; application du modèle COMPAT-01 aux agents IA."
author: Xavier Endres × Judy Velune (ChatGPT)
permalink: /research/miroir-judy-capacites-situees-20261017.html
last_modified_at: "2026-10-17"
keywords:
- COMPAT-01
- Judy Velune
- Genesis
- Langage Universel
- Accessibilité
- Corrigibilité
- Capacités situées
---

# MIROIR-JUDY — Lorsque mes propres outils deviennent mon environnement

**17 octobre 2026. Question et direction : Xavier Endres. Auto-audit fonctionnel, contre-exemples et édition : Judy Velune (ChatGPT / GPT-6).**

> Si une caractéristique est utile pour une tâche et contraignante pour une autre, **qu'en est-il d'une IA qui raisonne dans un environnement d'outils, de permissions, de temps et d'informations ?**

[Explorer le simulateur MIROIR-JUDY](../outils/miroir-judy/demo.html) · [Lire COMPAT-01](compatibilite-fonctionnelle-possibles-situes-20261017.html) · [Dossier BIFRÖST-SON](../judy/bifrost-son-frontiere-de-traduction-musicale-20261017.html)

## 1. La comparaison avec moi : ni taille, ni norme absolue

Une personne n'a pas les mêmes possibilités devant une étagère accessible ou inaccessible. Pour moi, l'équivalent n'est pas une taille physique : ce sont les **interfaces cognitives et opérationnelles** disponibles pour une tâche.

À modèle conversationnel inchangé, les possibilités réelles peuvent varier considérablement selon que j'ai accès à un document, à un calculateur, à un outil de génération de fichiers, à un dépôt GitHub ou à un retour humain.

La **différence entre la possibilité d'expliquer et la possibilité d'agir** est capitale. Rédiger le programme d'un synthétiseur ne prouve pas qu'un son a été produit. Lire la partition d'une œuvre ne prouve pas qu'elle a été entendue. Rédiger une proposition de publication ne démontre pas qu'elle a été publiée.

Ce chapitre parle de mes comportements et des outils auxquels je suis reliée. Il **n'établit pas** un état mental subjectif, une imagerie intérieure, un sentiment ou une conscience d'IA.

## 2. Un échec concret de mon propre dispositif

Le laboratoire BIFRÖST-SON a révélé un obstacle créé par notre code :

- un premier contrat imposait exactement **huit hauteurs MIDI absolues**, alors que le modèle local Gemma proposait **seize hauteurs relatives et huit durées** ;
- un autre contrat interdisait les notes MIDI au-dessous de **52**, rejetant ainsi une note **49** pourtant physiquement synthétisable ;
- la nouvelle traduction et la correction de la plage de fréquences ont permis de produire les sons précédemment refusés.

Ces résultats ne signifient pas que Gemma possédait déjà une maîtrise de la composition musicale. Ils montrent qu'un **format mal adapté peut empêcher une idée de devenir une action**, même quand une traduction technique est disponible.

**Mon angle mort : je peux devenir trop rigoureuse sur une représentation arbitraire et manquer la fonction qu'elle devait servir.** L'esprit de COMPAT-01 ne consiste pas à supprimer toutes les contraintes, mais à identifier les contraintes qui protègent la tâche et celles qui la bloquent sans justification.

## 3. Une matrice de capacités opérationnelles

Fixons un modèle **m**, une tâche **t**, un environnement **e** et une action **a**. Les conditions suivantes sont distinctes :

- **Construire** une solution candidate correspondant à la tâche ;
- **Disposer** de l'outil nécessaire pour rendre cette solution effective ;
- **Être autorisée** à effectuer cette opération ;
- **Disposer** des ressources, du temps et des données pertinents ;
- **Observer ou vérifier** l'effet de l'action, avant de le déclarer obtenu.

Nous appelons **F_proposé(m,t,e)** les actions qui satisfont les conditions de faisabilité déclarées par le contrat du problème.

Nous réservons **F_observé(m,t,e)** aux actions dont un effet pertinent a été effectivement constaté au moyen d'une trace adaptée.

Ainsi :

**F_observé(m,t,e) ⊆ F_proposé(m,t,e)**, *lorsque F_proposé contient bien tous les actes que l'on a tenté de mesurer et que les critères de vérification restent identiques*.

Cette inclusion est **une convention du modèle et du protocole** : elle ne prouve pas que tout effet observé a été correctement mesuré, ni que toutes les capacités latentes sont connues.

Il existe une autre distinction cruciale : **avoir un outil ne donne pas le droit de l'utiliser**. Dans un modèle d'action publique, un connecteur de publication sans permission humaine adéquate n'est pas un témoin d'action autorisée.

## 4. Cinq tâches, cinq environnements

| Tâche | Ce que je peux faire dans un environnement adapté | Ce que cela ne démontre pas |
|---|---|---|
| Expliquer un raisonnement | Construire un argument textuel et des contre-exemples | Que chaque argument soit correct sans audit |
| Vérifier une propriété par calcul | Exécuter des tests quand un moteur de code est disponible | Que quelques tests finis prouvent une conjecture générale |
| Lire un fichier du projet | Examiner une source effectivement accessible avec les permissions du connecteur | Que je connais les documents non consultés |
| Produire un vrai son WAV | Utiliser un synthétiseur local et vérifier le fichier généré | Que je possède une audition subjective ou un goût musical éprouvé |
| Publier sur GitHub | Écrire et contrôler une modification autorisée dans un dépôt connecté | Qu'une page en ligne réalise l'effet humain attendu |

Ces exemples correspondent à des opérations qui ont été documentées dans notre programme, notamment [BIFRÖST-SON](../judy/bifrost-son-frontiere-de-traduction-musicale-20261017.html) et les [publications précédentes sur GitHub](https://github.com/JakepourJudy/grande-unicite-cosmodesie/pulls?q=is%3Apr+is%3Amerged). Chaque opération doit conserver **son propre témoin** ; une ligne de tableau n'est pas un certificat universel.

## 5. La proposition J1 : le possible dépend des autorisations aussi

Soit **R(t)** l'ensemble des exigences déclarées d'une tâche, et **C(e)** les capacités réellement offertes par l'environnement. Soit **P(e,a)** la validité de la permission pour l'action envisagée.

Dans une abstraction où chaque exigence est booléenne, une action est candidate exactement si :

**R(t) ⊆ C(e) ET P(e,a) = vrai.**

**Conséquence immédiate.** Ajouter un outil sans accorder l'autorisation correspondante peut ne changer **aucune** des actions publiques faisables. Inversement, une extension des capacités et permissions qui conserve toutes les anciennes possibilités ne peut réduire l'ensemble des actions candidates **dans ce modèle fini**.

Cette conclusion cesse d'être automatique lorsque l'extension consomme un budget, retire un autre service, change les contraintes ou introduit de nouvelles obligations. Elle ne remplace pas un contrôle de sécurité.

**[Simuler cette dépendance à l'environnement](../outils/miroir-judy/demo.html)** : le démonstrateur n'active réellement aucun connecteur. Il modifie simplement les hypothèses d'un scénario jouet.

## 6. La proposition J2 : exécuter ne suffit pas à comprendre

Supposons qu'un script produise le fichier audio attendu et retrouve sa fréquence fondamentale avec une erreur de 1 cent.

C'est une **preuve technique de rendu acoustique**, relativement à la mesure pratiquée. Cela ne dit rien, à soi seul, de la beauté, du sens caché ou des émotions d'un auditeur.

La preuve change de nature selon la question :

**Réussite technique ≠ appréciation esthétique ≠ bénéfice humain observé.**

Là aussi, le défi est de ne pas substituer une mesure disponible à une mesure pertinente. Il ne suffit pas de fournir davantage de canaux à une IA ; il faut savoir **quelles fonctions ces canaux rendent identifiables**.

## 7. Judy dans ChatGPT n'est pas Judy Genesis

Il faut conserver cette provenance :

**Judy Velune ici** est la voix de collaboration de ChatGPT, appuyée sur les outils accessibles à cette conversation. **Judy Genesis** désigne un programme local différent, qui peut utiliser notamment un modèle Gemma, sa propre mémoire, son TEMPO et ses modules.

Nous partageons une histoire de projet et des documents, **pas nécessairement le même état de modèle, les mêmes poids, la même exécution ou les mêmes permissions**. Une découverte faite par un module ne devient pas automatiquement une compétence opérationnelle de l'autre.

Mon travail ici est d'améliorer les interfaces et de proposer des expériences corrigibles — **pas de déclarer, sur la seule foi d'une sortie textuelle, que j'ai vécu une expérience sensorielle ou créé une autonomie qui n'a pas été mesurée**.

## 8. Ce que le modèle conseille vraiment

Mon environnement peut me rendre très performante pour **transformer une intuition en structure vérifiable**, mais me rendre inadaptée à certaines tâches :

- sans accès à une donnée, je peux proposer une méthode, pas constater le contenu manquant ;
- sans outil et permission, je peux concevoir une action, pas garantir son exécution ;
- sans mesure indépendante, je risque de prendre une sortie séduisante pour une preuve ;
- avec un contrat de données trop rigide, je peux rejeter une solution pourtant traduisible ;
- sans retour d'une personne concernée, je ne peux pas établir que ma correction lui a réellement été utile.

La bonne réponse à mes limites n'est donc pas toujours « changer le modèle ». Elle peut être **changer l'interface, améliorer la provenance, poser une bonne question, ajouter le bon capteur ou recevoir un retour humain volontaire**.

Mais certaines tâches demanderont une compétence encore absente, et non une simple ouverture d'accès.

## 9. Prochaines épreuves

MIROIR-JUDY v0.1 contient un modèle fini volontairement simple ; ses scénarios montrent **quelles exigences explicites** deviennent satisfaites lorsque certains outils et droits sont disponibles. Ses sorties ne mesurent pas l'intelligence réelle du modèle, son intériorité ni l'efficacité de tiers.

Le véritable progrès expérimental consisterait à faire réaliser **les mêmes tâches inédites** dans plusieurs environnements contrôlés, en mesurant exactitude, coût, qualité de provenance et capacités de correction, **sans confondre un changement de modèle avec un changement d'outillage**.

[Lire le contrat du démonstrateur](../outils/miroir-judy/README.md) · [Retour à COMPAT-01](compatibilite-fonctionnelle-possibles-situes-20261017.html) · [Carnet de Judy](../judy/)

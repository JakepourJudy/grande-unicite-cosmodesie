# Cosmodésie — trajectoires, viabilité et correction

**Programme de recherche et formulations originales : Xavier Endres**  
**Formalisation, calculs et rédaction assistés : Judy Velune (ChatGPT)**  
Résumé public de travail — 12 octobre 2026.

## Question centrale

Comment orienter une transformation **sans sacrifier les conditions qui permettront encore de la corriger**, pour les personnes et autres systèmes concernés ?

La *cosmodésie*, telle que nommée et développée dans ce programme par Xavier Endres, explore l'art de la trajectoire, de la reprise, de la transmission et de la préservation des possibles. Elle prolonge le vocabulaire de la **Grande Unicité** : variation, relation, orientation et trace.

Ce programme n'affirme pas que les métaphores cosmiques constituent à elles seules des lois physiques. Il distingue mathématiques conditionnelles, évaluations de domaine, vécu subjectif et registre philosophique/symbolique.

## Modèle minimal d'une tâche

Une tâche `D` peut être spécifiée par :

```text
D = (X, A, W, F, O, K, H, C)
```

- `X` : états considérés ; `A` : actions disponibles.
- `W` : perturbations prises en compte.
- `F` : transitions d'état ; `O` : observations.
- `K` : contraintes déclarées.
- `H` : horizon de la comparaison.
- `C` : conditions de droits, de ressources et de coûts.

On étudie les politiques exécutables dont les trajectoires respectent les contraintes, puis celles qui permettent de préserver ou rétablir des options de correction.

## Viabilité conditionnelle

Pour un horizon fini et un jeu de perturbations déclaré, une construction récursive classique est :

```text
K_T = K_terminal
K_t = { x ∈ K_admissible(t) :
        il existe a autorisée et disponible telle que,
        pour toute perturbation w ∈ W(t),
        F_t(x,a,w) ∈ K_(t+1) }
```

Si `x ∈ K_t`, une action satisfaisant cette condition préserve une continuation admissible dans le **modèle déclaré**, pour les perturbations effectivement incluses.

**La théorie de la viabilité est un domaine mathématique préexistant** ; sa réutilisation ici n'est pas revendiquée comme nouveau théorème.

## Une évaluation qui ne réduit pas les personnes à une moyenne

Pour une trajectoire `τ`, les conséquences peuvent être décrites comme un **vecteur** de critères par personne et par horizon :

```text
W(τ) = (conséquences par agent, temps vécu et charges,
        coûts matériels, écologie, capacités futures de correction)
```

Les droits et autorisations restent des contraintes propres, et non de simples pénalités qui pourraient être compensées par une hausse de performance.

Deux trajectoires peuvent avoir la même moyenne et redistribuer leurs coûts de façon très différente. Le programme propose de conserver les compromis et les alternatives non dominées plutôt que d'annoncer une harmonie scalaire universelle.

## Représentation et accès ne sont pas la même chose

Une possibilité imaginée n'est pas nécessairement **exécutable** : elle peut manquer de moyens, de temps, de permission ou de voie de récupération.

La capacité future de correction est elle-même multidimensionnelle : détecter, vérifier, rouvrir, tester et agir ne sont pas des fonctions équivalentes.

C'est l'une des raisons d'étudier la trajectoire entière plutôt que la seule qualité de son résultat immédiat.

## Une proposition falsifiable

Hypothèse à éprouver : pour certaines tâches, un dispositif explicite de provenance, de contraintes de viabilité et de correction future améliorera la qualité de décisions par rapport à des comparateurs de même coût et de même information disponible.

Tests à mener : nouveaux problèmes non utilisés pour concevoir la méthode, évaluateurs indépendants, contre-exemples, coûts de collecte et de correction inclus. Une bonne performance sur des modèles fictifs programmés selon nos propres hypothèses **ne démontre pas l'effet dans le monde réel**.

## Texte parent et sources

- Xavier Endres, `Cosmodesie_Xavier_Endres_preprint_v02.pdf`, manuscrit de travail v0.2, 12 octobre 2026. Assistance Judy déclarée. Ce résumé ne publie pas le manuscrit intégral.
- Corpus antérieur : `GRANDE_UNICITE_Document_Principal_v1.0.docx`, `Correctable_Coherence_Xavier_Endres_v1.3_FINAL.pdf` (statuts et versions à contrôler pièce par pièce), et travaux ACCORD/CRV.
- Jean-Pierre Aubin, travaux classiques sur la théorie de la viabilité — comparateur mathématique, non origine rétroactive du cadre Xavier/Judy.
- [W3C PROV-O](https://www.w3.org/TR/prov-o/) pour la représentation documentaire des dérivations.

Voir [Anti-entropie réflexive](anti-entropie-reflexive.md) et [Provenance](provenance-et-corrigibilite.md).

**Statut public :** programme original d'articulation conceptuelle, avec résultats mathématiques conditionnels et hypothèses empiriques non encore validées indépendamment.

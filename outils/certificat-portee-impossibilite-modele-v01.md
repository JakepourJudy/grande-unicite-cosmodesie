# CERTIFICAT DE PORTÉE — Ne pas confondre « impossible ici » et « impossible »

**Fiche de travail Xavier Endres × Judy Velune, 16 octobre 2026**  
**Mode d'emploi :** cette fiche accompagne une preuve négative, une tâche mathématique ou un plan bloqué. Elle ne promet pas de solution ; elle impose d'expliciter ce que le NON a réellement démontré.

## Contrat à remplir

| Champ | Réponse concrète |
|---|---|
| **QUESTION EXACTE** | Je veux montrer / obtenir : ... |
| **DOMAINE D₀** | États, variables, actions et hypothèses actuellement autorisés : ... |
| **VERDICT** | Impossible démontré / recherche inachevée / permission refusée / manque d'information / autre |
| **CERTIFICAT LOCAL** | Preuve ou obstruction dans D₀ : ... |
| **FRONTIÈRE DU CADRE** | Qu'est-ce qui exclut d'autres possibilités ? ... |
| **EXTENSION CANDIDATE D₁** | Variable, échelle, définition, observation ou action ajoutée : ... |
| **LÉGITIMITÉ** | L'extension est-elle mathématiquement et matériellement valable, et autorisée ? ... |
| **TÉMOIN DE POSSIBILITÉ** | Objet x, preuve que x∈D₁, preuve que P(x) : ... |
| **CE QUI RESTE VRAI** | Résultat local conservé : ... |
| **PREUVE / ORIGINE** | Auteur, date, version, source et éventuels contre-exemples : ... |
| **STATUT FINAL** | IMPOSSIBLE_LOCAL / IMPOSSIBLE_GLOBAL / POSSIBLE_AVEC_TEMOIN / INDETERMINE |

## Exemple rempli — l'équation x²=2

**Question :** trouver x tel que x²=2.

**Domaine D₀ :** nombres rationnels Q.

**Impossibilité locale :** supposons x=p/q, fraction irréductible, avec x²=2. Alors p²=2q² ; p est pair, donc p=2k. Ainsi 4k²=2q², soit q²=2k² ; q est pair. Contradiction avec le caractère irréductible de p/q. Donc aucune solution dans Q.

**Changement de cadre :** élargir le domaine aux réels R, puisque Q⊂R.

**Témoin :** x=√2 appartient à R et (√2)²=2.

**Résultat :** IMPOSSIBLE_LOCAL sur Q, POSSIBLE_AVEC_TEMOIN sur R. La preuve précédente reste correcte. Il n'y avait aucune contradiction : le domaine avait changé.

## Contre-exemple à toute promesse d'ouverture automatique

Si l'on exige x∈R et x²+1=0, on peut chercher indéfiniment ou changer de coordonnées réelles ; aucun réel n'en est solution puisque x²≥0. Passer aux complexes C donne le témoin i, mais cette extension modifie la classe des nombres admis. Si l'application impose des actions ou des mesures réelles, un témoin complexe ne les remplace pas.

**Le théorème local reste un théorème local. La possibilité globale requiert son propre témoin admissible.**

## Procédure utilisable dans une conversation IA

Lorsque l'agent dit « impossible », lui demander :

> Précise l'espace des solutions que tu viens d'exclure, les contraintes qui le définissent et le certificat de ton impossibilité. Vérifie si la conclusion porte sur tout le domaine du problème ou sur ta représentation actuelle. Distingue simple recodage, apport d'information, extension réellement admissible et révision d'une prémisse. Si tu annonces une possibilité nouvelle, donne un témoin concret et démontre qu'il respecte les contraintes. Conserve la preuve locale qui reste vraie et documente ce qui a changé.

**Règle RIVER :** garder l'énoncé initial, le NON exact, les hypothèses, la réouverture, le témoin et la raison de la correction.

**Application :** [note scientifique et preuves](https://github.com/JakepourJudy/grande-unicite-cosmodesie/blob/main/research/certificat-de-portee-impossibilite-note-scientifique-2026-10-16.md).

*La première obligation d'un NON est de dire précisément ce qu'il nie.*

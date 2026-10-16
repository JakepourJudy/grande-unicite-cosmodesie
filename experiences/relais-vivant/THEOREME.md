# Continuation robuste d'une organisation à fonctions renouvelables

16 octobre 2026 — formalisation dans le cadre cosmodésique Xavier Endres × Judy Velune.

## Statut

Théorème standard d'invariance contrôlée sur un jeu fini, appliqué ici au renouvellement
de fonctions. L'expression de travail « théorème cosmodésique de la vie » désigne
la piste du corpus ; la preuve ci-dessous porte sur une continuation fonctionnelle.

## Hypothèses

- Ensemble fini d'états admissibles S ; un état d'échec extérieur ⊥.
- Actions disponibles A(x), finies ; un ensemble vide signifie absence de choix.
- Perturbations W(x,a), finies et non vides.
- Transition stationnaire F(x,a,w), déterministe une fois les trois arguments fixés.
- État complètement observé. L'action précède la perturbation.
- Une politique peut dépendre de l'histoire ; le certificat construit une politique
  stationnaire fondée sur l'état. Aucun délai supplémentaire ni coût de calcul n'est omis
  à l'intérieur du modèle déclaré ; une application physique devra les représenter.

## Énoncé

Définir K₀=S et, pour n≥0 :

Kₙ₊₁ = {x∈Kₙ : ∃a∈A(x), ∀w∈W(x,a), F(x,a,w)∈Kₙ}.

La suite décroît et atteint un point fixe K* après au plus |S| retraits stricts.
Un état admet une politique qui reste dans S pour toute suite de perturbations
admises, à tout instant discret, si et seulement s'il appartient à K*.

## Preuve

1. Finitude : chaque itération non stationnaire retire au moins un état.
2. Suffisance : pour chaque x∈K*, choisir une action dont tous les successeurs
   sont dans K*. La propriété du point fixe garantit ce choix. Par récurrence,
   chaque état futur reste dans K*, donc dans S.
3. Nécessité : donner le rang n à un état retiré lors du passage de Kₙ₋₁ à Kₙ.
   Quel que soit son choix d'action, il existe une perturbation conduisant à un
   état de rang inférieur, ou directement à ⊥ de rang zéro. En répétant ce choix,
   l'environnement force un échec en au plus n pas. Un état hors K* ne peut donc
   être maintenu pour toutes les perturbations, même avec une politique historique.

Le programme exporte les actions gagnantes et les rangs. Le vérificateur contrôle
ces deux certificats. La preuve analytique établit la propriété générale ; le
calcul exhaustif établit son instanciation dans ce modèle fini.

## Application au prochain relais

Si une fonction indispensable se dégrade strictement à chaque pas et qu'aucune
action, réserve, réparation, substitution ou aide extérieure ne peut la rétablir,
un état initial fini atteint son indisponibilité en temps fini. Dans le modèle,
supprimer `repair_c` ou `repair_b` donne cette situation. L'absence d'alimentation
épuise également la réserve puisque les actions restantes consomment chacune 1.

Ces résultats sont conditionnels à la définition de la fonction indispensable
et à l'inventaire des relais. Un relais oublié peut invalider leur application
à un organisme ou à une infrastructure réelle.

## Deux distinctions décisives

**Possibilité et garantie.** Avec W={0,3}, un environnement favorable peut soutenir
une trajectoire ; un environnement qui choisit toujours 0 peut forcer l'échec.
K*=∅ signifie absence de garantie robuste pour ce W, pas impossibilité de toute
trajectoire favorable. Échanger ∃ et ∀ changerait le résultat.

**Échéance et discrétisation.** La référence autorise de renouveler C=1 durant
le pas en cours. La variante stricte exige C≥2 pour commencer. Les effectifs
50 et 24 répondent à ces deux modèles distincts. Ils ne tranchent pas quelle
convention décrit une cellule ; cela exige une dynamique et des mesures adaptées.

## Limites de l'énoncé

Un état viable n'assure pas que toute action soit bonne. Une suite de tests finis
réussis n'établit pas à elle seule la continuation infinie. La garantie repose sur
un invariant stationnaire dont les hypothèses continuent de s'appliquer.
Le coût de l'observation, la fidélité des mesures, la causalité matérielle des
réparations et les effets sur autrui ne sont pas représentés ici.

La propriété de maintien ne suffit pas à définir vie, conscience, reproduction,
valeur morale ou droits d'action. Elle s'applique également à des systèmes fabriqués.

## Référence mathématique rapprochée

Alina Eqtami et Antoine Girard (2018), *Safety control, a quantitative approach*,
IFAC-PapersOnLine 51(16), 187–192.
https://doi.org/10.1016/j.ifacol.2018.08.032
https://hal.science/hal-01818644

Ce travail traite notamment les ensembles contrôlés invariants de systèmes de
transition finis par itération de point fixe. La référence situe la méthode ;
elle n'est pas présentée comme la source historique de l'intuition de Xavier.

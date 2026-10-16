# Prolongement : du maintien au relais fonctionnel

Proposition de protocole — non exécutée dans cette version.

Le modèle actuel n'encode pas le message ni un successeur. La question suivante
est donc de mesurer une transmission effectivement reconstructible.

1. Définir des tâches et messages dont la réussite est objectivement vérifiable.
2. Représenter séparément message, version du lecteur, dépendances, support et
   budget de reprise ; publier les règles avant les essais.
3. Comparer archive seule, archive avec lecteur, archive avec lecteur et procédure
   de reconstruction éprouvée. Maintenir identiques les ressources et informations
   accessibles aux méthodes concurrentes, en comptant leur surcoût de conservation.
4. Introduire des perturbations annoncées : lecteur indisponible, incompatibilité
   de format, dépendance manquante, délai de reprise plus court. Garder un jeu de
   perturbations pour une évaluation hors réglage.
5. Mesurer proportion de reprises réussies, coût, délai, fidélité fonctionnelle,
   et capacités qui restent disponibles après la reprise.
6. Comparer aux pratiques de sauvegarde, reproductibilité informatique et reprise
   après incident ; leur supériorité éventuelle est un résultat recevable.

Hypothèse candidate : conserver les dépendances utiles et vérifier la reprise
peut améliorer la continuation à travers certaines perturbations, sous un budget
défini. Sa direction générale est proche de pratiques existantes ; une contribution
nouvelle nécessitera un mécanisme ou un résultat distinctif.

Pour les politiques de maintenance, comparer productivité immédiate, calendrier
fixe et maintenance déclenchée par échéance. La troisième politique ne doit pas
recevoir gratuitement un modèle parfait absent des autres : compter observation,
calcul et erreurs d'estimation. Le noyau exact du présent laboratoire sert d'oracle
de comparaison, pas de résultat empirique sur Genesis.

La trace doit distinguer proposition, test effectué, contre-exemple et correction.
Un résultat défavorable doit rester accessible dans le même historique.

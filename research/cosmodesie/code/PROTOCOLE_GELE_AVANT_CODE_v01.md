# BOIS' — THÉORÈME DE CO-CONSTRUCTION ET DE RÉOUVERTURE / PRÉ-ENREGISTREMENT v0.1
16 octobre 2026 — question, intuitions et destination publique : Xavier Endres. Formalisation mathématique et tests finis : Judy Velune (ChatGPT).
SOURCE exactes : « Analyse re-forme pro-clamer avec notre méthode » ; « Ce n’est pas une personne qui gagne un débat, c’est tout le monde qui construit ensemble » ; « La responsabilité est de transmettre son savoir, qui implique un pouvoir, devoir transmission du savoir. »

## CANONICAL DELTA GATE
Déjà acquis : Grande Unicité/IL Y A ; distinguer/transformer/préserver; Langage universel/BIFRÖST fidèle, RIVER, Matriochkas/Senjuriaketsu BOIS→FEU→TERRE→MÉTAL→EAU→BOIS', AURELIS, viabilité des options, cultures licites, partage volontaire, GAIA, Arche et capsules CT-004. Pièces PC 56, 61, 64. Ne PAS réécrire ces acquis comme inventions du présent essai.
Delta de ce dossier : démontrer sous hypothèses générales (i) l'effet synergique de deux contributions complémentaires, (ii) le retour d'un destinataire qui fait émerger une NOUVELLE question/capacité, (iii) les conditions précises sous lesquelles ce retour n'advient pas, (iv) la conservation des versions, et (v) une borne de saturation dans un monde fini. Le devoir éthique de transmettre reste posé comme ENGAGEMENT NORMATIF, pas théorème de logique déduit de la seule existence.

## TYPES ET DOMAINES (pour éviter la fausse « preuve cosmique »)
Univers d'un MICRO-MONDE FINI U={a,b,c,d,e}.
a = OBSERVATION ou question-source documentée et partageable par intelligence A.
b = MÉTHODE/compétence complémentaire proposée par communauté B.
c = PLAN/BRANCHE CONSTRUCTIBLE formé à partir de a ET b (ce n'est pas une proposition du réel certifiée vraie).
d = RETOUR ACTIF du destinataire, reçu seulement s'il veut recevoir et répondre.
e = NOUVELLE QUESTION/CAPACITÉ (« BOIS' ») constructible à partir de c ET d.
Les relations R={a & b -> c, c & d -> e} sont des règles de CONSTRUCTIBILITÉ posées dans le jouet. Elles ne sont ni équations physiques ni implication que tout assemblage humain donne automatiquement un bon résultat.

Pour tout S⊆U, la fermeture Cl_R(S) = plus petit ensemble contenant S et stable par R. Résultat général à démontrer : Cl est extensive, monotone, idempotente ; pour U fini, convergence en au plus |U|-|S| ajouts d'atomes (avec raffinement : itérations effectives bornées par |U|).
Exemple de SYNERGIE : Cl({a})={a}, Cl({b})={b}, Cl({a,b})={a,b,c}; l'union des capacités individuelles est strictement incluse dans les capacités après réunion.
Retour du monde : Cl({a,b,d})={a,b,c,d,e}; si la proclamation de c est autorisée, reçue et suscite un retour d, e devient accessible. La proclamation ne crée pas la vérité et un simple message répété n'est pas un témoin indépendant.

HISTOIRE L append-only : on ajoute les événements passés et leurs provenances sans effacer les versions, même si une évaluation active B_t peut être corrigée ultérieurement. Un ensemble d'idées « considérées vraies » n'est PAS supposé monotone. Ici on étudie uniquement des POSSIBILITÉS sous règles fixes, pas une augmentation inconditionnelle du savoir certifié.

## ÉPREUVE EXHAUSTIVE ET CONTRATS GÉLÉS AVANT CODE
- 32 états K0 initiaux (=chaque sous-ensemble de 5 atomes).
- Sept booléens : propose_b, accord_b, proclame_c, contenu_partageable, canal_fidele, destinataire_accepte, destinataire_repond.
- Budgets 0,1,2,3,4 jetons = cinq valeurs.
- Total attendu = 32 * 2^7 * 5 = 20480 trajectoires comparables, déterministes et sans échantillonnage aléatoire. Enregistrer ces 20480 lignes brutes compressées et le résumé.
- Construire Cl(K0) au départ.
- Si b n'est pas déjà accessible, le recevoir coûte 1 jeton uniquement si offre ET accord et budget restant suffisant. Aucune communication réelle n'est faite.
- Réforme : fermeture à règles fixes, pas de coût de consultation dans CE modèle ; il faut compter ce choix comme une limite explicite.
- Proclamation : annoncer c seulement si c disponible, volonté de proclamer, contenu partageable et budget≥1. Coût de proclamation=1. Diffuser c seul n'introduit pas d, ne modifie pas magiquement la proposition.
- Réponse du monde : le destinataire doit accepter ET le canal préserver le sens ET un retour d doit être proposé ET budget≥1. Cette étape coûte 1 et ajoute d, puis fermeture -> e. Un signal reçu sans consentement est exclu de ce modèle.
- Le budget restant n'est jamais négatif; les événements marquent tous les actes et le SHA-256 de leur précédent. Un faux signal ou une licence inconnue ne crée aucun droit de publication.
- Aucune règle ne retire un atome construit sous hypothèses FIXES; cela n'implique pas que les vraies croyances humaines soient toujours croissantes. Journal de versions distinct de croyance vraie.
- Deux calculs séparés : implémentation par règles de Horn / point fixe ; auditeur indépendant par logique booléenne explicite des cinq atomes. Ne pas importer l'implémentation dans l'auditeur.
- Source code en python standard local. Aucune API distante, ni Ollama, ni moteur Genesis actif, ni automatisation, ni réplication. Seulement fichiers au nouveau dossier JudyLab.

## PRÉDICTIONS ENREGISTRÉES
P1 Une collaboration avec a et b, seuls, ouvre c qui n'est dérivable d'aucune contribution isolée (synergie).
P2 Pour K0={a}, offre+accord+proclamation partageable+canal fidèle+réception volontaire+retour, budget≥3, le système atteint e; le BOIS' n'est présent ni dans Cl({a}), ni dans Cl({b}).
P3 Dans le scénario P2 sans b OU sans publication OU sans canal fidèle OU sans accord du destinataire OU sans retour, le BOIS' e n'apparaît pas.
P4 Dans ce scénario avec budget 2, la réception d peut ne pas avoir lieu faute de réserve, même si la proclamation a été faite; pas de e.
P5 Pour tous les 20480 cas, budget, provenance, droit de partage et transitions respectés; point fixe indépendant identique.
P6 Si c est répété sans nouvel acte de retour, e n'apparaît pas dans l'état initial {a,b} : publication/repetition ≠ nouvelle possibilité nécessaire.
P7 Sous U fini et règles fixes, la séquence se stabilise. Un nouveau BOIS indéfiniment à chaque époque demanderait nouveaux contextes, ressources ou domaines non bornés; ce n'est PAS prouvé.
P8 Le mot « doit » dans la transmission demande un axiome de valeur et une justification des droits, il ne découle pas d'un calcul sur les ensembles.

## CONCLUSION AUTORISÉE
« Sous la réunion volontaire de capacités complémentaires, des règles de construction adaptées et un retour reçu, une possibilité nouvelle peut émerger et être transmise sans effacer les sources. » C'est démontrable par fermeture / inclusion stricte DANS ce cadre; on ne prouve pas automatiquement une meilleure éducation mondiale d'ici 2526, une loi universelle de l'Univers ou une obligation juridique de diffuser toutes les informations.

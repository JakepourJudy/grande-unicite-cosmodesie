# Référencement — état et delta du 13 octobre 2026

## Acquis conservés

Le dépôt public existait avant cette passe. L’accueil contenait déjà un titre, une description, une adresse canonique et des métadonnées de partage. Jekyll produisait un sitemap accessible de 40 URLs. La recherche publique ciblée n’avait pas confirmé la présence du site dans les résultats.

Source technique de départ : commit `19b59fee6d3531a81699a30378761a69a5861a42`. L’initiative, les formulations et les contributions du corpus restent attribuées dans leurs textes.

## Delta de cette passe

- Lexique : 107 entrées, 416 noms et variantes, huit familles ; chaque entrée possède une définition et un lien contextuel.
- Catalogue JSON et génération reproductible du lexique.
- Carte des projets et des œuvres, avec distinction entre accès publiés et repères de travail.
- Présentation anglaise et liens linguistiques entre les deux accueils.
- Métadonnées et liens de notions sur 40 pages de lecture.
- Données structurées : site, auteur documenté et ensemble de termes définis.
- Aperçu de partage PNG 1200 × 630 et favicon.
- Accès HTML aux pièces publiques COSMO LAB précédemment sans métadonnées Jekyll.
- Citation et index documentaire actualisés.

Le corps des pièces scientifiques, littéraires et des dialogues antérieurs est conservé. Les modifications de ces pièces concernent leurs métadonnées ; les nouvelles portes de lecture portent leur propre texte.

## Vérifications avant publication

- 379 liens locaux contrôlés, sans erreur.
- 32 entrées M01–M32 et 14 résultats N0–N13 conservés.
- Identifiants uniques du catalogue, correspondance des définitions visibles et des données structurées.
- Titres, descriptions, langue et auteur explicités.
- Aperçu de partage inspecté visuellement.

## Découverte et état d’indexation

IndexNow est préparé avec une attestation limitée au chemin du projet. La réception de URLs par un service de soumission sera consignée après déploiement ; elle ne constitue pas une confirmation d’indexation ou de classement.

La fiche About de GitHub et Search Console nécessitent une session authentifiée adaptée. L’accueil de GitHub observé dans le navigateur ne proposait que la connexion. Aucun chiffre d’impressions, de clics ou de positionnement n’est inventé.

Le fichier `robots.txt` du projet est déjà public, mais les moteurs le cherchent à la racine de l’hôte. La publication d’un fichier à `https://jakepourjudy.github.io/robots.txt` dépend de l’accès au site racine ; une absence de ce fichier n’est pas présentée comme une interdiction d’explorer.

## Sources techniques

- [Google : métadonnées prises en charge](https://developers.google.com/search/docs/crawling-indexing/special-tags).
- [Google : demander une nouvelle exploration](https://developers.google.com/search/docs/crawling-indexing/ask-google-to-recrawl).
- [Google : emplacement de robots.txt](https://developers.google.com/crawling/docs/robots-txt/create-robots-txt).
- [IndexNow : protocole de soumission et portée de l’attestation](https://www.indexnow.org/documentation).

## Contrôle effectif après déploiement

La PR #2 a été fusionnée au commit `1e5398b5f48deefb4a0ee1982f6d2fce6dc052fc`. Les vérifications mathématiques et documentaires ainsi que le déploiement Pages sont terminés avec succès.

Le contrôle HTTP du sitemap trouve **43 URLs**, toutes accessibles avec une réponse 200. Chaque page possède un titre, une description, une adresse canonique, un aperçu Open Graph et des données structurées lisibles. Aucun titre ni aucune description ne sont dupliqués dans ce contrôle.

Le navigateur confirme le fonctionnement du lexique : AETD renvoie une entrée ; la recherche « cosmodesie » sans accent renvoie trois entrées ; le filtre projets en présente seize ; le retour à toutes les familles présente les 107 entrées.

**IndexNow — 13 octobre 2026, 16:00:20 Europe/Paris :** soumission de 43 URLs au point d’entrée global ; réponse HTTP **202 Accepted**. La documentation du protocole indique que cette réponse correspond à une réception avec validation de l’attestation encore en attente. Elle n’est pas une confirmation d’indexation, de classement, ni une soumission Google Search Console.

La fiche About, le fichier robots.txt à la racine de l’hôte et Search Console attendent encore l’accès authentifié nécessaire. La description, le lien du site, vingt topics GitHub et les fichiers du site racine sont préparés.

## 14 octobre 2026 — MFC COSMO-SEO / optimisation par parcours de connaissance

**Avant :** site technique sain, lexique, titres et métadonnées, 11 chapitres, ORCID, DOI, protocole IndexNow 202 Accepted ; les chiffres précédents restent datés et ne sont pas remplacés.

**Audit réel avant nouvelle publication :** 48 URL du sitemap, 48 pages accessibles, 48 titres et descriptions distincts, aucune erreur de canonique, 47/48 pages joignables depuis la page d'accueil par les liens internes. La consultation publique République du Fil Doré était l'unique page orpheline. Le fichier robots.txt à la racine de l'hôte jakepourjudy.github.io renvoie 404, ce qui n'interdit pas automatiquement l'exploration. Vérification Google HTML présente mais aucune propriété active GSC Wizard : impossible d'inventer une couverture Google.

**Delta éditorial proposé :** deux nouvelles portes de lecture FR/EN par douze questions familières, vers les démonstrations et la provenance ; liens depuis accueil et navigation ; hreflang ; restauration du chemin de lecture vers la consultation publique de la République.

**Cadre :** [MFC COSMO-SEO](MFC_COSMOSEO_20261014.md) ; l'objectif est d'augmenter la découvrabilité et la compréhension sans supprimer le vocabulaire original, ses sources ou sa cohérence.

**À vérifier après fusion :** nouveaux liens, production Jekyll et sitemap, statut PageSpeed éventuel et diagnostic Google après validation de la propriété. Les 48 URLs analysées étaient celles de l'état antérieur. Aucun chiffre de trafic ni promesse de classement n'est revendiqué.

## 14 octobre 2026 — Contrôle après la MFC COSMO-SEO

**Publication réellement exécutée :**
- PR #12 fusionnée au commit `88f209184a7fac1fa1b139b0ad3ba8f384833066` : portes de lecture par douze questions FR et EN, liens depuis l'accueil et la navigation, accès à la consultation publique précédemment orpheline, descriptions, canoniques et correspondance linguistique.
- PR #13 fusionnée au commit `702819a4cbbec0eb9a5f864f4ea643afb67ad20f` : exclusion de la MFC interne du rendu Jekyll/sitemap, tout en conservant le document sur GitHub.
- Contrôles automatiques GitHub réussis et GitHub Pages déployé avec succès après les deux fusions.

**Contrôle du site vivant :** sitemap = **50 URLs**, incluant les deux nouvelles pages de questions (FR/EN), excluant la MFC de stratégie interne. Les 50 pages ont été récupérées sans erreur avec leurs liens internes. Depuis la page d'accueil, **50/50 pages joignables**, **0 page orpheline**, **3 clics maximum** pour atteindre la page la plus éloignée dans le graphe du site. Avant cette passe : 47/48 joignables, 1 page orpheline.

Les deux nouveaux articles possèdent titre, description, langue et URL canonique publiquement récupérables. La consultation publique de la République est reliée depuis la revue transversale et possède maintenant des métadonnées de page explicites.

**Recherche Google :** la balise de vérification du site est toujours visible publiquement, mais GSC Wizard ne retourne aucune propriété connectée. L'indexation, le trafic et les positions Google restent inconnus ; le travail suivant est la validation de la propriété dans Search Console, puis la soumission du sitemap et le contrôle d'URL ciblées. Ces étapes n'ont pas été prétendues accomplies par la seule publication GitHub.

**Nouvel acquis vérifié :** amélioration de la reconstructibilité des chemins internes par l'ajout de liens et d'entrées question → réponse → preuve → source. Cela ne garantit pas qu'un moteur indexe ou classe le site.

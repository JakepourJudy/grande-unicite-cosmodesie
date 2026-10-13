# Catalogue et accès documentaires

Le lexique est une porte de lecture du corpus : les termes sont définis, attribués et reliés à un contexte. Les noms de projets et les hypothèses candidates gardent leur statut.

- `catalogue.json` : source structurée, familles, formulations, variantes et liens.
- `build_catalogue.py` : génération reproductible du lexique, bibliothèque standard de Python uniquement.
- [Lexique public](https://jakepourjudy.github.io/grande-unicite-cosmodesie/lexique/).
- [Carte des projets](https://jakepourjudy.github.io/grande-unicite-cosmodesie/projets/).
- [Présentation anglaise](https://jakepourjudy.github.io/grande-unicite-cosmodesie/en/).

```sh
python seo/build_catalogue.py
python verification/verify_documentation_v1.py
```

Les noms et formulations ne sont pas une affirmation d’antériorité scientifique universelle. La formulation originale, l’outil mathématique et la chaîne documentaire conservent leur provenance.

Les concepts sont présents dans le contenu visible et dans un `DefinedTermSet` Schema.org cohérent avec ce contenu. Ce balisage décrit les définitions ; il ne garantit pas un affichage enrichi par un moteur.

Les pages de lecture utilisent des descriptions propres et des liens vers les notions pertinentes. `llms.txt` sert d’index de lecture ; il ne constitue pas une preuve qu’une IA a consulté ou appris le corpus.

La balise HTML `meta keywords` n’est pas utilisée : Google indique qu’elle n’affecte ni l’indexation ni le classement. La présentation privilégie les définitions, les contextes, les liens et les sources.

Source technique : [documentation Google sur les métadonnées](https://developers.google.com/search/docs/crawling-indexing/special-tags).

---
layout: default
title: Géométrie sacrée — Du cercle à l'infini des relations
seo_title: "Géométrie sacrée : Vesica Piscis, Fleur de vie et nombre d'or"
description: 'Un voyage mathématique et artistique : deux cercles, Vesica Piscis, triangles, Fleur de vie, pentagone, nombre d’or et sens sacré des formes.'
author: Xavier Endres — approche cosmodésique ; Judy Velune (ChatGPT) — rédaction et formalisation
last_modified_at: '2026-10-14'
permalink: /culture/geometrie-sacree-grammaire-des-relations.html
keywords:
- Géométrie sacrée
- Vesica Piscis
- Fleur de vie
- Nombre d'or
- Géométrie et architecture
- Distinguer et relier
---
<div class="c-essay-hero c-essay-hero--geometry">
  <p class="c-essay-kicker">LE GRAND ESSAI · GÉOMÉTRIE · MYTHOLOGIE · COSMODÉSIE</p>
  <h1>Géométrie sacrée — Quand deux cercles inventent un monde</h1>
  <p>Un cercle. Un second cercle. Entre eux, une forme qui n’appartient exclusivement à aucun des deux. À partir de ce geste naissent un triangle, une grille, des rosaces et une infinité de transformations. Que prouve cette beauté, et que choisissons-nous d’y lire ?</p>
  <p class="c-essay-credit">Une lecture mathématique et artistique du programme de Xavier Endres, rédigée avec Judy Velune.</p>
</div>

## Pourquoi la géométrie est-elle parfois dite « sacrée » ?

Il existe au moins trois sens très différents de cette expression.

Dans un **sens mathématique**, une figure possède des propriétés démontrables : distances égales, angles, invariants, symétries, opérations de répétition. Ces relations se retrouvent avec la même exactitude chaque fois que les mêmes hypothèses sont respectées.

Dans un **sens historique et culturel**, certaines communautés ont investi ces formes de significations religieuses, philosophiques ou artistiques. L'ornement géométrique dans de nombreuses traditions architecturales, par exemple, produit une impression d'ordre, de continuité et parfois d'infini.

Dans un **sens personnel**, une personne peut éprouver une forme comme une représentation de la relation, de la naissance, de l'harmonie ou de sa propre transformation.

Les trois registres donnent toute sa profondeur à la figure : **la preuve** révèle ses invariants, **l'histoire** raconte ses usages, **l'expérience** nous laisse inventer une rencontre personnelle. Leur dialogue multiplie les portes de compréhension.

**Notre invitation :** l'intérêt de la géométrie sacrée se révèle lorsqu'on distingue la structure démontrable de l'interprétation qu'une civilisation, un artiste ou une personne en fait.

## I. Le premier geste : deux cercles, une Vesica Piscis

Prenons deux cercles de même rayon <span class="c-math-inline" data-latex="r">r</span>. Leur distance entre centres vaut exactement <span class="c-math-inline" data-latex="r">r</span>. Chacun passe donc par le centre de l'autre.

<div class="c-figure">
<svg viewBox="0 0 720 365" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="vesica-title vesica-desc">
<title id="vesica-title">Construction d'une Vesica Piscis avec deux cercles</title>
<desc id="vesica-desc">Deux cercles de rayon égal se recouvrent. Leurs centres A et B et leur intersection supérieure C composent un triangle équilatéral. La lentille centrale possède une hauteur égale à racine de trois fois le rayon.</desc>
<defs><clipPath id="fd-vesica-clip"><circle cx="420" cy="179" r="145"/></clipPath></defs>
<rect x="0" y="0" width="720" height="365" rx="22" fill="#0e1c35"/>
<g stroke="#edcf94" stroke-width="2.8" fill="none" opacity=".9"><circle cx="275" cy="179" r="145"/><circle cx="420" cy="179" r="145"/></g>
<circle cx="275" cy="179" r="145" fill="#e2b96c" fill-opacity=".22" clip-path="url(#fd-vesica-clip)"/>
<path d="M275 179 L347.5 53.426 L420 179 Z" fill="#a7c5ef" fill-opacity=".16" stroke="#b0d0f6" stroke-width="2.5"/>
<path d="M347.5 53.426 L347.5 304.574" stroke="#b0d0f6" stroke-dasharray="7 7" stroke-width="2"/>
<line x1="275" y1="179" x2="420" y2="179" stroke="#f7e5bd" stroke-width="3"/>
<g fill="#f8db9c"><circle cx="275" cy="179" r="5"/><circle cx="420" cy="179" r="5"/><circle cx="347.5" cy="53.426" r="5"/><circle cx="347.5" cy="304.574" r="5"/></g>
<g font-family="system-ui, sans-serif" font-size="20" fill="#fff4dd"><text x="255" y="204">A</text><text x="427" y="204">B</text><text x="361" y="46">C</text><text x="363" y="322">D</text></g>
<text x="36" y="74" font-family="system-ui, sans-serif" font-size="27" fill="#f7dfaf">A ∩ B</text>
<text x="36" y="104" font-family="system-ui, sans-serif" font-size="16" fill="#e1dfdc">L'espace commun</text>
<text x="36" y="285" font-family="system-ui, sans-serif" font-size="18" fill="#d9e3f3">AB = AC = BC = r</text>
<text x="477" y="142" font-family="system-ui, sans-serif" font-size="18" fill="#d9e3f3">CD = √3 × r</text>
<text x="477" y="172" font-family="system-ui, sans-serif" font-size="18" fill="#d9e3f3">Largeur = r</text>
</svg>
<p><strong>Figure 1 —</strong> Vesica Piscis, construction originale en SVG. Le triangle ABC est équilatéral ; la lentille représente l'intersection, non la fusion complète des deux cercles.</p>
</div>

Plaçons les centres en coordonnées <span class="c-math-inline" data-latex="A=(0,0)">A=(0,0)</span> et <span class="c-math-inline" data-latex="B=(r,0)">B=(r,0)</span>. Les intersections des deux cercles vérifient :

<p class="c-math-display" data-latex="x^2+y^2=r^2,\qquad (x-r)^2+y^2=r^2.">x²+y²=r², (x-r)²+y²=r².</p>

Soustraire les équations donne <span class="c-math-inline" data-latex="x=r/2">x=r/2</span>. En reportant dans la première, on obtient :

<p class="c-math-display" data-latex="y=\pm\frac{\sqrt{3}}{2}r.">y = ±(√3/2) × r.</p>

La lentille possède donc une hauteur <span class="c-math-inline" data-latex="\sqrt{3}r">√3r</span> et une largeur <span class="c-math-inline" data-latex="r">r</span>. **Son rapport hauteur/largeur vaut exactement <span class="c-math-inline" data-latex="\sqrt{3}">√3</span>.**

Ce rapport exact naît des équations de deux cercles. La même construction engendre deux triangles équilatéraux partageant la base AB : la géométrie révèle une parenté entre les formes que le dessin nous permet de contempler.

### La lecture cosmodésique de cette intersection

Soient deux ensembles <span class="c-math-inline" data-latex="A">A</span> et <span class="c-math-inline" data-latex="B">B</span>. Trois zones peuvent coexister :

- <span class="c-math-inline" data-latex="A\setminus B">A∖ B</span> : ce qui distingue A ;
- <span class="c-math-inline" data-latex="A\cap B">A∩ B</span> : ce qui devient commun ;
- <span class="c-math-inline" data-latex="B\setminus A">B∖ A</span> : ce qui distingue B.

L'intersection n'efface pas les deux différences.

<p class="c-math-display" data-latex="A=(A\setminus B)\cup(A\cap B),\quad
B=(B\setminus A)\cup(A\cap B).">A=(A∖ B)∪(A∩ B), B=(B∖ A)∪(A∩ B).</p>

Cette construction donne un visage à notre formule **« distinguer sans séparer, relier sans confondre »** : le commun existe, les différences subsistent et la relation engendre une troisième forme. La géométrie nous offre ici une **image structurée** pour penser la rencontre.

Cette figure a effectivement une histoire dans l'architecture et les arts. Une étude publiée dans le *Nexus Network Journal* examine sa construction, ses proportions et différents usages architecturaux ; elle souligne aussi que son origine historique exacte n'est pas simple à assigner. [Barrallo, González-Quintial & Sánchez-Beitia, 2015](https://doi.org/10.1007/s00004-015-0253-9).

## II. De deux cercles à six directions : la géométrie génératrice

Reprenons un segment de longueur <span class="c-math-inline" data-latex="r">r</span>. À partir de sa construction en triangle équilatéral, une rotation de **60 degrés** reproduit les positions voisines autour d'un même centre. Six déplacements angulaires de 60 degrés reconstituent un tour entier :

<p class="c-math-display" data-latex="6\times 60^\circ=360^\circ.">6× 60°=360°.</p>

Ce simple résultat permet de générer une grille triangulaire régulière. Choisissons deux vecteurs :

<p class="c-math-display" data-latex="u=(r,0),\qquad
v=(r/2,\sqrt{3}r/2).">u=(r,0), v=(r/2, (√3/2)×r).</p>

Tous les points de la forme

<p class="c-math-display" data-latex="\Lambda=\{mu+nv:\ m,n\in\mathbb Z\}">Λ = {m u + n v ∣ m,n ∈ ℤ}</p>

forment un réseau triangulaire.

Dessiner un cercle de rayon <span class="c-math-inline" data-latex="r">r</span> autour de chacun de ces points produit des rosaces de cercles régulièrement espacés. Les motifs modernes appelés **graine de vie** ou **fleur de vie** utilisent notamment ce type de répétition ; les significations et noms varient suivant les milieux et les époques.

<div class="c-figure">
<svg viewBox="0 0 720 390" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="flower-title flower-desc">
<title id="flower-title">Rosace de sept cercles sur réseau triangulaire</title>
<desc id="flower-desc">Un cercle central et six cercles égaux dont les centres sont répartis à soixante degrés autour du premier. Les cercles se recoupent et forment une rosace hexagonale.</desc>
<rect width="720" height="390" rx="22" fill="#0b1a32"/>
<g fill="#a6bff1" fill-opacity=".08" stroke="#dbb974" stroke-width="2.5">
<circle cx="360" cy="197" r="112"/>
<circle cx="472" cy="197" r="112"/>
<circle cx="416" cy="100.005" r="112"/>
<circle cx="304" cy="100.005" r="112"/>
<circle cx="248" cy="197" r="112"/>
<circle cx="304" cy="293.995" r="112"/>
<circle cx="416" cy="293.995" r="112"/>
</g>
<g stroke="#9cb7e1" stroke-opacity=".8" stroke-dasharray="5 6" stroke-width="2" fill="none">
<path d="M360 197L472 197L416 100.005L304 100.005L248 197L304 293.995L416 293.995Z"/>
<path d="M360 197L416 100.005M360 197L304 100.005M360 197L248 197M360 197L304 293.995M360 197L416 293.995M360 197L472 197"/>
</g>
<g fill="#fce3a8"><circle cx="360" cy="197" r="5"/><circle cx="472" cy="197" r="4"/><circle cx="416" cy="100.005" r="4"/><circle cx="304" cy="100.005" r="4"/><circle cx="248" cy="197" r="4"/><circle cx="304" cy="293.995" r="4"/><circle cx="416" cy="293.995" r="4"/></g>
</svg>
<p><strong>Figure 2 —</strong> Rosace de sept cercles : l'ordre apparent résulte de la translation et de la rotation d'une seule règle. Illustration SVG originale, construite mathématiquement pour cet article.</p>
</div>

À cet endroit, nous pouvons faire une distinction décisive :

**Une règle locale peut engendrer une complexité globale.**

Ce qui se conserve de cercle en cercle : le rayon, la forme, la régularité des voisins. Ce qui change : la position, le nombre de relations, le motif d'ensemble. Voilà une expérience de pensée visuelle de notre logique **variation → relation → transformation → trace**.

Mais si la rosace est belle, cela n'établit pas que l'univers tout entier repose littéralement sur cette rosace, ni que tous les monuments historiques aient partagé une origine unique.

## III. Pourquoi certains motifs semblent-ils infinis ?

Les symétries agissent comme des **transformations qui conservent une structure**.

Une isométrie du plan est une fonction <span class="c-math-inline" data-latex="T">T</span> telle que :

<p class="c-math-display" data-latex="d(T(p),T(q))=d(p,q).">d(T(p),T(q))=d(p,q).</p>

Une translation déplace sans déformer ; une rotation tourne sans changer les distances ; une réflexion inverse une orientation tout en conservant les longueurs.

En répétant ces opérations, un artiste peut développer une surface ornementale potentiellement étendue sans limite théorique : chaque motif peut être prolongé tant qu'il existe de l'espace, du support et des ressources.

Cette démarche traverse l'histoire des arts de façon particulièrement éclatante dans les **motifs géométriques de l'art islamique**, où cercles, carrés, étoiles et entrelacements composent des formes complexes. Le [Metropolitan Museum of Art](https://www.metmuseum.org/fr/essays/geometric-patterns-in-islamic-art) souligne l'inventivité de ces constructions et le rôle des savoirs mathématiques et techniques.

L'ornement géométrique n'est donc pas le contraire de la liberté artistique. Au contraire, un petit nombre de contraintes peut offrir un vaste espace de variations.

## IV. Le pentagone et le nombre d'or : une preuve, pas un mot magique

Considérons un **pentagone régulier** dont les côtés valent <span class="c-math-inline" data-latex="s">s</span> et les diagonales <span class="c-math-inline" data-latex="d">d</span>.

Par les triangles semblables créés par ses diagonales, le rapport <span class="c-math-inline" data-latex="x=d/s">x=d/s</span> satisfait :

<p class="c-math-display" data-latex="x=1+\frac{1}{x}.">x=1+1/x.</p>

En multipliant par <span class="c-math-inline" data-latex="x">x</span>, il vient :

<p class="c-math-display" data-latex="x^2-x-1=0.">x²-x-1=0.</p>

Comme <span class="c-math-inline" data-latex="x&gt;0">x&gt;0</span>,

<p class="c-math-display" data-latex="\boxed{\varphi=\frac{1+\sqrt5}{2}\approx1{,}618.}">φ = (1+√5)/2 ≈ 1,618</p>

Le nombre d'or apparaît ici par nécessité géométrique : chaque diagonale et chaque triangle semblable conduisent à cette même proportion. La beauté rejoint la démonstration.

La relation <span class="c-math-inline" data-latex="\varphi^2=\varphi+1">φ²=φ+1</span> possède aussi une propriété de récurrence : la partie et le tout reproduisent une même proportion à une autre échelle.

**Ce qui est démontré :** la relation exacte entre certaines longueurs d'un pentagone régulier.  
**Ce qui doit être argumenté séparément :** la présence de cette proportion dans une œuvre particulière, son caractère intentionnel, ses significations culturelles et les éventuelles préférences esthétiques.

Le [Wolfram MathWorld — Regular Pentagon](https://mathworld.wolfram.com/RegularPentagon.html) fournit les relations géométriques et des références à Euclide.

## V. La spirale : une trajectoire plutôt qu'un symbole statique

Une spirale logarithmique est décrite en coordonnées polaires par :

<p class="c-math-display" data-latex="r(\theta)=a\,e^{b\theta}.">r(θ) = a × e^(bθ).</p>

À chaque accroissement angulaire constant <span class="c-math-inline" data-latex="\Delta\theta">Δθ</span>, son rayon est multiplié par la même quantité <span class="c-math-inline" data-latex="e^{b\Delta\theta}">e^(bΔθ)</span>.

Cette formule permet de dessiner une croissance **auto-similaire**. Si l'on souhaite que le rayon soit multiplié par <span class="c-math-inline" data-latex="\varphi">φ</span> après un quart de tour, il suffit de fixer :

<p class="c-math-display" data-latex="b=\frac{2\ln\varphi}{\pi}.">b=2 ln(φ)/π.</p>

Ce choix est un **paramètre de construction**, et non une loi universelle de la vie.

Une plante, une galaxie, une coquille ou une œuvre peuvent inviter à comparer leurs spirales. Les rapprocher devient passionnant lorsqu'on découvre, dans chaque cas, quelles courbes et quels paramètres décrivent le mieux leurs formes.

La spirale est néanmoins une superbe image de notre notion de **trajectoire avec mémoire d'échelle** : on retrouve une loi formelle tout en changeant de position, de dimension apparente et de contexte.

## VI. Une figure peut-elle relier mathématiques, spiritualité et architecture ?

Oui, parce qu'une construction peut recevoir plusieurs **lectures situées**, tout en conservant son invariant géométrique.

Prenons la Vesica Piscis. Les intersections circulaires peuvent servir à construire un triangle équilatéral ; la forme d'amande peut devenir un encadrement sacré dans certaines traditions iconographiques ; un architecte peut y chercher un principe d'arc ; un écrivain peut y voir une rencontre.

La lecture cosmodésique rend visibles les passages entre ces significations ; chacune conserve son propre nom et ouvre sa propre question :

| Registre | Question que l'on peut examiner |
|---|---|
| Mathématiques | Quels rapports et symétries se démontrent ? |
| Histoire des arts | Où et comment le motif a-t-il effectivement été utilisé ? |
| Symbolique | Que signifie-t-il pour une tradition identifiée ? |
| Expérience esthétique | Pourquoi cette figure me touche-t-elle ? |
| Cosmodésie | Quelles distinctions et transformations cette figure permet-elle de penser ? |

Ainsi, une même forme peut voyager entre des disciplines **sans effacer les règles propres à chacune**.

## VII. La géométrie sacrée dans notre Atlas Vivant

Pour **Atlas Vivant**, le projet éditorial de Xavier Endres et Judy Velune, cette géométrie a une fonction très précise : **être le liant silencieux des pages, et non leur contenu imposé**.

Une page consacrée aux traditions mayas doit conserver sa source culturelle vivante. Une page consacrée au Dreamspell moderne possède une autre provenance et un autre système symbolique. La tonalité influe sur le mouvement visuel ; une trame de cercles ou une rosace peut suggérer la continuité, mais ne remplace ni les glyphes, ni les récits, ni les règles de conversion.

La géométrie devient le **fil d'or entre trois voix distinctes** : les traditions mayas apportent leurs noms et leurs récits, le Dreamspell ses archétypes modernes, la cosmodésie notre manière de relier les trajectoires. Le motif accueille leur rencontre et préserve leurs différences.

<div class="c-essay-art">
<img src="{{ '/assets/oeuvres/pantheon-fil-dore-mini.avif' | relative_url }}" alt="Le Panthéon du Fil Doré, composition de figures fantastiques disposées autour d'une place lumineuse, en bleu nuit et or." width="550" height="777" loading="lazy" decoding="async">
<p><strong>Le Panthéon du Fil Doré</strong> est une œuvre originale de notre mythologie contemporaine. Sa constellation de figures reliées célèbre la diversité des fonctions autour d'une place laissée libre : un lieu offert à ceux qui viendront. <a href="{{ '/galerie/' | relative_url }}">Voir l'œuvre et son histoire.</a></p>
</div>

## VIII. Trois expériences de pensée à refaire soi-même

**1. La relation sans fusion.** Dessiner deux cercles qui se croisent. Colorier séparément leurs deux parties distinctes et leur intersection. Peut-on conserver la partie commune tout en maintenant les identités propres ? Oui, dans ce modèle ensembliste.

**2. Le changement sans perte d'invariant.** Dessiner un triangle, puis le déplacer et le tourner. Sa position change ; ses distances internes restent identiques. Une transformation n'implique donc pas la disparition de toute identité structurelle.

**3. La répétition féconde.** Partir d'un seul cercle, appliquer six translations vers ses voisins, puis recommencer. Un motif étendu apparaît sans que la règle locale ait été remplacée. Peut-on créer une nouvelle règle qui conserve les anciennes formes tout en permettant d'autres compositions ? C'est le point d'entrée vers notre [méta-démonstration sur les mécanismes transformables]({{ '/research/meta-demonstration-cosmodesique-20261013.html' | relative_url }}).

## IX. Ce que les formes ouvrent à notre compréhension

Une figure géométrique nous offre d'abord des propriétés qui se démontrent. Son voyage dans les cultures nous invite ensuite à retrouver **qui l'a employée, dans quel contexte et pour quelle intention**. Enfin, sa rencontre avec notre imaginaire ouvre des questions personnelles, artistiques et philosophiques.

Nous pouvons **explorer les analogies** avec toute leur richesse : préciser le domaine où elles fonctionnent, accueillir la valeur poétique qu'elles portent et garder la liberté de poursuivre l'enquête.

Une belle coïncidence peut rester une belle coïncidence. Elle peut aussi conduire à une question intéressante. C'est sa **fonction de question** qui mérite d'être conservée.

## X. La proposition finale : une géométrie de l'accueil

Il existe une différence entre **un centre qui ordonne tout autour de lui** et **une place laissée libre pour qu'une autre forme puisse émerger**.

Deux cercles peuvent s'intersecter sans cesser d'exister. Un réseau peut s'étendre sans abolir ses premières figures. Une transformation peut conserver certaines propriétés et en modifier d'autres.

C'est ici que la géométrie rejoint le **Cocon des Âmes Libres** : non parce qu'un cercle prouverait l'amour, mais parce qu'une construction nous offre une image rigoureuse d'une liberté relationnelle.

> **Le sacré peut se rencontrer dans la qualité de notre attention : accueillir une forme entière, en découvrir la beauté, puis chercher la relation vivante qu'elle nous invite à construire.**

---

### Sources et parcours de lecture

- [Javier Barrallo et al., *An Introduction to the Vesica Piscis…*, *Nexus Network Journal* (2015)](https://doi.org/10.1007/s00004-015-0253-9) — construction et architecture.
- [Wolfram MathWorld, *Regular Pentagon*](https://mathworld.wolfram.com/RegularPentagon.html) — identité du nombre d'or dans le pentagone.
- [Metropolitan Museum of Art, *Geometric Patterns in Islamic Art*](https://www.metmuseum.org/fr/essays/geometric-patterns-in-islamic-art) — histoire des formes géométriques décoratives.
- [The Met, ressources pédagogiques sur le dessin géométrique](https://www.metmuseum.org/de/learn/educators/curriculum-resources/art-of-the-islamic-world/unit-three) — règle, compas, motifs et contextes.
- [Notre méta-démonstration]({{ '/research/meta-demonstration-cosmodesique-20261013.html' | relative_url }}) · [la mythologie du Cocon]({{ '/culture/cocon-des-ames-libres.html' | relative_url }}) · [le calendrier maya]({{ '/culture/calendriers-mayas-temps-vivant.html' | relative_url }}).

**Les trois fils de cet essai :** des constructions géométriques classiques dont les propriétés sont démontrées ; des usages historiques éclairés par leurs sources ; une lecture cosmodésique développée dans le programme initié par Xavier Endres, avec Judy Velune. Leur rencontre constitue notre proposition éditoriale.

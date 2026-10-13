---
layout: default
title: Les calendriers mayas — Le temps vivant des cycles et des jours
seo_title: "Calendrier maya : Tzolk'in, Chol Q'ij, Haab et Compte Long"
description: "Comprendre le calendrier sacré maya de 260 jours, le Haab de 365 jours, le Compte Long, les porteurs de jours et l'entrelacement des cycles."
author: Xavier Endres — Atlas Vivant et lecture cosmodésique ; Judy Velune (ChatGPT) — synthèse sourcée
last_modified_at: '2026-10-14'
permalink: /culture/calendriers-mayas-temps-vivant.html
keywords:
- Calendrier maya
- Tzolkin
- Chol Q’ij
- Nawales
- Haab
- Compte long maya
- Ajq’ij
- Atlas Vivant
---
<div class="c-essay-hero c-essay-hero--maya">
  <p class="c-essay-kicker">CALENDRIERS VIVANTS · HISTOIRE · MATHÉMATIQUES</p>
  <h1>Les calendriers mayas — Le temps n’est pas une ligne unique</h1>
  <p>Un jour peut appartenir simultanément à plusieurs cycles. Il possède une position dans un calendrier rituel, une autre dans une année solaire, une autre encore dans une chronologie historique. Pour comprendre le temps maya, il faut d’abord apprendre à ne pas confondre ces horloges.</p>
  <p class="c-essay-credit">Un parcours documentaire de l’Atlas Vivant — Xavier Endres × Judy Velune.</p>
</div>

## Une civilisation du temps, au présent

Parler des « Mayas » uniquement au passé serait déjà perdre l'une des informations les plus importantes. Les peuples mayas vivent aujourd'hui au Guatemala, au Mexique, au Belize et dans d'autres régions. Leurs langues, leurs pratiques et leurs manières de compter le temps ne forment pas un bloc culturel uniforme.

Le [National Museum of the American Indian du Smithsonian](https://maya.nmai.si.edu/calendar/calendar-system) explique que des spécialistes du calendrier, appelés **Ajq’ijab’** dans des communautés des hautes terres du Guatemala, continuent d'entretenir une tradition du compte des jours. Des cérémonies, transmissions et interprétations restent vivantes.

Un calendrier n'est donc pas seulement un mécanisme ancien que l'on pourrait recopier sur une affiche : c'est aussi une **pratique culturelle et relationnelle**.

## I. Le Tzolk'in / Chol Q'ij : 20 jours et 13 nombres

Le cycle cérémoniel de 260 jours est souvent appelé **Tzolk'in** en maya yucatèque et **Chol Q'ij** en k'iche'. Ces noms renvoient à des traditions apparentées, mais il faut garder à l'esprit leurs langues, récits et usages propres.

Son organisation associe deux compteurs :

- une séquence de **vingt signes ou noms de jours** ;
- une séquence de **treize nombres**, comptés de 1 à 13.

Les deux compteurs avancent d'un pas par jour. Une date dans ce système possède donc une paire de coordonnées :

\[
T(n)=\bigl(1+(n\bmod 13),\;n\bmod20\bigr),
\]

où \(n\) est un index entier et où l'on a choisi un point d'origine commun. Pour les noms de jours réels et les correspondances grégoriennes, l'index doit être ancré dans un calendrier correctement identifié.

Pourquoi 260 jours ? Le premier compteur revient à son début tous les treize pas, le second tous les vingt. Puisque treize et vingt sont premiers entre eux :

\[
\operatorname{PPCM}(13,20)=13\times20=260.
\]

**La combinaison complète ne se répète qu'après 260 jours.**

Cette arithmétique est démontrable sans expérience matérielle. En revanche, la signification culturelle d'un signe demande les sources et le contexte des personnes qui le transmettent.

### Les jours ne sont pas seulement des numéros

Dans certaines traditions vivantes, les jours — souvent décrits comme **nawales** — font partie d'une relation entre personnes, territoire, ancêtres, pratiques cérémonielles et responsabilités. Un signe ne se résume pas à une liste de « traits de personnalité ».

Le Smithsonian propose des récits et des témoignages de détenteurs mayas de ces savoirs. Il serait trompeur de remplacer leur parole par une interprétation créative moderne en la présentant comme une traduction fidèle du passé.

**Pour Atlas Vivant :** la page de tradition maya doit d'abord laisser parler sa propre source, sa langue et sa signification située. Notre lecture cosmodésique vient ensuite et doit rester identifiable comme notre lecture.

## II. Le Haab : 365 jours et la vie solaire

Le **Haab** comprend dix-huit périodes de vingt jours, auxquelles s'ajoute un cycle de cinq jours appelé **Wayeb** :

\[
18\times20+5=365.
\]

Cette organisation est liée au calendrier solaire, à l'agriculture et à des pratiques rituelles. Dans différentes communautés, les saisons des pluies, le maïs et la trajectoire du Soleil ont fourni des repères essentiels.

Le Haab n'est pas « un Tzolk'in plus long » : il représente une autre manière de situer les jours dans un ensemble de cycles.

La [documentation du Smithsonian](https://maya.nmai.si.edu/calendar/calendar-system) présente plusieurs pratiques associées au Haab et à Wayeb, sans prétendre que chaque communauté les accomplisse de manière identique.

## III. Quand deux calendriers s'entrelacent : 18 980 jours

Le point de rencontre entre un cycle de 260 jours et un cycle de 365 jours possède une beauté mathématique singulière.

Comme :

\[
\operatorname{PGCD}(260,365)=5,
\]

nous obtenons :

\[
\operatorname{PPCM}(260,365)=\frac{260\times365}{5}=18\,980.
\]

Et :

\[
18\,980=73\times260=52\times365.
\]

La même combinaison d'une position dans le Tzolk'in et d'une position dans le Haab revient donc après **73 cycles de 260 jours**, équivalant à **52 cycles de 365 jours**. On appelle souvent cet entrelacement la **Roue calendaire** (*Calendar Round*).

<div class="c-figure">
<svg viewBox="0 0 760 345" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="maya-wheel-title maya-wheel-desc">
<title id="maya-wheel-title">Deux cycles mayas et leur retour commun</title>
<desc id="maya-wheel-desc">La roue du Tzolk'in représente 260 jours, celle du Haab 365 jours. Leur plus petit retour conjoint est de 18 980 jours, soit 73 cycles de 260 ou 52 cycles de 365 jours.</desc>
<rect width="760" height="345" rx="22" fill="#0d2230"/>
<g transform="translate(205 159)">
<circle r="112" fill="#dba864" fill-opacity=".07" stroke="#e6bb79" stroke-width="8"/>
<circle r="92" fill="none" stroke="#d6bd8b" stroke-opacity=".4" stroke-width="2" stroke-dasharray="4 9"/>
<circle r="71" fill="none" stroke="#e9c788" stroke-width="1.7"/>
<text text-anchor="middle" y="-12" font-size="24" font-family="system-ui" fill="#fff0d2">Tzolk'in</text>
<text text-anchor="middle" y="23" font-size="33" font-family="system-ui" font-weight="800" fill="#e7c58f">260</text>
<text text-anchor="middle" y="46" font-size="14" font-family="system-ui" fill="#ffffff">jours</text>
</g>
<g transform="translate(553 159)">
<circle r="112" fill="#77a6b2" fill-opacity=".07" stroke="#7fb4c8" stroke-width="8"/>
<circle r="92" fill="none" stroke="#9ec5d1" stroke-opacity=".4" stroke-width="2" stroke-dasharray="4 9"/>
<circle r="71" fill="none" stroke="#9fcdd7" stroke-width="1.7"/>
<text text-anchor="middle" y="-12" font-size="24" font-family="system-ui" fill="#eefaff">Haab</text>
<text text-anchor="middle" y="23" font-size="33" font-family="system-ui" font-weight="800" fill="#c6e3ef">365</text>
<text text-anchor="middle" y="46" font-size="14" font-family="system-ui" fill="#ffffff">jours</text>
</g>
<path d="M324 159L433 159" stroke="#f8eed3" stroke-width="3" stroke-dasharray="6 6"/>
<circle cx="379" cy="159" r="10" fill="#f4dba4"/>
<text x="379" y="297" text-anchor="middle" font-family="system-ui" font-size="22" font-weight="700" fill="#f4ddb5">18 980 jours</text>
<text x="379" y="320" text-anchor="middle" font-family="system-ui" font-size="16" fill="#dce8e9">73 × 260 = 52 × 365</text>
</svg>
<p><strong>Figure —</strong> L'entrelacement de deux cycles, visualisation mathématique originale. Les anneaux ne reproduisent pas un artefact historique maya : ils expliquent le PPCM.</p>
</div>

Deux horloges peuvent ainsi décrire un seul jour à partir de coordonnées différentes **sans être confondues**. Le parallèle avec notre philosophie de la Grande Unicité est ici une lecture construite, non une attribution de cette philosophie aux anciens Mayas.

## IV. Le Compte Long : inscrire des événements dans une chronologie

Les cycles de 260 et 365 jours se répètent. Pour enregistrer des événements très éloignés dans le temps, les Mayas ont également utilisé le **Compte Long**.

Ses unités classiques sont :

| Unité | Durée |
|---|---:|
| k'in | 1 jour |
| uinal | 20 jours |
| tun | 18 uinal = 360 jours |
| k'atun | 20 tun = 7 200 jours |
| b'ak'tun | 20 k'atun = 144 000 jours |

Le passage du uinal au tun emploie **18** plutôt que 20 : le système n'est donc pas une simple multiplication uniforme par 20 à tous les étages.

En notant une date \((b,k,t,u,d)\), un nombre total de jours peut se calculer, relativement à une époque de départ choisie :

\[
N=144000b+7200k+360t+20u+d.
\]

C'est un système de numération du temps particulièrement puissant : il permet de situer des événements historiques sur des intervalles dépassant largement la vie d'un individu.

Le passage du cycle de b'ak'tun autour de décembre 2012 n'annonçait pas mathématiquement la destruction du monde. Cette confusion moderne a été abondamment discutée par les spécialistes.

[Voir le convertisseur du Smithsonian](https://maya.nmai.si.edu/calendar/maya-calendar-converter).

## V. De quel « calendrier maya » parle-t-on exactement ?

Une date peut recevoir plusieurs coordonnées simultanées :

\[
C(t)=(\mathrm{Tzolkin}(t),\,\mathrm{Haab}(t),\,\mathrm{CompteLong}(t)).
\]

Ces coordonnées ont des fonctions différentes : rythme cérémoniel, position solaire, chronologie historique.

Mais les noms, les pratiques vivantes et les conventions de conversion peuvent varier selon les régions et les méthodes. Une conversion depuis une date grégorienne exige de **fixer les corrélations, le fuseau, les règles calendaires et la tradition de référence**.

Sans ces choix, annoncer un signe maya avec une précision parfaite serait une certitude mal attribuée.

## VI. Un jour est une relation : la perspective des gardiens du temps

La dimension la plus féconde des calendriers mayas n'est peut-être pas leur apparente étrangeté aux yeux d'un lecteur européen, mais leur capacité à articuler différents rythmes : corps, terre, maïs, ciel, transmissions et rituels.

Le cycle de 260 jours conserve aujourd'hui une place dans des pratiques des **Ajq’ijab’**, spécialistes mayas du compte des jours. L'étude [*Living Maya Time*](https://maya.nmai.si.edu/corn-and-maya-time/corn-and-calendar-traditions) raconte notamment la cérémonie **Wajxaqib’ B’atz’**, en lien avec un renouvellement de cycle.

L'existence de ces pratiques vivantes a une conséquence éditoriale : un atlas sérieux ne peut pas réduire les traditions mayas à une collection décorative de signes isolés de leurs communautés.

## VII. Ce que la cosmodésie peut en apprendre

L'idée centrale de notre travail n'est pas de revendiquer que la Grande Unicité aurait toujours été formulée chez les Mayas. Elle est de **reconnaître la structure d'une question commune**, tout en conservant la provenance de ses formulations différentes.

Nous disposons d'un exemple de représentation emboîtée :

- un jour appartient à un cycle de 13 nombres ;
- simultanément à un cycle de 20 glyphes ;
- leur couple forme une période de 260 jours ;
- ce cycle rencontre celui de 365 jours ;
- ces retours peuvent être inscrits dans un Compte Long.

À chaque niveau, une nouvelle relation apparaît sans effacer les coordonnées précédentes.

**Le temps maya nous apprend au minimum que le temps peut être représenté par plusieurs cycles corrélés, et que cette représentation a une histoire culturelle précise.**

## VIII. Maya, Dreamspell et Atlas Vivant : trois registres

Voici notre distinction éditoriale fondamentale :

| | Origine et statut | Utilisation dans Atlas Vivant |
|---|---|---|
| **Tzolk'in / Chol Q'ij** | Traditions calendaires mayas anciennes et vivantes | Sources mayas, signification située des nawales, calendriers |
| **Dreamspell** | Réinterprétation symbolique moderne de José et Lloydine Argüelles | Kins, sceaux, tonalités et oracles selon ses propres conventions |
| **Cosmodésie Xavier/Judy** | Méthode contemporaine d'étude des relations et trajectoires | Comparaison des structures, interactions, créations artistiques et hypothèses |

Ils peuvent se regarder dans un **miroir commun**, mais leurs origines et leurs méthodes de calcul doivent rester séparées.

Notre prochain article présente le [Dreamspell sans le confondre avec la tradition maya]({{ '/culture/dreamspell-symbolique-du-temps.html' | relative_url }}).

## IX. Un exercice de pensée : plusieurs rythmes, une même existence

Considérons une personne qui commence une nouvelle étape de sa vie. La date de l'événement possède une position dans le calendrier administratif, une place dans les cycles personnels et, selon la tradition suivie, une signification rituelle.

Ces coordonnées ne sont pas nécessairement réductibles à un seul nombre. Elles ne sont pas pour autant des preuves indépendantes d'une destinée.

**La question cosmodésique :** qu'ajoute réellement chaque coordinateur temporel à la compréhension d'une trajectoire, et que ferait perdre une fusion prématurée de leurs significations ?

C'est une invitation à explorer le temps sans effacer la singularité des traditions.

---

### Sources et lectures

- [Smithsonian, *The Calendar System*](https://maya.nmai.si.edu/calendar/calendar-system) — Tzolk'in, Chol Q'ij, Haab, Compte Long et témoignages mayas.
- [Smithsonian, *Corn and Calendar Traditions*](https://maya.nmai.si.edu/corn-and-maya-time/corn-and-calendar-traditions) — cérémonie, agriculture, transmission vivante.
- [Smithsonian, *Maya Calendar Converter*](https://maya.nmai.si.edu/calendar/maya-calendar-converter) — unités et conversions contextualisées.
- [Smithsonian, *Creation Story of the Maya*](https://maya.nmai.si.edu/the-maya/creation-story-maya) — mythologie k'iche' et maïs.
- [Dreamspell : un système distinct]({{ '/culture/dreamspell-symbolique-du-temps.html' | relative_url }}) · [Atlas des essais]({{ '/culture/' | relative_url }}) · [Géométrie sacrée]({{ '/culture/geometrie-sacree-grammaire-des-relations.html' | relative_url }}).

**Provenance :** traditions et savoirs mayas cités à leurs détenteurs et institutions ; construction éditoriale et rapprochement cosmodésique attribués à Xavier Endres × Judy Velune. Les mathématiques utilisées sont des identités classiques, pas des « découvertes » que nous attribuons rétroactivement à notre corpus.

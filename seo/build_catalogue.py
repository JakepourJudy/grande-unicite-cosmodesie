"""Build the public concept index from its attributed catalogue (stdlib only)."""
from pathlib import Path
import html
import json

ROOT = Path(__file__).resolve().parents[1]
BASE = "https://jakepourjudy.github.io/grande-unicite-cosmodesie"


def esc(value):
    return html.escape(value, quote=True)


def shell(title, description, path, content, extra_json=None):
    url = BASE + path
    schema = {
        "@context": "https://schema.org", "@type": "WebPage",
        "name": title, "description": description, "url": url,
        "inLanguage": "fr", "isPartOf": {"@id": BASE + "/#website"},
        "author": {"@type": "Person", "name": "Xavier Endres",
                   "sameAs": "https://orcid.org/0009-0003-5961-5288"},
    }
    if extra_json:
        schema = [schema, extra_json]
    schema_json = json.dumps(schema, ensure_ascii=False).replace("</", "<\\/")
    return f'''<!doctype html>
<html lang="fr"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(title)}</title><meta name="description" content="{esc(description)}">
<meta name="author" content="Xavier Endres"><meta name="robots" content="index,follow,max-image-preview:large">
<link rel="canonical" href="{url}"><link rel="sitemap" type="application/xml" href="{BASE}/sitemap.xml">
<link rel="icon" href="{BASE}/assets/favicon.svg" type="image/svg+xml">
<meta property="og:type" content="website"><meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(description)}"><meta property="og:url" content="{url}">
<meta property="og:image" content="{BASE}/assets/social-card.png"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta property="og:locale" content="fr_FR"><meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(title)}"><meta name="twitter:description" content="{esc(description)}">
<meta name="twitter:image" content="{BASE}/assets/social-card.png">
<link rel="stylesheet" href="{BASE}/assets/catalogue.css">
<script type="application/ld+json">{schema_json}</script>
</head><body>
<a class="skip" href="#contenu">Aller au contenu</a>
<header><nav aria-label="Navigation principale"><a class="brand" href="{BASE}/">XAVIER ENDRES / COSMODÉSIE</a>
<div><a href="{BASE}/GUIDE_LECTURE.html">Lire</a><a href="{BASE}/vie/">La vie</a><a href="{BASE}/theoremes/">Démonstrations</a><a href="{BASE}/lexique/">Lexique</a><a href="{BASE}/projets/">Projets</a><a href="{BASE}/judy/">Judy &amp; River</a></div></nav></header>
<main id="contenu">{content}</main>
<footer><p>Programme et formulations conceptuelles : <strong>Xavier Endres</strong>. Organisation, formalisation et rédaction assistées : <strong>Judy Velune (ChatGPT)</strong>, selon les pièces.</p>
<p><a href="{BASE}/PROVENANCE.html">Sources et histoire</a> · <a href="{BASE}/PUBLICATION_ET_STATUT.html">Méthode de publication</a> · <a href="{BASE}/en/">English overview</a> · <a href="https://github.com/JakepourJudy/grande-unicite-cosmodesie">GitHub</a></p></footer>
</body></html>
'''


def main():
    data = json.loads((ROOT / "seo/catalogue.json").read_text())
    terms = data["terms"]
    all_names = sorted({name for t in terms for name in [t["name"], *t["aliases"]]})
    schema = {
        "@context": "https://schema.org", "@type": "DefinedTermSet",
        "@id": BASE + "/lexique/#definitions", "name": "Lexique de la Grande Unicité et de la cosmodésie",
        "url": BASE + "/lexique/", "inLanguage": "fr", "description": data["description"],
        "hasDefinedTerm": [
            {"@type": "DefinedTerm", "@id": BASE + "/lexique/#" + t["id"],
             "name": t["name"], "alternateName": t["aliases"], "description": t["definition"],
             "inDefinedTermSet": BASE + "/lexique/#definitions"} for t in terms
        ],
    }
    nav = "".join(f'<a href="#{esc(g["id"])}">{esc(g["name"])}</a>' for g in data["groups"])
    sections = []
    for group in data["groups"]:
        cards = []
        for term in terms:
            if term["group"] != group["id"]:
                continue
            aliases = (f'<p class="aliases"><span>Autres formulations :</span> {esc(" · ".join(term["aliases"]))}</p>'
                       if term["aliases"] else "")
            searchable = " ".join([term["name"], *term["aliases"], term["definition"]])
            cards.append(f'''<article class="term" id="{esc(term['id'])}" data-group="{esc(term['group'])}" data-search="{esc(searchable)}">
<h3>{esc(term['name'])}</h3><p>{esc(term['definition'])}</p>{aliases}
<a class="source" href="{BASE}{esc(term['path'])}">Lire le contexte et les sources →</a></article>''')
        sections.append(f'<section class="group" id="{esc(group["id"])}"><h2>{esc(group["name"])}</h2><p class="intro">{esc(group["description"])}</p><div class="terms">'+"\n".join(cards)+"</div></section>")
    options = "".join(f'<option value="{esc(g["id"])}">{esc(g["name"])}</option>' for g in data["groups"])
    content = f'''<section class="hero"><p class="kicker">LES MOTS QUI RELIENT NOTRE TRAVAIL</p>
<h1>Une notion.<br><span>Son sens. Son chemin.</span></h1>
<p class="lead">Le lexique de la Grande Unicité, de la cosmodésie et du Fil Doré. Chaque entrée conserve ses formulations, donne une définition et ouvre une pièce du corpus.</p>
<p>{len(terms)} entrées · {len(all_names)} noms et formulations · {len(data['groups'])} familles</p>
<div class="search"><label for="query">Retrouver un mot ou une question</label><input id="query" type="search" placeholder="Con-science, AETD, mémoire, viabilité…" autocomplete="off">
<label for="family">Parcourir une famille</label><select id="family"><option value="">Toutes les familles</option>{options}</select></div>
<p id="count" class="muted" role="status" aria-live="polite">{len(terms)} entrées accessibles.</p>
<nav class="families" aria-label="Familles du lexique">{nav}</nav></section>
<div id="definitions">{''.join(sections)}</div><p id="empty" hidden>Aucune entrée ne correspond. Essayez un autre mot ou une autre famille.</p>
<section class="sources"><h2>Une carte avec une histoire</h2><p>Le vocabulaire est extrait des pages publiques et de la carte des projets Xavier/Judy relue le 10 octobre 2026, puis complétée par les quatre fiches de recherche du 14 publiées le 15 octobre et le dossier sur la vie du 16 octobre. Les formulations de Xavier gardent leur provenance ; les mathématiques antérieures gardent leurs auteurs. Les noms de projets indiquent leur place dans le programme, et les liens ouvrent les pièces actuellement publiques.</p>
<p><a href="{BASE}/seo/catalogue.json">Consulter le catalogue structuré</a> · <a href="{BASE}/projets/">Voir la carte des projets et des œuvres</a> · <a href="{BASE}/CONTRIBUTIONS_ORIGINALES.html">Lire les contributions</a></p></section>
<script>
const q=document.getElementById('query'),family=document.getElementById('family');
const terms=[...document.querySelectorAll('.term')],groups=[...document.querySelectorAll('.group')];
function normalize(s){{return s.normalize('NFD').replace(/[\\u0300-\\u036f]/g,'').toLowerCase();}}
function update(){{const words=normalize(q.value).trim().split(/\\s+/).filter(Boolean);let count=0;
for(const t of terms){{const visible=(!family.value||t.dataset.group===family.value)&&words.every(w=>normalize(t.dataset.search).includes(w));t.hidden=!visible;if(visible)count++;}}
for(const g of groups){{g.hidden=![...g.querySelectorAll('.term')].some(t=>!t.hidden);}}
document.getElementById('count').textContent=count+' entrée'+(count===1?'':'s')+' accessible'+(count===1?'':'s')+'.';document.getElementById('empty').hidden=count>0;}}
q.addEventListener('input',update);family.addEventListener('change',update);
q.value=new URLSearchParams(location.search).get('q')||'';update();
</script>'''
    lexicon = ROOT / "lexique/index.html"
    lexicon.parent.mkdir(exist_ok=True)
    lexicon.write_text(shell("Lexique : Grande Unicité, cosmodésie, con-science — Xavier Endres",
        "Définitions, variantes et sources du corpus Xavier Endres et Judy Velune : cosmodésie, anti-entropie, con-science, Fil Doré et projets.", "/lexique/", content, schema))
    print(json.dumps({"entries": len(terms), "names_and_aliases": len(all_names), "families": len(data["groups"]), "output": str(lexicon)}, ensure_ascii=False))


if __name__ == "__main__":
    main()

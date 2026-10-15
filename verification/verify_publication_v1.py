"""Validate publication identities, original source hashes and rendered navigation.

Run without arguments for the source registry; pass --site _site after Jekyll.
Checks are documentary contracts, not evidence of human comprehension.
"""
from pathlib import Path
from urllib.parse import urljoin, urlsplit, unquote
from html.parser import HTMLParser
import argparse
import hashlib
import json
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
BASE = '/grande-unicite-cosmodesie'


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attrs):
        data = dict(attrs)
        for attr in ('href', 'src'):
            if data.get(attr):
                self.links.append(data[attr])


def check_registry():
    registry = json.loads((ROOT/'travaux/registre-20261014.json').read_text())
    manifest = json.loads((ROOT/'verification/sources-20261014.json').read_text())
    entries = registry['results']
    assert len(entries) == 4
    assert len({row['id'] for row in entries}) == len(entries)
    for row in entries:
        for field in ('programme_author', 'source_date', 'publication_date',
                      'kind', 'hypotheses', 'reopen_when', 'source_manifest'):
            assert row[field], (row['id'], field)
        for path in row['verifiers'] + row['results'] + [row['source_manifest']]:
            assert (ROOT/path).is_file(), path
        assert (ROOT/(row['page'].lstrip('/')[:-5]+'.md')).is_file(), row['page']
    for row in manifest['files']:
        path = ROOT/row['path']
        assert hashlib.sha256(path.read_bytes()).hexdigest() == row['sha256'], row['path']
    return {'results': len(entries), 'source_hashes': len(manifest['files'])}


def check_rendered(site):
    sitemap = ET.parse(site/'sitemap.xml')
    urls = [node.text for node in sitemap.findall('.//{*}loc')]
    assert not any('google964e013960c982a8' in url for url in urls)
    assert (site/'google964e013960c982a8.html').is_file()
    assert (site/'google964e013960c982a8.html').read_bytes() == (ROOT/'google964e013960c982a8.html').read_bytes()
    checked = 0
    for source in site.rglob('*.html'):
        parser = Links()
        parser.feed(source.read_text(encoding='utf-8'))
        page_url = BASE + '/' + source.relative_to(site).as_posix()
        if page_url.endswith('/index.html'):
            page_url = page_url[:-10]
        for href in parser.links:
            target = urlsplit(urljoin('https://jakepourjudy.github.io'+page_url, href))
            if target.netloc != 'jakepourjudy.github.io':
                continue
            if not target.path.startswith(BASE+'/'):
                continue
            path = unquote(target.path[len(BASE)+1:])
            local = site/path
            if target.path.endswith('/'):
                local = local/'index.html'
            assert local.is_file(), (str(source.relative_to(site)), href)
            checked += 1
    for row in json.loads((ROOT/'travaux/registre-20261014.json').read_text())['results']:
        assert (site/row['page'].lstrip('/')).is_file(), row['page']
    return {'rendered_local_links': checked, 'sitemap_urls': len(urls),
            'verification_file_served_and_excluded_from_sitemap': True}


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--site', type=Path)
    args = parser.parse_args()
    result = check_registry()
    if args.site:
        result.update(check_rendered(args.site))
    print(json.dumps(result, ensure_ascii=False, indent=2))

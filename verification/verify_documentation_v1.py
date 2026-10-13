"""Check repository links, Jekyll destinations and MFC catalogue/proof coverage.

No network and no third-party dependencies. Resolves front-matter permalinks,
generated .html destinations and directory index pages. Checks local existence,
not remote server status. Xavier Endres / Judy Velune, 2026-10-13.
"""
from pathlib import Path
from urllib.parse import unquote, urlsplit
import json
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
BASE = "/grande-unicite-cosmodesie"


def front_matter(text):
    if not text.startswith("---\n"):
        return ""
    return text.split("---\n", 2)[1]


def destinations(files):
    targets = {}
    for path in files:
        relative = path.relative_to(ROOT).as_posix()
        targets[relative] = path
        if path.suffix == ".scss" and path.read_text(encoding="utf-8").startswith("---\n"):
            targets[relative[:-5] + ".css"] = path
        if path.suffix == ".html":
            if path.name == "index.html":
                targets[str(path.relative_to(ROOT).parent).replace(".", "").strip("/")+"/"] = path
            continue
        if path.suffix != ".md" or path.name == "README.md" and path.parent == ROOT:
            continue
        fm = front_matter(path.read_text(encoding="utf-8"))
        if not fm:
            continue
        match = re.search(r"^permalink:\s*[\"']?([^\n\"']+)", fm, re.M)
        target = match.group(1).strip().lstrip("/") if match else relative[:-3]+".html"
        targets[target] = path
        if path.stem == "index" and not match:
            targets[path.relative_to(ROOT).parent.as_posix().strip(".")+"/"] = path
    return targets


def extract_links(text, suffix):
    # Code examples may contain placeholders, not navigation.
    clean = re.sub(r"```.*?```", "", text, flags=re.S)
    clean = re.sub(r"\{\{\s*['\"]([^'\"]+)['\"]\s*\|\s*relative_url\s*\}\}",
                   lambda match: BASE+"/"+match.group(1).lstrip("/"), clean)
    links = re.findall(r"\]\(([^\s)]+)(?:\s+[^)]*)?\)", clean)
    links += re.findall(r"(?:href|src)=[\"']([^\"']+)[\"']", clean)
    return links


def normalize(source, value):
    parsed = urlsplit(value)
    if parsed.scheme or parsed.netloc or not parsed.path:
        return None
    target = unquote(parsed.path)
    if target.startswith(BASE+"/"):
        target = target[len(BASE)+1:]
    elif target.startswith("/"):
        target = target[1:]
    else:
        target = (source.relative_to(ROOT).parent / target).as_posix()
    parts = []
    for part in target.split("/"):
        if part in ("", "."):
            continue
        if part == "..":
            if not parts:
                return "__OUTSIDE_REPOSITORY__"
            parts.pop()
        else:
            parts.append(part)
    normalized = "/".join(parts)
    return normalized+"/" if parsed.path.endswith("/") or parsed.path in (".", "..") else normalized


def main():
    files = [p for p in ROOT.rglob("*") if p.is_file() and
             ".git" not in p.relative_to(ROOT).parts and
             "__pycache__" not in p.relative_to(ROOT).parts]
    targets = destinations(files)
    errors, checked = [], 0
    for source in files:
        if source.suffix not in (".md", ".html"):
            continue
        for value in extract_links(source.read_text(encoding="utf-8"), source.suffix):
            target = normalize(source, value)
            if target is None:
                continue
            checked += 1
            if target not in targets:
                errors.append({"source": source.relative_to(ROOT).as_posix(), "target": value})

    atlas = (ROOT/"research/mecanismes-non-necessaires.md").read_text(encoding="utf-8")
    catalogue = re.findall(r"\| (M\d{2}) ·", atlas)
    if catalogue != [f"M{n:02d}" for n in range(1, 33)]:
        errors.append({"catalogue": "Expected exactly M01--M32 in order"})
    proofs = (ROOT/"theoremes/11-necessite-fonctionnelle.md").read_text(encoding="utf-8")
    proof_ids = re.findall(r"^## (N\d+) —", proofs, re.M)
    if proof_ids != [f"N{n}" for n in range(14)]:
        errors.append({"proofs": "Expected exactly N0--N13 in order"})
    result = {"local_links_checked": checked, "catalogue_entries": len(catalogue),
              "mathematical_results": len(proof_ids), "errors": errors}
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())

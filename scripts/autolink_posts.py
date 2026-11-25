import html
import re
from pathlib import Path

import yaml

SCRIPT_DIR = Path(__file__).resolve().parent
POSTS_DIR = SCRIPT_DIR.parent / "docs/_posts"
LINKS_FILE = SCRIPT_DIR / "keywords.yml"
PROTECTED = re.compile(
    r"(^[ \t]*(`{3,}|~{3,})[^\n]*\n.*?^[ \t]*\2[ \t]*$"
    r"|`+[^`]*`+"
    r"|!?\[[^\]\n]*\]\([^\n)]*\)"
    r"|!?\[[^\]\n]*\]\[[^\]\n]*\]"
    r"|^\[[^\]\n]+\]:[^\n]*"
    r"|<a\b[^>]*>.*?</a>"
    r"|<!--.*?-->|<[^>]+>"
    r"|{{.*?}}|{%.*?%}"
    r"|^#{1,6}[ \t]+[^\n]*)",
    re.MULTILINE | re.DOTALL | re.IGNORECASE,
)


def load_links(yaml_file):
    links = yaml.safe_load(Path(yaml_file).read_text(encoding="utf-8"))
    return {entry["key"]: entry["url"] for entry in links}


def autolink_content(content, keywords, skip_key):
    frontmatter = re.match(r"\A---\r?\n.*?\r?\n---(?:\r?\n|$)", content, re.DOTALL)
    prefix = frontmatter.group() if frontmatter else ""
    body = content[len(prefix):]
    skip_keys = {skip_key} if isinstance(skip_key, str) else set(skip_key or [])
    keys = sorted((key for key in keywords if key not in skip_keys), key=len, reverse=True)
    if not keys:
        return content
    pattern = re.compile(r"(?<![\w/])(?:" + "|".join(map(re.escape, keys)) + r")(?!\w)")
    in_table = False

    def link_text(text):
        def replace(match):
            key = match.group()
            url = keywords[key]
            if in_table:
                return f'<a href="{html.escape(url, quote=True)}">{html.escape(key)}</a>'
            return f"[{key}]({url})"
        return pattern.sub(replace, text)

    result = []
    offset = 0
    for match in PROTECTED.finditer(body):
        result.append(link_text(body[offset:match.start()]))
        protected = match.group()
        if re.match(r"<table\b", protected, re.IGNORECASE):
            in_table = True
        elif re.match(r"</table\b", protected, re.IGNORECASE):
            in_table = False
        result.append(correct_post_links(protected, keywords))
        offset = match.end()
    result.append(link_text(body[offset:]))
    return prefix + "".join(result)


def correct_post_links(protected, keywords):
    if not re.match(r"(\[|<a\b|#)", protected):
        return protected
    urls_by_slug = {url.rsplit("/", 1)[-1].removesuffix(".html"): url for url in keywords.values()}
    pattern = re.compile(r"""(href=["']|\]\()(/(?:fish|tank|food)/\d{4}/\d{2}/\d{2}/([^"'()#\s]+))""")

    def replace(match):
        canonical = urls_by_slug.get(match[3].removesuffix(".html"))
        return match[0] if canonical is None else match[1] + canonical
    return pattern.sub(replace, protected)


def main():
    keywords = load_links(LINKS_FILE)
    for path in sorted(POSTS_DIR.glob("*.md")):
        slug = path.name[11:-3]
        own_keys = {key for key, url in keywords.items() if url.rsplit("/", 1)[-1] == slug}
        original = path.read_text(encoding="utf-8")
        updated = autolink_content(original, keywords, own_keys)
        if original != updated:
            path.write_text(updated, encoding="utf-8")
            print(f"Verlinkungen aktualisiert: {path.name}")


if __name__ == "__main__":
    main()

import os
import re
import yaml

POSTS_DIR = '../_posts'  # Dein Pfad zu Markdown-Dateien
LINKS_FILE = 'keywords.yml'  # Deine YAML-Liste mit key/url

def load_links(yaml_file):
    """
    Liefert:
    - keywords_dict: key -> url
    - url2key: url -> key
    """
    with open(yaml_file, 'r', encoding='utf-8') as f:
        links = yaml.safe_load(f)
    keywords_dict = {entry['key']: entry['url'] for entry in links}
    url2key = {entry['url']: entry['key'] for entry in links}
    return keywords_dict, url2key

def target_url_for_file(md_filename):
    """
    Rückgabe: Webpfad für diesen Post im Jekyll-Format /fish/2025/09/30/fish_bandit
    Jekyll erstellt URLs ohne trailing slash
    """
    base = os.path.basename(md_filename)
    # z.B. 2025-09-29-fish_bandit.md
    m = re.match(r'(\d{4})-(\d{2})-(\d{2})-([^\.]+)\.md$', base)
    if not m:
        raise ValueError(f"Ungültiges Dateiformat: {md_filename}")
    year, month, day, slug = m.groups()
    # Ordner-Struktur und Präfix individuell anpassbar!
    # Du hast: /fish/yyyy/mm/dd/fish_bandit oder /tank/yyyy/mm/dd/tank_babys usw.
    # Dafür bestimmen wir aus dem Slug den Unterordner ("fish", "tank" etc.)
    if "_" in slug:
        folder = slug.split("_")[0]
    else:
        folder = slug
    url = f"/{folder}/{year}/{month}/{day}/{slug}"
    return url

def get_own_key_for_file(md_filename, url2key):
    """Gibt den eigenen Key für diese Datei zurück, wenn sie in url2key enthalten ist, sonst None."""
    own_url = target_url_for_file(md_filename)
    return url2key.get(own_url)

def autolink_content(content, keywords_dict, skip_key):
    # Front Matter abtrennen
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            front_matter = parts[0] + '---' + parts[1] + '---\n'
            body = parts[2]
        else:
            front_matter = ''
            body = content
    else:
        front_matter = ''
        body = content

    lines = body.splitlines(keepends=True)
    new_lines = []
    for line in lines:
        if line.lstrip().startswith('#'):  # Überschrift überspringen
            new_lines.append(line)
            continue
        modified_line = line
        # 1. Bestehende Links auf Keywords prüfen und ggf. korrigieren
        for key, url in sorted(keywords_dict.items(), key=lambda x: -len(x[0])):
            if key == skip_key:
                continue
            # Finde alle [key](irgendeine_url) und prüfe die URL
            link_pattern = re.compile(r'\[' + re.escape(key) + r'\]\(([^)]+)\)')
            def link_replacer(match):
                current_url = match.group(1)
                if current_url != url:
                    return f'[{key}]({url})'  # Korrigiere die URL
                else:
                    return match.group(0)  # Link ist korrekt
            modified_line = link_pattern.sub(link_replacer, modified_line)
        # 2. Begriffe längster zuerst: keine Überschneidung, nur noch nicht verlinkte Begriffe
        for key, url in sorted(keywords_dict.items(), key=lambda x: -len(x[0])):
            if key == skip_key:
                continue
            # Exakter Match, Case-sensitive, nur Ganzwort, nicht bereits verlinkt
            pattern = r'(?<!\[)' + re.escape(key) + r'(?!\w)(?!\]\([^)]+\))'
            def replacer(match):
                start = match.start()
                pre = modified_line[max(0, start-50):start]
                if '](' in pre[-10:] or '<a ' in pre[-10:]:
                    return match.group(0)
                return f'[{key}]({url})'
            modified_line = re.sub(pattern, replacer, modified_line)
        new_lines.append(modified_line)
    return front_matter + ''.join(new_lines)

def main():
    keywords_dict, url2key = load_links(LINKS_FILE)
    for filename in os.listdir(POSTS_DIR):
        if not filename.endswith('.md'):
            continue
        path = os.path.join(POSTS_DIR, filename)
        own_key = get_own_key_for_file(filename, url2key)
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        new_content = autolink_content(content, keywords_dict, own_key)
        if new_content != content:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f'Verlinkte Begriffe in: {filename}')
        else:
            print(f'Keine Änderung in: {filename}')

if __name__ == '__main__':
    main()

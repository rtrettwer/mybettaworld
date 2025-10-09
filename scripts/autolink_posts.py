import os
import re
import yaml

POSTS_DIR = '../docs/_posts'      # Passe ggf. an deinen Pfad an
LINKS_FILE = 'keywords.yml'       # YAML mit key/url-paaren

def load_links(yaml_file):
    with open(yaml_file, 'r', encoding='utf-8') as f:
        links = yaml.safe_load(f)
    return {entry['key']: entry['url'] for entry in links}

def get_target_key(filename, links):
    basename = os.path.basename(filename)
    for key, url in links.items():
        base_key = url.rsplit('/', 1)[-1].replace('.html', '.md').replace('.htm', '.md')
        if basename == base_key:
            return key
    return None

def autolink_content(content, links, skip_key):
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
        if line.lstrip().startswith('#'):
            new_lines.append(line)
            continue  # Skip Überschriften
        modified_line = line
        for key, url in sorted(links.items(), key=lambda x: -len(x[0])):
            if key == skip_key:
                continue
            pattern = r'(?<!\[)(?<!\w)' + re.escape(key) + r'(?!\w)(?!\]\([^)]+\))'
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
    links = load_links(LINKS_FILE)
    for filename in os.listdir(POSTS_DIR):
        if not filename.endswith('.md'):
            continue
        path = os.path.join(POSTS_DIR, filename)
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        skip_key = get_target_key(filename, links)
        new_content = autolink_content(content, links, skip_key)
        if new_content != content:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f'Verlinkte Begriffe in: {filename}')
        else:
            print(f'Keine Änderung in: {filename}')

if __name__ == '__main__':
    main()

import os
import yaml
from collections import OrderedDict

GALLERY_YML = os.path.join(os.path.dirname(__file__), '../docs/_data/gallery.yml')
FISH_DIR = os.path.join(os.path.dirname(__file__), '../docs/assets/images/fish')

# Hilfsfunktion: YAML mit korrekter Reihenfolge laden

def ordered_load(stream, Loader=yaml.SafeLoader, object_pairs_hook=OrderedDict):
    class OrderedLoader(Loader):
        pass
    def construct_mapping(loader, node):
        loader.flatten_mapping(node)
        return object_pairs_hook(loader.construct_pairs(node))
    OrderedLoader.add_constructor(
        yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
        construct_mapping)
    return yaml.load(stream, OrderedLoader)

def ordered_dump(data, stream=None, Dumper=yaml.SafeDumper, **kwds):
    class OrderedDumper(Dumper):
        pass
    def _dict_representer(dumper, data):
        return dumper.represent_dict(data.items())
    OrderedDumper.add_representer(OrderedDict, _dict_representer)
    return yaml.dump(data, stream, OrderedDumper, **kwds)

def file_exists(rel_path):
    abs_path = os.path.join(os.path.dirname(__file__), '../docs', rel_path.lstrip('/'))
    return os.path.isfile(abs_path)

def get_all_fish_images():
    fish_images = set()
    for root, dirs, files in os.walk(FISH_DIR):
        for f in files:
            if f.endswith('.webp') and '_thumbnail' not in f:
                rel = os.path.relpath(os.path.join(root, f), os.path.join(os.path.dirname(__file__), '../docs'))
                fish_images.add('/' + rel.replace(os.sep, '/'))
    return fish_images

def main():
    # 1. gallery.yml einlesen
    with open(GALLERY_YML, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    # 2. YAML-Abschnitte extrahieren (mit Kommentaren)
    new_lines = []
    used_paths = set()
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.strip().startswith('- path: '):
            path = line.strip().split(': ', 1)[1]
            if file_exists(path):
                new_lines.append(line)
                used_paths.add(path)
                # Nächste 2 Zeilen (title/caption) übernehmen
                new_lines.append(lines[i+1])
                new_lines.append(lines[i+2])
                i += 3
            else:
                # Überspringe diesen Eintrag (existiert nicht mehr)
                i += 3
        else:
            new_lines.append(line)
            i += 1
    # 3. Alle großen fish-Bilder, die noch nicht gelistet sind, ergänzen
    fish_images = get_all_fish_images()
    missing = sorted(fish_images - used_paths)
    if missing:
        # Füge am Ende einen Block hinzu
        new_lines.append('\n# Automatisch hinzugefügte neue Fisch-Bilder am {}\n'.format(__import__('datetime').date.today()))
        for path in missing:
            new_lines.append(f"- path: {path}\n")
            new_lines.append(f"  title: {path}\n")
            new_lines.append("  caption: (Platzhalter)\n")
    # 4. Schreibe zurück
    with open(GALLERY_YML, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    print(f"gallery.yml wurde bereinigt und ergänzt. {len(missing)} neue Bilder hinzugefügt.")

if __name__ == '__main__':
    main()

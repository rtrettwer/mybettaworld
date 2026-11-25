from pathlib import Path

import yaml

DOCS_DIR = Path(__file__).resolve().parents[1] / "docs"
GALLERY_YML = DOCS_DIR / "_data/gallery.yml"


def main():
    original = GALLERY_YML.read_text(encoding="utf-8")
    entries = yaml.safe_load(original)
    if not isinstance(entries, list):
        raise ValueError("gallery.yml muss eine Liste von Bild-Metadaten enthalten.")
    retained = [entry for entry in entries if (DOCS_DIR / entry["path"].lstrip("/")).is_file()]
    used_paths = {entry["path"] for entry in retained}
    new_images = sorted(
        path for path in (DOCS_DIR / "assets/images/fish").rglob("*.webp")
        if "_thumbnail" not in path.stem and "_timeline" not in path.stem
    )
    for path in new_images:
        relative_path = "/" + path.relative_to(DOCS_DIR).as_posix()
        if relative_path not in used_paths:
            retained.append({"path": relative_path, "title": path.parent.name, "caption": ""})
            used_paths.add(relative_path)
    if entries == retained:
        print("Galerie-Metadaten sind aktuell.")
        return
    updated = "# Galerie-Metadaten; individuelle Titel und Bildbeschreibungen bleiben erhalten.\n"
    updated += yaml.safe_dump(retained, allow_unicode=True, sort_keys=False, width=120)
    GALLERY_YML.write_text(updated, encoding="utf-8")
    print(f"Galerie-Metadaten aktualisiert: {len(retained)} Bilder.")


if __name__ == "__main__":
    main()

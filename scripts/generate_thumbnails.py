import os
import sys
from pathlib import Path
from PIL import Image
from concurrent.futures import ThreadPoolExecutor, as_completed
import multiprocessing

# Konfiguration
IMAGE_ROOT = Path('../docs/assets/images')
THUMBNAIL_SUFFIX = '_thumbnail.webp'
WEBP_QUALITY = 85
THUMBNAIL_QUALITY = 70
THUMBNAIL_SIZE = (400, 400)
SOURCE_EXTS = {'.jpg', '.jpeg', '.png'}
MAX_WORKERS = min(4, multiprocessing.cpu_count())  # Limit für I/O-bound tasks


def is_source_image(filename):
    """Prüft ob es sich um ein Quellbild handelt."""
    ext = Path(filename).suffix.lower()
    return ext in SOURCE_EXTS and not filename.lower().endswith(THUMBNAIL_SUFFIX)


def is_webp(filename):
    """Prüft ob es sich um eine WebP-Datei handelt (kein Thumbnail, kein Timeline, kein _timeline.webp)."""
    return (
        filename.lower().endswith('.webp')
        and not filename.lower().endswith(THUMBNAIL_SUFFIX)
        and '_timeline' not in filename.lower()
    )


def webp_path(image_path):
    """Gibt den WebP-Pfad für ein Quellbild zurück."""
    return image_path.with_suffix('.webp')


def thumbnail_path(webp_path):
    """Gibt den Thumbnail-Pfad für eine WebP-Datei zurück (Suffix _thumbnail vor .webp)."""
    p = Path(webp_path)
    if p.name.endswith(THUMBNAIL_SUFFIX):
        return p  # Falls schon Thumbnail
    return p.with_name(p.stem + THUMBNAIL_SUFFIX)


def create_webp(image_path, webp_path):
    """Erstellt WebP aus Quellbild und löscht Original."""
    try:
        with Image.open(image_path) as img:
            # Optimiere für Web: RGB-Modus für kleinere Dateien
            if img.mode in ('RGBA', 'P'):
                img = img.convert('RGB')

            img.save(webp_path, 'WEBP', quality=WEBP_QUALITY, method=6)
            print(f"✓ WebP erstellt: {webp_path.name}")

        # Original nur bei erfolgreicher Konvertierung löschen
        image_path.unlink()
        print(f"✓ Original gelöscht: {image_path.name}")
        return True
    except Exception as e:
        print(f"✗ Fehler bei {image_path.name} (WebP): {e}")
        return False


def create_thumbnail(webp_path, thumb_path):
    """Erstellt Thumbnail aus WebP-Datei."""
    try:
        with Image.open(webp_path) as img:
            # Thumbnail mit besserer Qualität
            img.thumbnail(THUMBNAIL_SIZE, Image.Resampling.LANCZOS)
            img.save(thumb_path, 'WEBP', quality=THUMBNAIL_QUALITY, method=6)
            print(f"✓ Thumbnail erstellt: {thumb_path.name}")
        return True
    except Exception as e:
        print(f"✗ Fehler bei {webp_path.name} (Thumbnail): {e}")
        return False


def process_source_image(file_path):
    """Verarbeitet ein Quellbild (JPG/PNG) zu WebP + Thumbnail."""
    webp_out = webp_path(file_path)

    # Skip wenn WebP bereits existiert
    if webp_out.exists():
        print(f"→ WebP existiert bereits: {webp_out.name}")
    else:
        success = create_webp(file_path, webp_out)
        if not success:
            return False

    # Thumbnail erstellen
    thumb_out = thumbnail_path(webp_out)
    if thumb_out.exists():
        print(f"→ Thumbnail existiert bereits: {thumb_out.name}")
    else:
        return create_thumbnail(webp_out, thumb_out)

    return True


def process_webp_image(file_path):
    """Verarbeitet eine WebP-Datei zu Thumbnail."""
    thumb_out = thumbnail_path(file_path)
    if thumb_out.exists():
        print(f"→ Thumbnail existiert bereits: {thumb_out.name}")
        return True
    else:
        print(f"→ Erzeuge Thumbnail für: {file_path.name}")
        return create_thumbnail(file_path, thumb_out)


def main():
    """Hauptfunktion mit paralleler Verarbeitung."""
    if not IMAGE_ROOT.exists():
        print(f"✗ Bildverzeichnis nicht gefunden: {IMAGE_ROOT}")
        sys.exit(1)

    # Sammle alle zu verarbeitenden Dateien
    tasks = []

    for file_path in IMAGE_ROOT.rglob('*'):
        if not file_path.is_file():
            continue

        filename = file_path.name

        if is_source_image(filename):
            print(f"[DEBUG] Quellbild erkannt: {filename}")
            tasks.append(('source', file_path))
        elif is_webp(filename):
            print(f"[DEBUG] WebP erkannt (Thumbnail-Kandidat): {filename}")
            tasks.append(('webp', file_path))
        else:
            print(f"[DEBUG] Übersprungen: {filename}")

    if not tasks:
        print("→ Keine Bilder zur Verarbeitung gefunden.")
        return

    print(f"→ Verarbeite {len(tasks)} Dateien mit {MAX_WORKERS} Threads...")

    # Parallel verarbeiten
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        future_to_task = {}

        for task_type, file_path in tasks:
            if task_type == 'source':
                future = executor.submit(process_source_image, file_path)
            else:  # webp
                future = executor.submit(process_webp_image, file_path)

            future_to_task[future] = (task_type, file_path)

        # Ergebnisse sammeln
        success_count = 0
        for future in as_completed(future_to_task):
            task_type, file_path = future_to_task[future]
            try:
                if future.result():
                    success_count += 1
            except Exception as e:
                print(f"✗ Fehler bei {file_path.name}: {e}")

    print(f"✓ Verarbeitung abgeschlossen: {success_count}/{len(tasks)} erfolgreich")


if __name__ == '__main__':
    main()

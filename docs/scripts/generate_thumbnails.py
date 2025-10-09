import os
from PIL import Image

# Konfiguration
IMAGE_ROOT = ('../assets/images')
THUMBNAIL_SUFFIX = '_thumbnail.webp'
WEBP_QUALITY = 85
THUMBNAIL_QUALITY = 70
THUMBNAIL_SIZE = (400, 400)  # Maximalgröße für Thumbnails
SOURCE_EXTS = {'.jpg', '.jpeg', '.png'}


def is_source_image(filename):
    ext = os.path.splitext(filename)[1].lower()
    return ext in SOURCE_EXTS and not filename.lower().endswith(THUMBNAIL_SUFFIX)

def is_webp(filename):
    return filename.lower().endswith('.webp') and not filename.endswith(THUMBNAIL_SUFFIX)

def webp_path(image_path):
    base, _ = os.path.splitext(image_path)
    return base + '.webp'

def thumbnail_path(webp_path):
    base, _ = os.path.splitext(webp_path)
    return base + THUMBNAIL_SUFFIX

def create_webp(image_path, webp_path):
    try:
        with Image.open(image_path) as img:
            img.save(webp_path, 'WEBP', quality=WEBP_QUALITY)
            print(f"WebP erstellt: {webp_path}")
        # Nach erfolgreicher Konvertierung das Original löschen
        os.remove(image_path)
        print(f"Original gelöscht: {image_path}")
        return True
    except Exception as e:
        print(f"Fehler bei {image_path} (WebP): {e}")
        return False

def create_thumbnail(webp_path, thumb_path):
    try:
        with Image.open(webp_path) as img:
            img.thumbnail(THUMBNAIL_SIZE)
            img.save(thumb_path, 'WEBP', quality=THUMBNAIL_QUALITY)
            print(f"Thumbnail erstellt: {thumb_path}")
    except Exception as e:
        print(f"Fehler bei {webp_path} (Thumbnail): {e}")

def main():
    for root, dirs, files in os.walk(IMAGE_ROOT):
        for filename in files:
            file_path = os.path.join(root, filename)
            # 1. Quellbild (jpg, png) → webp erzeugen und Original löschen
            if is_source_image(filename):
                webp_out = webp_path(file_path)
                if not os.path.exists(webp_out):
                    success = create_webp(file_path, webp_out)
                    if not success:
                        continue
                else:
                    print(f"WebP existiert bereits: {webp_out}")
                # Thumbnail erzeugen
                thumb_out = thumbnail_path(webp_out)
                if not os.path.exists(thumb_out):
                    create_thumbnail(webp_out, thumb_out)
                else:
                    print(f"Thumbnail existiert bereits: {thumb_out}")
            # 2. WebP (kein Thumbnail) → Thumbnail erzeugen
            elif is_webp(filename):
                thumb_out = thumbnail_path(file_path)
                if not os.path.exists(thumb_out):
                    create_thumbnail(file_path, thumb_out)
                else:
                    print(f"Thumbnail existiert bereits: {thumb_out}")
            # 3. Thumbnails und andere Dateien ignorieren
            else:
                pass

if __name__ == '__main__':
    main()

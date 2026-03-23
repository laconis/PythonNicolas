import os

def list_recursive(path):
    for root, dirs, files in os.walk(path):
        print(f"Dossier : {root}")
        for f in files:
            print(f"  - {f}")

def list_dirs_recursive(path):
    for root, dirs, files in os.walk(path):
        for d in dirs:
            print(os.path.join(root, d))

def delete_empty_dirs(path):
    for root, dirs, files in os.walk(path, topdown=False):
        for d in dirs:
            full_path = os.path.join(root, d)
            if not os.listdir(full_path):  # dossier vide
                print("Suppression :", full_path)
                os.rmdir(full_path)


def delete_empty_dirs_recursive(path):
    removed = True
    while removed:
        removed = False
        for root, dirs, files in os.walk(path, topdown=False):
            for d in dirs:
                full_path = os.path.join(root, d)
                if not os.listdir(full_path):
                    print("Suppression :", full_path)
                    os.rmdir(full_path)
                    removed = True


# liste les dossiers sans les supprimer
def list_empty_dirs(path):
    empty = []
    for root, dirs, files in os.walk(path, topdown=False):
        for d in dirs:
            full_path = os.path.join(root, d)
            if not os.listdir(full_path):
                empty.append(full_path)
    return empty

# Exemple
#for d in list_empty_dirs("/chemin/vers/ton/dossier"):
 #   print("Dossier vide :", d)


def folder_size(path: Path) -> int:
    return sum(f.stat().st_size for f in path.rglob("*") if f.is_file())

def format_size(size):
    for unit in ["B", "KB", "MB", "GB", "TB"]:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024
      
def folder_size(path):
    total = 0
    for root, dirs, files in os.walk(path):
        for f in files:
            try:
                total += os.path.getsize(os.path.join(root, f))
            except OSError:
                pass
    return total
  

def top_folders(path, n=10):
    sizes = []
    with os.scandir(path) as entries:
        for entry in entries:
            if entry.is_dir():
                size = folder_size(entry.path)
                sizes.append((entry.name, size))
    sizes.sort(key=lambda x: x[1], reverse=True)
    return sizes[:n]

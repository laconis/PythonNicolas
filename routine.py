
#!/usr/bin/env python3
import os
import time
import argparse

try:
    import send2trash
    USE_TRASH = True
except ImportError:
    USE_TRASH = False


def supprimer_fichiers_extension(racine, extensions, dry=False, trash=False):
    for dossier, _, fichiers in os.walk(racine):
        for f in fichiers:
            if any(f.endswith(ext) for ext in extensions):
                chemin = os.path.join(dossier, f)
                if dry:
                    print("[SIMULATION] →", chemin)
                else:
                    if trash and USE_TRASH:
                        send2trash.send2trash(chemin)
                    else:
                        os.remove(chemin)
                    print("Supprimé :", chemin)


def supprimer_fichiers_vides(racine, dry=False, trash=False):
    for dossier, _, fichiers in os.walk(racine):
        for f in fichiers:
            chemin = os.path.join(dossier, f)
            if os.path.getsize(chemin) == 0:
                if dry:
                    print("[SIMULATION] →", chemin)
                else:
                    if trash and USE_TRASH:
                        send2trash.send2trash(chemin)
                    else:
                        os.remove(chemin)
                    print("Supprimé (vide) :", chemin)


def supprimer_vieux_fichiers(racine, jours, dry=False, trash=False):
    limite = time.time() - jours * 86400
    for dossier, _, fichiers in os.walk(racine):
        for f in fichiers:
            chemin = os.path.join(dossier, f)
            if os.path.getmtime(chemin) < limite:
                if dry:
                    print("[SIMULATION] →", chemin)
                else:
                    if trash and USE_TRASH:
                        send2trash.send2trash(chemin)
                    else:
                        os.remove(chemin)
                    print(f"Supprimé (>{jours} jours) :", chemin)


def supprimer_dossiers_vides(racine, dry=False):
    for dossier, sous, fichiers in os.walk(racine, topdown=False):
        if not sous and not fichiers:
            if dry:
                print("[SIMULATION dossier vide] →", dossier)
            else:
                os.rmdir(dossier)
                print("Dossier supprimé :", dossier)


def main():
    parser = argparse.ArgumentParser(description="Nettoyeur de fichiers/dossiers.")
    parser.add_argument("racine", help="Dossier à nettoyer")
    parser.add_argument("-e", "--ext", nargs="*", help="Extensions à supprimer (.log .tmp ...)")
    parser.add_argument("-v", "--vides", action="store_true", help="Supprimer fichiers vides")
    parser.add_argument("-j", "--jours", type=int, help="Supprimer fichiers plus vieux que X jours")
    parser.add_argument("-d", "--dry", action="store_true", help="Mode simulation (ne supprime rien)")
    parser.add_argument("-t", "--trash", action="store_true", help="Envoyer à la corbeille (si dispo)")
    parser.add_argument("-c", "--clean-dirs", action="store_true", help="Supprimer dossiers vides")

    args = parser.parse_args()

    if args.ext:
        supprimer_fichiers_extension(args.racine, args.ext, args.dry, args.trash)

    if args.vides:
        supprimer_fichiers_vides(args.racine, args.dry, args.trash)

    if args.jours:
        supprimer_vieux_fichiers(args.racine, args.jours, args.dry, args.trash)

    if args.clean_dirs:
        supprimer_dossiers_vides(args.racine, args.dry)


if __name__ == "__main__":
    main()

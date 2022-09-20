# Lire et écrire dans les fichiers textes

import os

def main():
    # chemin du fichier
    chemin = os.path.dirname(__file__)

    # Ouvrir un fichier pour ecriture and le créer si cela n'existe pas
    f = open(chemin + "/textfile.txt", "w")

    # Ouvrir un fichier pour ajouter du contenu à la fin
    # f = open(chemin + "/textfile.txt", "a")

    # Ecrire quelques lignes des données dans le fichier
    for i in range(10):
        f.write(f"Ligne {i + 1}\n")

    # Fermer le fichier à la fin des opérations
    f.close()

    # Ouvrir le fichier en mode lecture avec with
    with open(chemin + "/textfile.txt", "r") as f:
        # tester que le fichier est bien ouvert en mode lecture
        if f.mode == 'r': 
            # Lire le contenu du fichier
            contenu1 = f.read()
            print(contenu1)
            f.seek(0)
            contenu2 = f.read()
            print(contenu2)
            f.seek(0)

            # lire qu'une ligne par appel
            f1 = f.readline()
            print(f1)
            f1 = f.readline()
            print(f1)

            # lire les lignes individuellement dans une liste
            fl = f.readlines()
            
            for x in fl:
                print(x.replace("\n", ""))

if __name__ == "__main__":
    main()
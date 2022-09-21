# TP 3
# Mini Systeme BD 
# Creer un dictionnaire permettant d'enregistrer nom, age et taille d'utilisateurs dans un dictionnaire
# creer une fonction inscription pour saisir les données utilisateurs
# et poser la question si on veut continuer a saisir un utilisateur
# Creer une fonction consultation qui permet de voir les données utilisateurs enregistrées dans le dictionnaire.
# Creer un menu pour choisir entre quitter, inscription ou consultation

# Dans un deuxieme temps enregistrer les infos dans un fichier nommé utilisateurs.txt
# et lisez le fichier lors des consultations.
# On utilisera le caractère séparateur @ pour séparer la clé de la valeur d'un dictionnaire
# et le caractère # pour séparer les données constituant cette valeur.
# Exemple Juliette@18#1.68

# Dans un troisième temps améliorer le script en créant le menu suivant à l'aide d'un dictionnaire
# qui servira aussi à appeler les fonctions correspondantes.
# (L) Lecture
# (I) Inscription 
# (C) Consultation par nom
# (T) Consultation totale
# (E) Enregistrement
# (Q) Quitter

import os
fichier = "/utilisateurs.txt"
chemin = os.path.dirname(__file__)
dico = {}

def inscription():
    reponse = ""
    while reponse.upper() != "NON":
        age = 0
        taille = 0
        nom = input("Saisir le nom de l'utilisateur : ")
        
        while age == 0:
            try:
                age = int(input("Saisissez l'age de l'utilisateur : "))
            except Exception as e:
                print("Saisissez un nombre entier pour l'age.")
                age = 0

        while taille == 0:
            try:
                taille = float(input("Saisissez la taille de l'utilisateur : "))
            except Exception as e:
                print("Saisissez un nombre pour la taille.")
                taille = 0

        reponse = input("Continuer à saisir un utilisateur (oui/non) ? ")
        dico[nom] = (age, taille)

def consultation():
    nom = input("Quel nom d'utilisateur ? ")
    
    if nom in dico:
        print(f"Nom : {nom:20} - Age : {dico[nom][0]:<3} - Taille : {dico[nom][1]:2.2f}")
    else:
        print("L'utilisateur n'existe pas.")

def consultationTotale():
    for nom in dico:
        print(f"Nom : {nom:20} - Age : {dico[nom][0]:<3} - Taille : {dico[nom][1]:2.2f}")

def ligne():
        print("_" * 50)

def enregistrement():
    with open(chemin + fichier, "wt") as f:
        for nom in dico:
            f.write(f"{nom}@{dico[nom][0]}#{dico[nom][1]}\n")

    print("Ecriture du dictonnaire dans le fichier effectuée.")

def lecture():
    try:
        with open(chemin + fichier, "rt") as f:
            while True:
                ligneInfos = f.readline()

                if ligneInfos == "": break
                
                utilisateur = ligneInfos.split("@")
                nom = utilisateur[0]
                tampon = utilisateur[1].split("#")
                age = int(tampon[0])
                taille = float(tampon[1])
                dico[nom] = (age, taille)
    # Si le fichier n'est pas trouvé à la lecture on le crée.
    except Exception as e:
        f = open(chemin + fichier, "wt") 
        f.close()
        print("Le fichier n'existait pas, il est maintenant crée.")
    else:
        print("Lecture fichier effectuée.")

def quitter():
    print("Fin de programme.")
    input("Appuyer sur la touche <Entrée> pour quitter !")
    raise SystemExit

def clear():
    if os.name == "nt": os.system('cls') 
    else: os.system('clear') 

def main():
    reponse = ""
    clear()
    # solution premiere et deuxieme partie
    # menu = """
    # (L) Lecture
    # (I) Inscription
    # (C) Consultation
    # (T) Consutation Totale
    # (E) Enregistrement
    # (Q) Quitter
    # """
    # while reponse != "Q":
    #     print(menu)
    #     reponse = input("Votre choix : ").upper()
    #     ligne()
    # # Solution avec match case :
    #     match reponse:
    #         case "L": lecture()
    #         case "I": inscription()
    #         case "C": consultation()
    #         case "T": consultationTotale()
    #         case "E": enregistrement()
    #         case "Q": quitter()
    #         case _: print("Choisissez l'une des option du menu.")
    #     ligne()
    #
    # # Solution avec if elif else :        
        # if reponse == "L": lecture()
        # elif reponse == "I": inscription()
        # elif reponse == "C": consultation()
        # elif reponse == "T": consultationTotale()
        # elif reponse == "E": enregistrement()
        # elif reponse == "Q": quitter()
        # else: print("Choisissez l'une des options du menu.")
        # ligne()

    # Solution 2
    dicoMenu = {
        "L" : ("Lecture", lecture),
        "I" : ("Inscription", inscription),
        "C" : ("Consultation par nom", consultation),
        "T" : ("Consultation totale", consultationTotale),
        "E" : ("Enregistrement", enregistrement),
        "Q" : ("Quitter", quitter)}  

    while reponse != "Q":
        for cle in dicoMenu:  # sorted(dicoMenu) ==> tri le menu sur la clé
            print(f"{cle} : {dicoMenu[cle][0]}")
        
        reponse = input("Votre choix : ").upper()
        ligne()

        if reponse not in dicoMenu.keys(): 
            print("Veuillez saisir un choix du menu.")
        else : 
            eval("dicoMenu.get(reponse, "")[1]()")

        ligne()
    
if __name__ == "__main__":
    main()
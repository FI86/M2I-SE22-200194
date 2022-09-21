# Exercice 15
# Définissez une classe JeuDeCartes() permettant d’instancier des objets dont le 
# comportement soit similaire à celui d’un vrai jeu de cartes. La classe devra comporter 
# au moins les quatre méthodes suivantes :

# • méthode constructeur : création et remplissage d’une liste de 52 éléments, 
# qui sont eux-mêmes des tuples de 2 entiers. Cette liste de tuples contiendra les 
# caractéristiques de chacune des 52 cartes. Pour chacune d’elles, il faut en effet 
# mémoriser séparément un entier indiquant la valeur (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14), les 4 
# dernières valeurs étant celles des valet, dame, roi et as), et un autre entier indiquant la couleur 
# de la carte (c’est-à-dire 0, 1, 2, 3 pour Coeur, Carreau, Trèfle et Pique).

# Dans une telle liste, l’élément (11,2) désigne donc le valet de Trèfle, et la 
# liste terminée doit être du type :
# [(2, 0), (3,0), (3,0), (4,0), ..... (12,3), (13,3), (14,3)] 

# • méthode nom_carte() : cette méthode doit renvoyer, sous la forme d’une chaîne, l’identité
# d’une carte quelconque dont on lui a fourni le tuple descripteur en argument. Par exemple,
# l’instruction : 
# print(jeu.nom_carte((14, 3))) doit provoquer l’affichage de : As de pique

# • méthode battre() : comme chacun sait, battre les cartes consiste à les mélanger.  Cette méthode sert 
# donc à mélanger les éléments de la liste contenant les cartes, quel qu’en
# soit le nombre. 
# • méthode tirer() : lorsque cette méthode est invoquée, une carte est retirée du jeu. Le tuple 
# contenant sa valeur et sa couleur est renvoyé au programme appelant. On retire toujours 
# la première carte de la liste. Si cette méthode est invoquée alors qu’il ne reste plus aucune 
# carte dans la liste, il faut alors renvoyer l’objet spécial None au programme appelant.

import random

class JeuDeCartes:
    """Classe Jeu de Cartes"""

    def __init__(self):
        self.couleur = ("Coeur", "Carreau", "Trefle", "Pique")
        self.valeurs = (2, 3, 4, 5, 6, 7, 8, 9, 10, "Valet", "Dame", "Roi", "As")
        self.cartes = []
        
        for couleur in self.couleur:
            for valeur in self.valeurs:
                self.cartes.append((valeur, couleur))
        
        self.nbCartes = len(self.cartes)
       
    def nom_carte(self, carte):
        return f"{carte[0]} de {carte[1]}"

    def battre(self):
        random.shuffle(self.cartes)

    def tirer(self):
        if len(self.cartes) != 0: return self.cartes.pop(0)
        else: return None

def main():
    jeu = JeuDeCartes()
    jeu.battre()
    index = 0
    
    while (len(jeu.cartes) != 0):
        index += 1
        c = jeu.tirer()
        print(f"{index} - {jeu.nom_carte(c)}")

    input("Appuyer sur une <Entrée> pour terminer !")

if __name__ == "__main__":
    main()
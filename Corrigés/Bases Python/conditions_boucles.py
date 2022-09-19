# Fichier d'exemples pour les instructions conditionnelles et les boucles

def main():
    # CONDITIONS
    x, y = 10, 100
    c = x + y

    # if, elif, else
    if x < y: 
        st = "x est plus petit que y"
    elif x == y: 
        st = "x est égale à y"
    else: 
        st = "x est plus grand que y"
    print(st)

    # match case
    match c:
        case 1 | 2: print(x)
        case 3: print(y)
        case _: print(c)    

    # condition ternaire
    st = "x est plus petit que y" if (x < y) else "x est plus grand que y"
    print(st)

    # Instruction imbriquée
    age1, age2 = 10, 100
    nom, ville = "Tabuteau", "Poitiers"
    
    if (age1 > 10):
        if (nom == "Tabuteau"):
            print(ville)
        else:
            print(age1)
    else:
        print(age2)

    # BOUCLES
    # Definir une boucle while
    x = 0
    while (x < 5):
        print(x)
        x += 1

    # Definir une boucle For
    for x in range(5, 10):
        print(x)

    # Utiliser For sur une collection
    jours = ["Lun", "Mar", "Mer", "Jeu", "Ven", "Sam", "Dim"]

    for elem in jours:
        print(elem)

    # Utilisation du break and continue
    for x in range(5, 10):
        if (x == 7):
            break
        if (x % 2 == 0):
            continue
        print(x)

    # Utiliser la fonction enumerate() pour retrouver l'index
    for i, j in enumerate(jours):
        print(i + 1, j)


    # compréhension de liste
    liste1 = [1, 4, 2, 7, 1, 9, 0, 3, 4, 6, 6, 6, 8, 3]
    liste2 = []
    liste3 = []
    liste4 = []

    # code sans compréhension de liste
    for elem in liste1:
        if elem > 5:
            liste2.append(elem)

    print(liste2)

    # code avec compréhension de liste simple
    liste3 = [elem for elem in liste1 if elem > 5]
    print(liste3)

    # code avec compréhension de liste complète
    liste4 = [elem * 2 if elem % 2 == 0 else elem ** 2 for elem in liste1]
    print(liste1)
    print(liste4)

if __name__ == "__main__":
    main()
# Fichier d'exemples pour les lambda, all, any, map et filter

# all (si toutes les conditions sont vraie)
x = 3
liste = [x == 3, x > 5, x < 3]
print("all =", all(liste))

# any (si une des conditons est vraie)
print("any =", any(liste))

# map applique une transformation à tout les éléments d'un itérable
# (une fois le map parcouru le curseur ne revient pas et n'est pas réutilisable)
def cube(x):
    return x ** 3

liste = [0, 1, 2, 3, 4]
map1 = map(cube, liste)

for x in map1:
    print("Element map =", x)

# conversion en liste d'un map
liste2 = list(map(cube, liste))
print("liste map :", liste2)

# filter : filtre avec un prédicat les éléments d'un itérable et retourne un booléen
liste2 = list(filter(lambda x: x < 3, liste))
print("liste avec éléments inférieur à 3 :", liste2)

# lambda
def CelsiusToFahrenheit(temp):
    return (temp * 9/5) + 32

def FahrenheitToCelsius(temp):
    return (temp - 32) * 5/9

# fonction principale
def main():
    ctemps = [0, 12, 34, 100]
    ctemps2 = [2, 4, 6]
    ftemps = [32, 65, 100, 234]

    # appel par fonction sans lambda
    print(list(map(CelsiusToFahrenheit, ctemps)))
    print(list(map(FahrenheitToCelsius, ftemps)))

    # avec lambda on a plus besoin des fonctions qui sont utilisées qu'une fois.
    print(list(map(lambda temp: (temp * 9/5) + 32, ctemps)))
    print(list(map(lambda temp: (temp - 32) * 5/9, ftemps)))
    print(list(map(lambda temp, temp2: ((temp + temp2) * 9/5) + 32, ctemps, ctemps2)))

if __name__ == "__main__":
    main()
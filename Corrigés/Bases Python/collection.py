# Fichier d'exemples pour les variables

# LISTES
# Déclarer une liste avec la possibilité de modifier son contenu
maliste = [0, 1, 1, 2, 2, 3, 5, 8, 13]
print(maliste)

# J'accède au 7e élément de la liste (les index commencent à 0)
print(maliste[6])

# Je retire le 5e élément de la liste
print(maliste.pop(4))
print(maliste)

# J'ajoute un élément à la fin
maliste.append(21)
print(maliste)
# Ou
maliste += [12]
print(maliste)

# J'extrais les éléments de la position 3 jusqu'à la fin de la liste
print(maliste[2:])

# J'extrais les deux premiers éléments
print(maliste[:2])

# J'extrais du 4eme éléments au 6eme inclus (les index commencent à 0)
print(maliste[3:6])

# J'extrais le dernier élément de la liste
print(maliste[-1])

# Quelle est la longueur de ma liste ?
print(len(maliste))

# Je modifie un élément (celui qui est en 3e position)
maliste[2] = 8
print(maliste)

# SERIE DE FONCTION SUR LES LISTES
# supprime le premier élément trouvé avec la valeur indiquée dans les ()
print(maliste.remove(1))

# suppression par index de la liste mais ne retourne pas la valeur supprimée
del maliste[0] 
print(maliste)

# nombre d'occurences correspondantes dans la liste.
print(maliste.count(8)) 

# retourne l’index d’une valeur
print(maliste.index(12)) 

# inverse la liste
maliste.reverse()
print(maliste)
print(type(maliste))

# listes imbriquées
ma_liste_imbrique = [1, [5, 6, 7], 2, 3]
print(ma_liste_imbrique)
print(ma_liste_imbrique[1][2])

# COPIER UNE LISTE
# Copie par référence (agit comme un alias de la première liste)
y = [1, 2, 3]
x = y
y[0] = 4
print(x)

# Copie par valeur
x = [1, 2, 3]
y = x[:]
# Ou
y = x.copy()
y[0] = 9
print(x, y)

# Transformation String en liste
ma_chaine = "Xavier:Tabuteau:Poitiers"
print(ma_chaine.split(":"))

# Transformation liste en string
ma_liste = ["Xavier", "Tabuteau", "Poitiers"]
print(' - '.join(ma_liste))

# Extension de liste  
ma_liste = ["Xavier", "Tabuteau"]
ma_liste2 = ['Ici', "Poitiers"]
ma_liste.extend(ma_liste2)
print(ma_liste)


# TUPLES
# Déclarer un tuple sans la possibilité de modifier son contenu
montuple = (0, 1, 1, 2, 2, 3, 5, 8, 13)
untuple = 1, 2, 3
print(montuple, untuple)

# J'accède au 7e élément du tuple (les index commencent à 0)
print(montuple[6])

# On peut pas modifier un tuple
# montuple.append(5)
# montuple.pop(4)
# montuple.remove("coucou")

# SET (ensemble non ordonné sans doublons)
# agit comme un dictionnaire n'ayant que des valeurs
# liste avec doublon
mon_set = ['pascal', 'pierre', 'paul', 'pierre']

# affichage en set
print(set(mon_set))

# reconverti en liste sans doublon
print(list(set(mon_set)))

# affectation d'un set
mon_set = {"pascal", "pierre", "paul", "pierre"}
set2 = {"toto", "titi"}

# ajouter une valeur
mon_set.add("toto")
print("mon set :", mon_set)

# supprimer une valeur
mon_set.remove("toto")
print("mon set :", mon_set)

# ajouter un autre set
mon_set.update(set2)
print("mon set :", mon_set)

# Construire un dictionnaire vide
dico = {}
print(dico)

# ajouter des éléments
dico['Computer'] = 'Ordinateur'
dico['Mouse'] = 'Souris'
dico['Keyboard'] = 'Clavier'

# ajouter un dictionnaire à un autre
dico.update({'Printer': 'Imprimante'})
print(dico)

# Un autre dictionnaire créer directement
berti = {
  'Nom': 'Bertignac', 
  'Prenom': 'Louis', 
  'Instruments': ['Guitare', 'Chant']}

print(berti)

# Accéder à la valeur rattaché à la clé Nom
print(berti['Nom'])
print(berti.get("Nom"))

# Accéder à une liste dans un dictionnaire
print(berti["Instruments"][0])

# Enregistrer un nouvel ensemble clé valeur
berti['Groupes'] = ['Higelin', 'Telephone', 'Bertignac et les visiteurs']
print(berti)

# Effacer une clé et la valeur qui lui est associée
del berti['Instruments']
print(berti)

# Récupérer la listes des clés
print(dico.keys())
print(berti.keys())

# Récupérer la listes des valeurs
print(dico.values())

# Récupérer la listes des clés/valeurs
print(dico.items())

# Copier un dictionnaire par référence
dico_ref = dico

# Copier un dictionnaire par valeur
dico_copy =  dico.copy()
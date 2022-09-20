# Fichier d'exemples de regex.
import re

# Utilisation.
texte = "Je m'appel Paul"
print("Paul" in texte)
pseudo = re.findall(r"kevin\d+", texte)
print(pseudo)

texte = "Je m'appelle Paul Paul33 Paul444 Paul9"
modele = r"Paul[0-9]+"
pseudo = re.findall(modele, texte)
print(pseudo)

# Reconnaitre un email.
# Test si l'email saisi est ok.
chaine = input("Saisir un email : ")
modele = r"[a-zA-Z0-9]+@[a-zA-Z]+\.(com|org|net|fr)"

if(re.search(modele, chaine)):
    print("Email valide")
else:
    print("Email non valide")

# Trouver toutes les dates.
texte = "On est le 15-03-2022 ou le 16/03/2022."
modele = r"\d{2}-\d{2}-\d{4}" # modele simple
modele = r"\b\d{2}(?:-|/)\d{2}(?:-|/)\d{4}\b" # modele amélioré
pt = re.compile(modele)
print(pt.findall(texte))

# Rechercher une chaîne de caractères comportant un "a" suivi de zéro ou plusieurs "b".
def correspondanceTexte(text):
    modeles = r"ab*"
    if re.search(modeles,  text):
        return "Correspond !"
    else:
        return "Correspond pas !"

print(correspondanceTexte("bc"))
print(correspondanceTexte("ac"))
print(correspondanceTexte("abc"))
print(correspondanceTexte("abbc"))

# Suppression des zéros de tête d'une adresse IP.
ip = "216.008.094.196"
modele = r"\.[0]+"
string = re.sub(modele, ".", ip)
print(string)

# Trouver un mot dans une chaine de caractères.
texte = "Python exercices, PHP exercices, C# exercices"
modele = "exercices"

for match in re.findall(modele, texte):
    print(f"Trouvé : {match}")

# Vérifier qu'une chaîne de caractères ne contient qu'un certain ensemble
# de caractères (dans ce cas, a-z, A-Z et 0-9).
def caracteresAutorise(string):
    charRe = re.compile(r"[^a-zA-Z0-9]")
    string = charRe.search(string)
    return not bool(string)

print(caracteresAutorise("ABCDEFabcdef123450")) 
print(caracteresAutorise("*&%@#!}{"))

# Vérifier qu'une chaîne de caractères ne contient que des lettres majuscules,
# minuscules, des chiffres et des caractères de soulignement.
def correspondanceTexte2(str1):
    modeles = r"^[a-zA-Z0-9_]*$"
    modeles = r"^\w*$" # modele simplifié avec le token \w
    if re.search(modeles, str1):
        return "Correspond !"
    else:
        return "Correspond pas !"

texte = "Le renard est dans le poulailler !"
print(correspondanceTexte2(texte))
print(correspondanceTexte2("Exercice_Python_1"))

# Rechercher certaines chaînes littérales dans une chaîne de caractères.
modeles = ["renard", "poulailler", "cheval"]

for modele in modeles:
    if re.search(modele, texte):
        print(f"{modele} dans {texte} -> Trouvé !")
    else:
        print(f"{modele} dans {texte} -> Pas trouvé !")

# Insérer des espaces entre les mots commençant par une majuscule.
def espace_mot_capitale(str1):
    modele = r"(\w)([A-Z])"
    separe_groupe = r"\1 \2"
    return re.sub(modele, separe_groupe, str1)

print(espace_mot_capitale("Python"))
print(espace_mot_capitale("PythonExercices"))
print(espace_mot_capitale("PythonExercicesSolutionPossible"))
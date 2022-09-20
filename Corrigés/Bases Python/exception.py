# Traiter une exception
nombre = input("Entrez un nombre : ")

try:
    nombre = int(nombre)
except ValueError:
    print("Désolé la valeur saisie n'est pas un nombre.")

# Double exception
try:
    numerateur = int(input("Entrez un numérateur : "))
    denominateur = int(input("Entrez un dénominateur : "))
    resultat = numerateur / denominateur
    print("Le résultat de la division est :", resultat)
except ValueError:
    print("Désolé, la valeur saisie n'est pas un nombre.")
except ZeroDivisionError:
    print("Désolé, la division par zéro n'est pas permise.")

# Récupérer le message d’une exception
nombre = input("Entrez nombre : ")

try:
    nombre = int(nombre)
except Exception as e:
    print(e)

# Clause else
# Le bloc else permet de distinguer la partie du code qui est susceptible de 
# produire une exception de celle qui fait partie du comportement nominal du 
# code mais qui ne produit pas d’exception.
try:
    numerateur = int(input("Entrez un numérateur : "))
    denominateur = int(input("Entrez un dénominateur : "))
    resultat = numerateur / denominateur
except (ValueError, ZeroDivisionError):
    print("Désolé, quelque chose ne s'est pas bien passé.")
else:
    print("Le resultat de la division est :", resultat)

# Post-traitement
# Un bloc finally est systématique appelé même si le bloc try est interrompu 
# par une instruction return.
try:
    numerateur = int(input("Entrez un numérateur : "))
    denominateur = int(input("Entrez un dénominateur : "))
    resultat = numerateur / denominateur
    print("Le resultat de la division est :", resultat)
except (ValueError, ZeroDivisionError):
    print("Désolé, quelque chose s'est mal passé.")
finally:
    print("afficher ceci quel que soit le résultat")

# Lever une exception
x = input("saisissez un nombre : ")

if int(x) < 0:
    raise ValueError("La valeur ne doit pas être négative")

# structure complete du try
try:
    pass
except Exception as e:
    pass
else:
    pass
finally:
    pass
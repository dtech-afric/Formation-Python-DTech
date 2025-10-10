### ============================= SEMAINE 4: STRUCTURES CONDITIONNELLES ==============

"""
Semaine 4: Structures conditionnelles et boucles
Module: Structures conditionnelles (if, else, elif)
Lesson: Structure if...else
"""

"""Dans cette leçon, vous apprendrez à utiliser les structures conditionnelles if, else et elif en Python.
Ces structures vous permettent d'exécuter du code en fonction de conditions spécifiques.
C'est essentiel pour contrôler le flux de votre programme.
Imaginez vous en train de créer un programme qui décide quoi faire en fonction de l'âge d'une personne.

Exemple : 
Si la personne a moins de 18 ans, le programme pourrait afficher "Vous êtes mineur".
Si la personne a entre 18 et 65 ans, il pourrait afficher "Vous êtes adulte".

"""

#================Exercice 1: Vérification de l'âge=================
"""
1 - Demandez à l'utilisateur de saisir son âge.
2 - Utilisez une structure if...else pour vérifier si l'utilisateur est majeur (18 ans ou plus) ou mineur (moins de 18 ans).
3 - Affichez un message approprié en fonction de l'âge de l'utilisateur.

"""
# ============= Resultats =============
age = int(input("Veuillez entrer votre âge: "))

if age >=18:
    print("Vous êtes majeur.")
else:
    print("Vous êtes mineur.")

#================Exercice 2: Vérification de la parité=================
"""
1 - Demandez à l'utilisateur de saisir un nombre entier.
2 - Utilisez une structure if...else pour vérifier si le nombre est pair ou impair.
3 - Affichez un message approprié en fonction de la parité du nombre.

"""
# ============= Resultats =============
nombre = int(input("Veuillez entrer un nombre entier: "))
if nombre % 2 == 0:
    print(f"Le nombre {nombre} est pair.")
else:
    print(f"Le nombre {nombre} est impair.")


#================Exercice 3: Vérification de la note=================
"""
1 - Demandez à l'utilisateur de saisir une note entre 0 et 100.
2 - Utilisez une structure if...elif...else pour déterminer la mention correspondante:
   - 90-100 : "Excellent"
    - 80-89 : "Très bien"
    - 70-79 : "Bien"
    - 60-69 : "Passable"
    - 0-59 : "Insuffisant"
3 - Affichez la mention correspondante.

"""
# ============= Resultats =============


###### ==================== UTILISATION DE IF ELSE AND OR  IN NOT ==================
"""
Pour aller plus loin, nous verrons comment utiliser les strucutres verifier si toutes les 
conditions sont vraies, inverser une logique et meme utiliser pour ecrire du code plus efficace et courte.
"""
# avec AND:
age = 20
permis = True #Boolean

if age >= 18 and permis:
    print("Tu peux conduire")

# avec OR
jour = "samedi"

if jour == "samedi" or jour == "dimanche":
    print("C’est le week-end")

# avec NOT
# ici nous allons verifié si un utilisateur est connecté ou non
est_connecte = False

if not est_connecte:
    print("Utilisateur non connecté")
else:
    print('Utilisateur connecté')


# code courte 
note_courses = 60
status = "Certified" if note_courses >= 80 else "Not Certified"
print(status)






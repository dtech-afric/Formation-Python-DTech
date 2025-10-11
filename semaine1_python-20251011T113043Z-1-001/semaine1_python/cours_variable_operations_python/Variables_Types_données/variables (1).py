import datetime
"""🔹 Variables et Types de Données en Python3"""

" Qu’est-ce qu’une variable ?"

"""Une variable est comme une “boîte” dans laquelle on stocke une valeur (nombre, texte, etc.)
pour la réutiliser plus tard.
En Python, on n’a pas besoin de déclarer le type à l’avance, il est défini automatiquement.
"""

""" Exemple :"""

nom = "Python"
age = 25
pi = 3.14
#est_etudiant = True

#print(nom, age, pi, est_etudiant)

"""Règles pour nommer une variable"""

"""Doit commencer par une lettre ou un underscore _.

Ne doit pas commencer par un chiffre.

Ne doit pas contenir d’espace ni de caractères spéciaux (! @ # % ...).

Sensible à la casse (Age ≠ age).
"""
""" Bonnes pratiques :

Utiliser des noms clairs : note_moyenne, prix_total.

Style recommandé en Python : snake_case (mots séparés par _).
"""

## affiche le nom et le prenom d'un individu

name = "Josué"
surname = "Jesugnon"

#print(name, surname)
#print(surname, name)

# je m'appelle josue jesugnon
#print(f"Je m'appelle {name} {surname}")

nom = "Josué" #### chaines de caractère (str)
prenom="Jesugnon"
age = 23.5 
#print(f"Je m'appelle {nom} {prenom}, j'ai {age} ans")

#print(type(age))

#### Exemple ####

menu = str(input('entrez votre menu:'))
nom_client=str(input("Le nom du client:"))
prenom_client=str(input("votre prenom:"))
restaurant=str(input("le type de restaurant de commande:"))
jour = str(input("entrer votre jour de reservation:"))
date_heure = int(input("l'heure de la commande:"))


print(f"Le client {nom_client} {prenom_client} desire gouter le {menu} le {jour} à {date_heure}h dans le restaurant {restaurant}")




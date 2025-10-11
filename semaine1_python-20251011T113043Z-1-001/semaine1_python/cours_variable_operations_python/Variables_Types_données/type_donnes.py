"""Types de données de base en Python

Nombres
int → entier (10, -5, 0)

float → décimal (3.14, -0.5, 2.0)
"""

a = 10        # int
b = 3.14      # float

"""Chaînes de caractères (str)

Texte encadré par "" ou ''
"""

nom = "Python"
langue = 'Français'

"""
Booléens (bool)

True ou False
"""
est_inscrit = True
aime_python = False

"""Conversion de types

Parfois, il faut changer le type d’une donnée.
"""

age = "25"          # chaîne
age_int = int(age)  # conversion en entier

print(age_int + 5)  # affiche 30


"""int() → en entier

float() → en nombre décimal

str() → en texte
"""
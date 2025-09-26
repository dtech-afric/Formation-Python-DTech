#==============📘 Cours : Les Boucles en Python (for et while)=====================

"""
Les boucles permettent de répéter une ou plusieurs instructions plusieurs fois, sans les réécrire.
Python propose deux types principaux de boucles :

for → quand on sait combien de fois on veut itérer ou qu’on parcourt une collection (liste, dictionnaire…).

while → quand on veut répéter tant qu’une condition est vraie.

"""
## Parcourir une liste
fruits = ["pomme", "banane", "cerise"]

for fruit in fruits:
    print(f"J'aime {fruit}")


# Parcourir une liste avec index

for i in range(len(fruits)):
    print(f"{i+1}. {fruits[i]}")


## Parcourir un dictionnaire
notes = {"Maths": 15, "PCT": 18, "Anglais": 12}

for matiere, note in notes.items():
    print(f"{matiere} : {note}")

# Boucle avec range

# 0,1,2,3,4
for i in range(5):  
    print(i)

# 1,2,3,4,5
for i in range(1, 6):  
    print(i)
    
# 0,2,4,6,8
for i in range(0, 10, 2):  
    print(i)


#############==================== WHILE ==================
#La boucle while
#syntaxe de base
i = 1
while i <= 5:
    print(i)
    i += 1  # incrémentation

# BOUCLER AVEC CONNDITION
mot = ""
while mot.lower() != "python":
    mot = input("Devine le mot magique : ")
print("Bravo !")

"""Instructions utiles dans les boucles

    break → quitte la boucle immédiatement

    continue → saute l’itération courante et passe à la suivante

else avec for ou while → s’exécute si la boucle s’est terminée normalement (pas par break)
"""
for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("Boucle terminée sans break")  # ne s’exécute pas ici

### SOMME DES NOTES 
notes = [15, 8, 12, 18, 9]
somme = 0

for note in notes:
    if note > 12:
        somme += note

print(f"Somme des notes > 12 : {somme}")

### CHERCHER UN MOT DANS UNE LISTE

mots = ["chat", "chien", "lapin"]
mot_a_trouver = "chien"

for mot in mots:
    if mot == mot_a_trouver:
        print("Trouvé !")
        break
else:
    print("Pas trouvé")

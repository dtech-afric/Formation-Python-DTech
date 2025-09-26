"""Instructions avancées sur les listes en Python.
Vous apprendrez des techniques avancées pour manipuler les listes, y compris le slicing, les compréhensions de liste et les méthodes de liste utiles.
"""

nombres = [1, 2, 12, 100, 25, 8, 3, 4, 5, 6, 7, 8, 9]

# Du 2e au 5e élément (indices 1 à 4)
print(nombres[0:5])  # Affiche [2, 3, 4, 5]

# Du début jusqu'au 3e élément
print(nombres[:3])   # Affiche [1, 2, 3]

# Du 4e élément jusqu'à la fin
print(nombres[3:])   # Affiche [4, 5, 6, 7, 8, 9]

# Tous les éléments, en sautant un sur deux
print(nombres[::2])  
# Une copie de la liste
print(nombres[:])    # Affiche [1, 2, 3, 4, 5, 6, 7, 8, 9]


#list.insert(indice, element) : Insère un élément à un indice spécifique.
nombres_insert = nombres.insert(1, "Jean")
print(nombres_insert)

#list.pop(indice) : Supprime et renvoie l'élément à l'indice donné (le dernier si l'indice est omis).
nombres_supprimer = nombres.pop(2)
print(nombres_supprimer)

#list.sort() : Trie la liste sur place (par ordre croissant par défaut).

nmbres_sorted = nombres.sort()
print(nmbres_sorted)

#list.reverse() : Inverse l'ordre des éléments de la liste.
nmbres_reserve = nombres.reverse()
print(nmbres_reserve)

# etendre une liste list1.extend(liste2) avec une autre liste en utilisant la methode extend
fruits_1 = ["pomme", "banane"]
fruits_2 = ["orange", "mangue"]

fruits_1.extend(fruits_2)

print(fruits_1)

### definir 
boites = ["boite1", "boite2", "boite3"]
print(boites)
# type de la variable
print(type(boites))

# inserer un element
boites.insert(4, "boite2.5")
print(boites)

## ajouter un element a la fin
boites.append("boite4")
print(boites)

# supprimer un element
boites.remove("boite2")
print(boites)

# ordonner une liste
boites.sort()
print(boites)

# inverser une liste
boites.reverse()
print(boites)

# extendre une liste
boites2 = ["boite5", "boite6"]
boites.extend(boites2)
print(boites)


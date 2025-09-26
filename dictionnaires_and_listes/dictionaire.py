"""Ici ce cours porte sur les dictionnaires en Python.
Vous apprendrez comment créer, accéder, modifier et supprimer des éléments dans un dictionnaire.


Un dictionnaire est une collection non ordonnée de paires clé-valeur.
"""

### creer un dictionnaire vide 
mon_dictionnaire = {}
print(mon_dictionnaire)

# creer un dictionnaire avec des paires clé-valeur
lancement_tache = {
    "tache_1": "créer la page de vente",
    "tache_2": "Rediger les emails de lancement",
    "tache_3": "configurer la passerelle",
    "tache_4": "tester le processus de commande",
    "tache_5": "lancer la campagne marketing"
}
print(lancement_tache)

# type de la variable
print(type(lancement_tache))

# accéder a une valeur
print(lancement_tache["tache_4"])

# ajouter une paire clé-valeur
lancement_tache["tache_6"] = "Analyser les statistiques de vente"
lancement_tache["tache_7"] = "preparer les supports visuel"
print(lancement_tache)

# supprimer une paire clé-valeur
del lancement_tache["tache_3"]
print(lancement_tache)

# obtenir toutes les clés d'un dictionaire
cles = lancement_tache.keys()
print(cles)

# obtenir toutes les valeurs d'un dictionaire
valeurs = lancement_tache.values()
print(valeurs)

# obtenir toutes les paires clé-valeur d'un dictionaire
paires = lancement_tache.items()
print(paires)

#####=============================#######

# partir de deux listes pour creer un dictionaire

#1* creer un dictionaire vide
personne = {}
#2* creer deux listes
cles = ["Nom", "Prénom", "Âge"]
valeurs = ["Doe", "John", 30]

# utiliser la fonction zip pour combiner les deux listes en paires clé-valeur
# puis convertir le zip en dictionaire avec la fonction dict
personne = dict(zip(cles, valeurs))
print(personne)

##### ============================#######
# étendre un dictionaire avec un autre dictionaire
adresse = {
    "Rue": "123 Rue Principale",
    "Ville": "Paris",
    "Code Postal": "75001",
    "Pays": "France",
    "Téléphone": "0123456789"
}
personne.update(adresse)
print(personne)

##### ============================#######
# parcourir un dictionaire avec une boucle for
for cle, valeur in personne.items():
    print(f"{cle}: {valeur}")

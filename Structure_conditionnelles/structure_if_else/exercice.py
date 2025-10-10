###=============== CONSOLIDATIONS DES ACQUIS ==============

            #### ============= EXERCICE 1 ===============
"""
Vous avez une liste d’étudiants inscrits à une session d'anglais . Votre objectif est de 
verifier si l'étudiant se trouve dans la base de données. Pour cela, 

    1- Creer une base de données vides nommées "etudiants_base"
    2- Insérer 03 prenoms de votre choix dans la base de données
    3- demander à un utilisateur d'entre son prenom
    4- Vérifier si le prénom est dans la liste.
    5- Afficher un message différent selon le cas

"""

        ###### ================ EXERCICE 2 ================

"""
Vous etes un professeur principal d'une classe de Terminale. Le premier semestre de l'année tend vers 
sa fin et vous devriez appreter les notes(maths, pct, anglais , histoire, svt, philo) et calculer les moyennes des élèves. Pour faciliter la tache, un élève
intelligent qui sait manipuler les listes et dictionnaires, vous propose de :

1- Créer une liste des "notes"  et des "matières" de chaque élève
2- Vous fusionner ces listes pour obtenir un dictionnaire
3- Calculer maintenant la moyenne de l'élève
4- Verifier maintenant la mention de l'élève selon votre logique
        (0-9 --> Redouble
        10-11.99 ---> Passable
        12- 13.99 ---> Assez_bien
        14-15.99 ----> Bien
        16--18 ------> Très bien ou Excellent
        )
"""

   ###===================== EXERCICE 3=================

"""
Écris un programme qui :

1-Affiche la liste des plats disponibles.

2-Demande à l’utilisateur de choisir un plat.

3-Vérifie si le plat est dans le menu.

    A-Si oui → affiche le prix.

    B- Si non → affiche "Plat indisponible" et ajouter-le au menu

Bonus : permettre à l’utilisateur de choisir plusieurs plats et calculer la facture totale.
"""

#### ==================== Resultats ===============

## crerer un dictionnaires 

menu = {
    "Pizza": 2500,
    "Burger": 570,
    "Salade": 1560,
    "Pâtes": 600,
    "Sushi": 1890
}

# listes des plats disponibles

plats_disponibles = list(menu.keys())
print("Plats disponibles :", plats_disponibles)
# demander à l'utilisateur de choisir un plat
choix = input("Veuillez choisir un plat : ")
somme = 0
while choix != "":

    # vérifier si le plat est dans le menu

    if choix in menu:
        print(f"Le prix de {choix} est {menu[choix]} FCFA")
        somme += menu[choix]
        print(f"Votre total provisoire est de {somme} FCFA")
    else:
        print("Plat indisponible")
        # ajouter le plat au menu
        prix = float(input(f"Veuillez entrer le prix pour {choix} : "))
        menu[choix] = prix
        print(f"{choix} a été ajouté au menu avec un prix de {prix} FCFA")
    choix= input("Veuillez choisir un autre plat (ou appuyez sur Entrée pour terminer) : ")
    print("Menu mis à jour :", menu)
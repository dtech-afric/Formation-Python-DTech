lancement_tache = ["créer la page de vente", "Rediger les emails de lancement", "configurer la passerelle", "tester le processus de commande", "lancer la campagne marketing"]

print(lancement_tache)

# ajouter une tache au debut

lancement_tache.insert(0, "preparer les supports visuel")
print(lancement_tache)

# ajouter une tache a la fin
lancement_tache.append("Analyser les statistiques de vente")
print(lancement_tache)

# supprimer une tache
lancement_tache.remove("configurer la passerelle")
print(lancement_tache)

# ordonner les taches
lancement_tache.sort()
print(lancement_tache)

# inverser l'ordre des taches
lancement_tache.reverse()
print(lancement_tache)

# calculer la longueur de la liste
print(len(lancement_tache))

# longueur d'un element
print(len(lancement_tache[0]))


#####=============================#######
# creer une liste
elements = ["Rôle : 'Agis comme un expert en SEO'.", "Tâche : 'Rédige l'introduction d'un article de blog'.", "Sujet : 'sur les 5 techniques de prompt engineering'.", "Format : 'en 150 mots et avec un ton engageant'."]

element_prompt = ",".join(elements)
print(element_prompt)
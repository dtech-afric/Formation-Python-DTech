"""Exercice 1:Gestion d'une liste de produit"""
#Création *de la liste "tache_lancement"
taches_lancement =["Creer la page de vente","Rédiger les emails de lancement","Configurer la paserelle de lancement","Lancer la campagne","Envoyer l'email de lancement à la liste "]
#Affichage de la liste 
print(taches_lancement)
taches_lancement.insert(0,"Préparer les supports visuels")
#Ajout de la tache "Analyser les statistiques de vente" à la fin de la liste 
taches_lancement.append("Analyser les statistiques de vente")
#supression de la tache "Configurer la paserelle de lancement"
taches_lancement.remove("Configurer la paserelle de lancement")
#Affichage de la liste finale
print(taches_lancement)


"""Exercice 2: Utilisation des listes pour la génération de prompts"""
#
element_prompt = ["Rôle: 'Agis comme un expect en SEO'", "Tâche: 'Rédige l'introduction d'un article de blog'", "Sujet: 'sur les cinq(05) techniques de prompt engineering'", "Format: 'en 150 mots et avec un ton engageant' "]
#
prompt = ",".join(element_prompt)
print(prompt)
#
element_prompt.remove("Format: 'en 150 mots et avec un ton engageant' ")
print(element_prompt)
#
element_prompt.append("Cible : 'pour un public de débutant'.")
print(element_prompt)

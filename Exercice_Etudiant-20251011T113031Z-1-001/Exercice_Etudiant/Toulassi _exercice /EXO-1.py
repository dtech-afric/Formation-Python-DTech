# -*- coding: utf-8 -*-
"""
Created on Wed Sep 17 13:59:03 2025

@author: DELL
"""

#Exercice 1
Taches_lancemment=['Créer la page de vente','Rediger les emailsde lancement','Configurer lapasserelle de paiement','Lancer la campagne publicitaire','Envoyer email de lancement à la liste']
print(Taches_lancemment)
##Taches_lancemment.append('Préparer les supports visuels')
Taches_lancemment[0]='Préparer les supports visuels'
print(Taches_lancemment)
Taches_lancemment.append('Analyser les statistiques de la vente')
Taches_lancemment.remove('Configurer lapasserelle de paiement')
print(Taches_lancemment)

##Exercice 2

Element_prompt=["Role:'Agis comme un expert en SEO'","Tache:'Rediger l'introduction d'un article de blog'","Sujet:'sur les 5 techniques de prompt engineering'","Format:'en 150 MOTS ET AVEC UN TON ENGAGEANT'"]
print(Element_prompt)
Element_prompt.remove("Format:'en 150 MOTS ET AVEC UN TON ENGAGEANT'")
Element_prompt.append("Cible:'pour un public de débutant'")
print(Element_prompt)
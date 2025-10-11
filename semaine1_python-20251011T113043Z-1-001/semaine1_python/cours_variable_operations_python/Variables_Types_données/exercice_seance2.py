"""1-Crée une variable nom avec ton prénom et affiche :
votre nom et prenom dans un programme #ex01.py
"""

### creer nom
nom = "Narcisse"
prenom = "Nekoua"

print(f"Je m'appelle {nom} {prenom}")

# ================= exo2.py=================
"""2-Demande l’âge d’un étudiant (input), convertis-le en entier et affiche son âge dans 5 ans.
ce programme s'exécute dans un fichier nommé #exo2.py"""

age_etudiant = str(input("Entre votre age :"))
### convertir 
age_etudiant_entier = float(age_etudiant) +5

#print(f" Je m'appelle {nom} {prenom}, j'aurai {age_etudiant_entier} ans dans 5ans")


is_inscrit = bool(input("entrer si votre inscrit:"))
print(is_inscrit)
"""
Tu veux écrire un petit programme pour gérer une liste d’étudiants et leurs notes.
Chaque étudiant est représenté par un dictionnaire contenant son nom et sa note.

Écris une fonction ajouter_etudiant(liste_etudiants, nom, note) qui ajoute un dictionnaire {"nom": nom, "note": note} à la liste.

Écris une fonction moyenne_classe(liste_etudiants) qui retourne la moyenne des notes de la classe.

Écris une fonction meilleur_etudiant(liste_etudiants) qui retourne le nom et la note du meilleur étudiant.

Teste ton code avec une liste d’au moins 5 étudiants.


"""

### ===== resultats =====

def ajouter_etudiants(liste_etudiants, nom,note):
	liste_etudiants[nom]=note
	return liste_etudiants

ajouter_etudiants({}, "Alice", 15)
ajouter_etudiants({}, "Bob", 12)

def moyenne_classe(liste_etudiants):
	notes = list(liste_etudiants.values())
	moyenne = sum(notes)/len(notes)
	return f"La moyenne de la classe est :{moyenne}"

print(moyenne_classe({"Alice": 15, "Bob": 12, "Charlie": 18, "David": 10, "Eve": 14}))




def meilleur_etudiant(liste_etudiants):
    meilleur = max(liste_etudiants, key=liste_etudiants.get)
    return f"Le meilleur etudiant est {meilleur} avec une note de {liste_etudiants[meilleur]}"

print(meilleur_etudiant({"Alice": 15, "Bob": 12, "Charlie": 18, "David": 10, "Eve": 14}))
import numpy as np

# 1️⃣ Demander à l'utilisateur le nombre de matières
nb_matieres = int(input("Combien de matières voulez-vous entrer ? "))

# 2️⃣ Créer des listes vides pour stocker les matières et les notes
matieres = []
notes = []

# 3️⃣ Boucle pour saisir les matières et les notes
for i in range(nb_matieres):
    matiere = input(f"Entrez le nom de la matière {i+1} : ")
    matieres.append(matiere)
    
    while True:  # boucle pour vérifier la validité de la note
        try:
            note = float(input(f"Entrez la note pour {matiere} : "))
            if 0 <= note <= 20:
                notes.append(note)
                break
            else:
                print("Erreur : la note doit être entre 0 et 20.")
        except ValueError:
            print("Erreur : veuillez entrer un nombre valide.")

# 4️⃣ Créer un dictionnaire {matière: note}
note_matieres = dict(zip(matieres, notes))

# 5️⃣ Calculer la moyenne arrondie
moyenne = np.round(sum(note_matieres.values()) / len(note_matieres.values()), 2)

# 6️⃣ Afficher les résultats
print("\n===== Résultats =====")
for matiere, note in note_matieres.items():
    print(f"{matiere} : {note}")

print(f"\nMoyenne : {moyenne}")

# 7️⃣ Donner l'appréciation selon la moyenne
if 0 <= moyenne <= 9:
    print("Résultat : Redouble ❌")
elif 10 <= moyenne <= 13:
    print("Résultat : Passable 🙂")
elif 14 <= moyenne <= 16:
    print("Résultat : Bien 👍")
elif 17 <= moyenne <= 20:
    print("Résultat : Excellent 🚀")
else:
    print("Erreur : moyenne invalide")

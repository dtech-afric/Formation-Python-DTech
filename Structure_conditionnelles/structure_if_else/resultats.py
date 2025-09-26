### ================== Exercie 2 ==============
import numpy as np
# 1- creer deux listes
notes = [15, 18, 15, 9, 17, 12]
matieres = ["Maths", "PCT", "Anglais", "Histoire", "SVT", "Philo"]

# 2- fusionner les deux listes

note_matieres = dict(zip(matieres, notes))

print(note_matieres)

print(f"Les matières sont : list({note_matieres.keys()})")

#3- calculer la moyenne

moyenne = np.round(sum(note_matieres.values()) / len(note_matieres.values()), 2)

print(f"La moyenne est : {moyenne:.2f}")

# 4- Conditionnelle pour appréciation
if 0 <= moyenne <= 9.99:
    print("Résultat : Redouble ❌")
elif 10 <= moyenne <= 11.99:
    print("Résultat : Passable 🙂")
elif 14 <= moyenne <= 16:
    print("Résultat : Bien 👍")
elif 17 <= moyenne <= 20:
    print("Résultat : Excellent 🚀")
else:
    print("Erreur : moyenne invalide")
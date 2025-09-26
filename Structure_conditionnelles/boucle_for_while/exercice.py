
"""
📝 Exercice : Gestion des Notes d’un Étudiant

Objectif :

    1-Écrire un programme Python qui :

    2-Demande à l’utilisateur le nombre de matières.
    3-Permet de saisir le nom de chaque matière et la note correspondante (0–20).

    4-Stocke ces informations dans un dictionnaire {matière: note}.

    5-Calcule la moyenne arrondie à 2 décimales.

Affiche :

Chaque matière et sa note

La moyenne

Une appréciation selon la moyenne :

Moyenne	Appréciation
0 – 9	Redouble ❌
10 – 13	Passable 🙂
14 – 16	Bien 👍
17 – 20	Excellent 🚀


Instructions détaillées :

    Créer des listes vides matieres et notes.

    Utiliser une boucle for pour demander les noms de matières et les notes.

    Vérifier que la note saisie est entre 0 et 20 (boucle while si nécessaire).

    Fusionner les listes pour créer un dictionnaire avec zip().

    Calculer la moyenne avec sum() et len().

    Arrondir la moyenne à 2 décimales avec round() ou numpy.round().

    Afficher chaque matière et sa note avec une boucle for.

    Afficher la moyenne et l’appréciation selon le tableau ci-dessus.

"""
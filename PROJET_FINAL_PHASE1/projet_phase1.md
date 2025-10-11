## 🎯 Projet 1 — Jeu “Qui veut gagner des points ?” (Mini Quiz Console)

### 🎯 Objectif : appliquer les conditions, boucles, fonctions, listes, tuples, et la logique.

### Description :


1- Créer un petit quiz interactif dans le terminal :

##  *Chaque partie contient 5 à 10 questions*

##  *L’utilisateur tape la lettre de la bonne réponse*

## *+10 points si c’est correct, -5 sinon*

##  *À la fin, on affiche le score total*

Les questions sont stockées dans une liste de dictionnaires

``` bash
Exemple de structure :

questions = [
    {"question": "Que signifie CPU ?", 
     "options": ["Central Processing Unit", "Computer Power Unit", "Central Program Utility"], 
     "answer": 0},
]

```

#### Concepts travaillés :

1.  Boucles for, while

2.  Gestion des entrées utilisateur

3.  Listes, dictionnaires, conditions

4.  Affichage formaté

5.  Calcul de score

6.  Sauvegarde du score dans un fichier texte (bonus)

```python
Idée bonus :
Créer un mode multi-joueur avec classement à la fin.
Ou sauvegarder l’historique des parties dans un fichier .txt.

```

### Livrable : un script Python `quiz.py` fonctionnel avec au moins 5 questions
import math
import numpy as np



def hello():
    print("Hello, World!")

#hello()

# calculer la somme de deux nombres
def somme():
    a = int(input("Entrez le premier nombre: "))
    b = int(input("Entrez le deuxieme nombre: "))
    resutat = a + b
    return resutat

#print(somme())

def aire_cercle(rayon):
    aire = math.pi * rayon ** 2
    return aire

print(aire_cercle(5))

def division(a, b):
    if b == 0:
        return "Erreur: Division par zero"
    else:
        return a / b
    
print(division(10, 2))
print(division(10, 0))
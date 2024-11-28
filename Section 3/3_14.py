import random

valeur_a_trouver = random.randint(0, 100)
nombre_utilisateur = int(input())
essais = 1

while essais < 6 and nombre_utilisateur != valeur_a_trouver:
    if nombre_utilisateur < valeur_a_trouver:
        print("Trop petit")
    else:
        print("Trop grand")
    nombre_utilisateur = int(input())
    essais += 1
        
if nombre_utilisateur == valeur_a_trouver:
    print("Gagné en", essais, "essai(s) !")
else:
    print("Perdu ! Le secret était", valeur_a_trouver)
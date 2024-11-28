from math import sqrt

nom_polyedre = str(input())
longueur_arrete = float(input())

if nom_polyedre == "T":
    print((sqrt(2) / 12) * longueur_arrete ** 3)
elif nom_polyedre == "C":
    print(longueur_arrete ** 3)
elif nom_polyedre == "O":
    print((sqrt(2) / 3) * longueur_arrete ** 3)
elif nom_polyedre == "D":
    print(((15 + 7 * sqrt(5)) / 4) * longueur_arrete ** 3)
elif nom_polyedre == "I":
    print(((5 * (3 + sqrt(5))) / 12) * longueur_arrete ** 3)
else:
    print("Polyèdre non connu")
import random 

secret = random.randint(0, 5)
val_utilisateur = int(input("Devinez la valeur aléatoire entre 0 et 5."))

if (val_utilisateur == secret):
    print("gagné !")
else:
    print("perdu : La valeur était ", secret, ".")
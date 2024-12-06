from random import randint, seed

def bat(points, coup_joueur, coup_ordinateur):
    pfc = ['Pierre', 'Feuille', 'Ciseaux']
    
    if coup_joueur == coup_ordinateur:
        print(f'{pfc[coup_ordinateur]} annule {pfc[coup_joueur]} : {points}')
    elif (coup_joueur == 0 and coup_ordinateur == 2) or (coup_joueur == 1 and coup_ordinateur == 0) or (coup_joueur == 2 and coup_ordinateur == 1):
        points += 1
        print(f'{pfc[coup_ordinateur]} est battu par {pfc[coup_joueur]} : {points}')
    else:
        points -= 1
        print(f'{pfc[coup_ordinateur]} bat {pfc[coup_joueur]} : {points}')
    return points

def affiche_resultat(points):
    if points == 0:
        print("Nul")
    elif points > 0:
        print("Gagné")
    else:
        print("Perdu")

PIERRE = 0
FEUILLE = 1
CISEAUX = 2

points = 0

s = int(input())
seed(s)

for i in range(5):
    coup_ordinateur = randint(0, 2)
    coup_joueur = int(input())
    
    points = bat(points, coup_joueur, coup_ordinateur)

affiche_resultat(points)
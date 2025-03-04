def placer_pion(couleur, colonne, grille):
    modifiable = False
    line = 0
    while line <= 5 and not modifiable:
        if grille[line][colonne] == "V":
            grille[line][colonne] = couleur
            modifiable = True
        line += 1
    return modifiable, grille



premiere_grille = [['V', 'V', 'V', 'J', 'V', 'V', 'V'],
                     ['V', 'V', 'V', 'V', 'V', 'V', 'V'],
                     ['V', 'V', 'V', 'V', 'V', 'V', 'V'],
                     ['V', 'V', 'V', 'V', 'V', 'V', 'V'],
                     ['V', 'V', 'V', 'V', 'V', 'V', 'V'],
                     ['V', 'V', 'V', 'V', 'V', 'V', 'V']]
print(placer_pion("R", 3, premiere_grille))

deuxieme_grille = [['J', 'J', 'J', 'J', 'R', 'R', 'R'],
                     ['R', 'R', 'R', 'R', 'R', 'V', 'V'],
                     ['J', 'J', 'J', 'J', 'J', 'V', 'V'],
                     ['V', 'R', 'J', 'R', 'J', 'V', 'V'],
                     ['V', 'V', 'V', 'V', 'J', 'V', 'V'],
                     ['V', 'V', 'V', 'V', 'R', 'V', 'V']]
print(placer_pion("J", 4, deuxieme_grille))
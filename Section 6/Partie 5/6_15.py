def gagnant(grille):
    for i in range(len(grille)):
        for j in range(len(grille[i])):
            if grille[i][j] != 'V':
                if i < len(grille) - 3 :
                    if grille[i][j] == grille[i+1][j] == grille[i+2][j] == grille[i+3][j]:
                        return grille[i][j]
                if j < len(grille[i]) - 3 :
                    if grille[i][j] == grille[i][j+1] == grille[i][j+2] == grille[i][j+3]:
                        return grille[i][j]
                if i < len(grille) - 3 and j < len(grille[i]) - 3:
                    if grille[i][j] == grille[i+1][j+1] == grille[i+2][j+2] == grille[i+3][j+3]:
                        return grille[i][j]
                if i > 2 and j < len(grille[i]) - 3:
                    if grille[i][j] == grille[i-1][j+1] == grille[i-2][j+2] == grille[i-3][j+3]:
                        return grille[i][j]
    return None
    
print(gagnant([['V', 'V', 'V', 'J', 'R', 'R', 'J'],
         ['V', 'V', 'V', 'R', 'J', 'R', 'R'],
         ['V', 'V', 'V', 'V', 'R', 'J', 'J'],
         ['V', 'V', 'V', 'V', 'V', 'V', 'J'],
         ['V', 'V', 'V', 'V', 'V', 'V', 'V'],
         ['V', 'V', 'V', 'V', 'V', 'V', 'V']]))

print(gagnant([['V', 'R', 'J', 'J', 'J', 'R', 'V'],
         ['V', 'V', 'V', 'V', 'V', 'V', 'V'],
         ['V', 'V', 'V', 'V', 'V', 'V', 'V'],
         ['V', 'V', 'V', 'V', 'V', 'V', 'V'],
         ['V', 'V', 'V', 'V', 'V', 'V', 'V'],
         ['V', 'V', 'V', 'V', 'V', 'V', 'V']]))

print(gagnant([['J', 'R', 'J', 'J', 'J', 'R', 'R'],
               ['R', 'R', 'R', 'J', 'R', 'J', 'J'], 
               ['J', 'J', 'R', 'R', 'J', 'V', 'R'], 
               ['V', 'V', 'R', 'V', 'J', 'V', 'V'], 
               ['V', 'V', 'V', 'V', 'V', 'V', 'V'], 
               ['V', 'V', 'V', 'V', 'V', 'V', 'V']]))
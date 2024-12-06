def bat(joueur_1, joueur_2):
    return (joueur_1 == 0 and joueur_2 == 2) or (joueur_1 == 1 and joueur_2 == 0) or (joueur_1 == 2 and joueur_2 == 1)
    
print(bat(0, 0))
print(bat(0, 1))
print(bat(2, 1))
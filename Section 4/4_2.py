def soleil_leve(heure_leve, heure_couche, heure_actuelle):
    return heure_leve <= heure_actuelle < heure_couche or heure_couche == heure_leve == 0 or heure_couche < heure_leve <= heure_actuelle or heure_actuelle < heure_couche < heure_leve

heure_leve_e1515 = int(input())
heure_couche_e1515 = int(input())
heure_leve_e666 = int(input())
heure_couche_e666 = int(input())

for heure_actuelle in range(24):
    est_leve_e1515 = soleil_leve(heure_leve_e1515, heure_couche_e1515, heure_actuelle)
    est_leve_e666 = soleil_leve(heure_leve_e666, heure_couche_e666, heure_actuelle)
    print(heure_actuelle, end='')
    if not est_leve_e1515 and not est_leve_e666:
        print(' *', end='')
    print()
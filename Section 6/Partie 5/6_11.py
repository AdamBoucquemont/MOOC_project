from math import pi

def bonne_planete(diametre):
    aire = pi * diametre ** 2
    return aire >= 50 * 1000
    
assez_grande = bonne_planete(int(input()))
if assez_grande:
    print("Bonne planète")
else:
    print("Trop petite")
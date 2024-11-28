saut = int(input())
position_cible = int(input())
position_courante = saut

while position_courante != position_cible and position_courante != 0:
   print(position_courante)
   position_courante = (position_courante + saut) % 100
   
if position_courante == position_cible:
    print("Cible atteinte")
else:
    print(position_courante)
    print("Pas trouvée")
pari_joueur = int(input())
num_tirage = int(input())
mise = 10
gain = 0

if pari_joueur <= 12 and pari_joueur == num_tirage:
    gain = mise * 12
elif pari_joueur == 13 and num_tirage % 2 == 0:
    gain = mise * 2
elif pari_joueur == 14 and num_tirage % 2 != 0:
    gain = mise * 2
elif pari_joueur == 15 and num_tirage in (1, 3, 5, 7, 9, 12):
    gain = mise * 2
elif pari_joueur == 16 and num_tirage not in (1, 3, 5, 7, 9, 12):
    gain = mise * 2
    
print(gain)
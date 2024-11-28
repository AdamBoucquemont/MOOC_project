nb_nombre = int(input())
somme = 0

if nb_nombre >= 0:
    for i in range(nb_nombre):
        new_valeur = int(input())
        somme += new_valeur
elif nb_nombre == -1:
    new_valeur = input()
    while new_valeur != 'F':
        somme += int(new_valeur)
        new_valeur = input()
print(somme)
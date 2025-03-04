def charger(filename, sep=';'):
    liste_donnees = []
    with open(filename, 'r', encoding='utf-8') as mon_csvfile:
        les_entetes = mon_csvfile.readline().strip().split(sep)
        for ligne in mon_csvfile:
            d_donnees = {}
            l_donnees = ligne.strip().split(sep)
            for index, donnee in enumerate(l_donnees):
                d_donnees[les_entetes[index]] = donnee
            liste_donnees.append(d_donnees)
    return liste_donnees

first_file = input()
second_file = input()
# first_file = 'Section 6/Partie 5/result-pass-fail-0.csv'
# second_file = 'Section 6/Partie 5/result-count-0.csv'
reussite_exercice = charger(first_file)
etudiant_exercices = charger(second_file)

etudiants_fiable = []
for index, etudiant in enumerate(etudiant_exercices):
    is_fiable = True
    for ex in etudiant:
        nb_essais = etudiant_exercices[index][ex]
        if nb_essais:
            if int(nb_essais) > 10:
                is_fiable = False
                break
    if is_fiable:
        etudiants_fiable.append(index)

nb_reussite = [{sum(1 for index, item in enumerate(reussite_exercice) if item[exercice] == 'VRAI' and index in etudiants_fiable) : exercice} for exercice in reussite_exercice[0]]
nb_reussite = sorted(nb_reussite, key=lambda d: (next(iter(d)), d[next(iter(d))]), reverse=True)

for exercice in nb_reussite:
    for key, value in exercice.items():
        print(value)
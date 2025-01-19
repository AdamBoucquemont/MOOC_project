with  open('Section 5/mots.txt', encoding = "utf-8") as fichier:
    nombre_mots = mots_avec_e = 0

    for ligne in fichier:
        mots = ligne.split()
        for mot in mots:
            if 'e' not in mot:
                print(mot)
                mots_avec_e += 1
            nombre_mots += 1

print(f'Pourcentage de mots ne contenant pas de e : ', mots_avec_e / nombre_mots * 100, '%.')
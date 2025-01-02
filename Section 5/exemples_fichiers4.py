with  open("Section 5/mots.txt", encoding = "utf-8") as fichier:
    mot_quatre_double_consecutifs = []
    for word in fichier:
        word = word.strip()
        nb_double_consommes = 0
        index = 0
        while index < len(word) - 1 and nb_double_consommes < 4 :
            if word[index] == word[index+1]:
                nb_double_consommes += 1
                index += 2
            else:
                index += 1
        if nb_double_consommes == 4:
            mot_quatre_double_consecutifs.append(word)
    
    print(mot_quatre_double_consecutifs)
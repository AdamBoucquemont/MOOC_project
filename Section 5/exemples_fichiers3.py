with  open("Section 5/words.txt", encoding = "utf-8") as fichier:
    mot_trois_double_consecutifs = []
    for word in fichier:
        word = word.strip()
        nb_double_consommes_consecutives = 0
        index = 0
        while index < len(word) - 1 and nb_double_consommes_consecutives < 3 :
            if word[index] == word[index+1]:
                nb_double_consommes_consecutives += 1
                index += 2
            else:
                index += 1
                nb_double_consommes_consecutives = 0
        if nb_double_consommes_consecutives == 3:
            mot_trois_double_consecutifs.append(word)
    
    print(mot_trois_double_consecutifs)
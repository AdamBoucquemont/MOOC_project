def liste_des_mots(file_name):
    liste_mots = []
    with  open(file_name, encoding = "utf-8") as my_file:
        for line in my_file:
            for sep in ['-', "'",'"', '?', '!', ':', ';', '.', ',', '*', '=', '(', ')', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                line = line.replace(sep, ' ')
            for word in line.split():
                if word.lower() not in liste_mots:
                    liste_mots.append(word.lower())
    liste_mots.sort()
    return liste_mots
        
print(liste_des_mots("Section 5/le-petit-prince.txt"))
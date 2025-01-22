def distance_mots(mot_1, mot_2):
    distance = 0
    for caractere1, caractere2 in zip(mot_1, mot_2):
        if caractere1 != caractere2:
            distance += 1
    return distance

def correcteur(mot, liste_mots):
    vrai_mot = ''
    index = 0
    while vrai_mot == '' and index != len(liste_mots):
        actual_distance = distance_mots(mot, liste_mots[index])
        if actual_distance <= 1:
            vrai_mot = liste_mots[index]
        index += 1
    return vrai_mot
    
    
print(correcteur("bonvour", ["chien", "chat", "train", "voiture", "bonjour", "merci"]))
print(correcteur("chat", ["chien", "chat", "train", "voiture", "bonjour", "merci"]))
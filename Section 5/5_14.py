def distance_mots(mot_1, mot_2):
    distance = 0
    for caractere1, caractere2 in zip(mot_1, mot_2):
        if caractere1 != caractere2:
            distance += 1
    return distance

print(distance_mots("lire", "bise"))
print(distance_mots("Python", "Python"))
print(distance_mots("merci", "adieu"))
print(distance_mots("chien", "niche"))
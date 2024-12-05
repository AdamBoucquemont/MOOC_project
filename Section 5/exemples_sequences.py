def keep_alnum(chaine):
    new_chaine = ''
    for caractere in chaine:
        if caractere.isalnum():
            new_chaine += caractere
    return new_chaine

def in_both(word1, word2):
    caracteres_en_commun = []
    for caractere in word1:
        if caractere in word2 and caractere not in caracteres_en_commun:
            caracteres_en_commun.append(caractere)
    return caracteres_en_commun

def lecture(invite):
    res = []
    x = input(invite)
    while x != '':
        decoupe = x.split()
        for elem in decoupe:
            res.append(int(elem))
        x = input()
    return res

print(keep_alnum('he23.?56th'))
print(in_both('pommeees', 'oranges'))
print(lecture("liste d'entiers terminée par une ligne vide : "))
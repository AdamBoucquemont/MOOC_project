import re

def wc(nomFichier):
    with  open(nomFichier, encoding = "utf-8") as my_file:
        content = my_file.read()
        nb_caracteres = len(content)
        nb_mots = 0
        actual_word = ''
        for index in range(nb_caracteres):
            if actual_word.isalnum():
                actual_word += content[index]
                if not actual_word.isalnum():
                    nb_mots += 1
                    actual_word = ''
            else:
                actual_word = content[index]
        nb_lignes = len(re.findall('\n', content))
        return nb_caracteres, nb_mots, nb_lignes

print(wc("Section 5/wc1.txt"))
print(wc("Section 5/Zola.txt"))
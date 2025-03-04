import re

def file_histogram(fileName):
    dictionnaire = {}
    with open(fileName) as file:
        for line in file:
            for letter in line:
                if letter in dictionnaire:
                    dictionnaire[letter] += 1
                else : 
                    dictionnaire[letter] = 1
        return dictionnaire
    
def words_by_length(fileName):
    dictionnaire = {}
    with open(fileName) as file:
        for line in file:
            all_words = re.findall(r'[A-z|À-ÿ]+', line)
            for word in all_words:
                if len(word) in dictionnaire:
                    if word.lower() not in dictionnaire[len(word)]:
                        dictionnaire[len(word)].append(word.lower())
                else:
                    dictionnaire[len(word)] = [word.lower()]
        for key in dictionnaire:
            dictionnaire[key].sort()
        return dictionnaire
    
    
    
print(file_histogram("Section 6/Partie 5/Zola.txt"))
print(words_by_length("Section 6/Partie 5/Zola.txt"))
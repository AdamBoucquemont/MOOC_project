def belongs_to_file(word, filename):
    with open(filename, encoding = "utf-8") as file:
        for line in file:
            for new_word in line.split():
                if word == new_word:
                    return True
    return False
    
print(belongs_to_file("renard", "Section 6/Partie 5/words.txt"))
print(belongs_to_file("aaronical", "Section 6/Partie 5/words.txt"))
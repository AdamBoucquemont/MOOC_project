def acrostiche(file_name):
    with open(file_name, encoding = "utf-8") as my_file:
        mot_accrostiche = ''
        for line in my_file:
            mot_accrostiche += line[0]
    return mot_accrostiche

print(acrostiche('Section 5/Apollinaire.txt'))
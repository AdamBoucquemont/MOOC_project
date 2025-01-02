def text_sans_e(file_name):
    with  open(file_name, encoding = "utf-8") as fichier:
        texte = fichier.read()
        texte = texte.replace('é', 'e')
        texte = texte.replace('è', 'e')
        texte = texte.replace('ê', 'e')
        texte = texte.replace('ë', 'e')
        return "e" not in texte
        
print(text_sans_e("Section 5/mots.txt"))
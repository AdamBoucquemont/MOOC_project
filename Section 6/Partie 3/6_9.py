def compteur_lettres(texte):
    dictionnaire = dict(zip('abcdefghijklmnopqrstuvwxyz', (0 for _ in range(26))))
    for caractere in texte:
        if caractere.lower() in dictionnaire:
            dictionnaire[caractere.lower()] += 1
    return dictionnaire
        
    
print(compteur_lettres("Dessine-moi un mouton !"))
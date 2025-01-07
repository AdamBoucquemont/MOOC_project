# def symetrie_verticale(carre):
#    """renvoie l'image de la matrice carre par symétrie verticale"""

#    n = len(carre)
#    return [[carre[i][j] for j in range(n-1,-1,-1)] for i in range(n)]



def symetrie_verticale(carre):
    nouvelle_matrice = [[0] * len(carre) for i in range(len(carre))]
    for i in range(len(carre)):
        for j in range(len(carre)):
            nouvelle_matrice[i][j] = carre[i][len(carre) - j - 1]
    return nouvelle_matrice

carre = [[2, 7, 6], [9, 5, 1], [4, 3, 8]]
print(symetrie_verticale(carre))
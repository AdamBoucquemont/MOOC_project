def rotation(carre):
    n = len(carre)
    return [[carre[i][j] for i in range(n-1,-1,-1)] for j in range(n)]

carre = [[2, 7, 6], [9, 5, 1], [4, 3, 8]]
print(rotation(carre))
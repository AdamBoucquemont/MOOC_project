def symetrie_horizontale(A):
    n = len(A)
    return [[A[i][j] for j in range(n)] for i in range(n-1, -1, -1)]
    
print(symetrie_horizontale([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(symetrie_horizontale([['a', 'b'], ['c', 'd']]))
print(symetrie_horizontale([]))
# def antisymetrique(M):
#     for i in range(len(M)):
#         for j in range(len(M)):
#             if M[i][j] != -M[j][i]:
#                 return False
#     return True

def antisymetrique(M):
    n = len(M)
    return all(
        M[i][j] == -M[j][i] 
        for i in range(n) 
        for j in range(n)
    )
    
print(antisymetrique([[0, 1, 1], [-1, 0, 1], [-1, -1, 0]]))
print(antisymetrique([[0, 1], [1, 0]]))
print(antisymetrique([[1, -2], [2, 1]]))
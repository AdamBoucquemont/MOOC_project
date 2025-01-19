def print_mat(M):
    if not M:
        print("")
        return
    
    for i in range(len(M)):
        for j in range(len(M[0])):
            print(M[i][j], end=" ")
        print("")
        
# ma_matrice = eval(input())
# print_mat(ma_matrice)

print_mat([[1, 2], [3, 4], [5, 6]])
print_mat([['H', 'E', 'L', 'L', 'O'], ['W', 'O', 'R', 'L', 'D']])
print_mat([])
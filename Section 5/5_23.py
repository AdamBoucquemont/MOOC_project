def init_mat(m, n):
    return [[0] * n for i in range(m)]
    
print(init_mat(2, 3))
print(init_mat(0, 0))
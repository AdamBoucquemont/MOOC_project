def trace(M):
    return sum(M[i][i] for i in range(len(M)))

print(trace([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(trace([]))
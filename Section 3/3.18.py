n = int(input())
fibonacci_table = [[] for _ in range(n)]
for i in range(1, n+1):
    for j in range(i):
        fibonacci_table[i-1].append((i + j) % 10)
    for k in range(1, i):
        fibonacci_table[i-1].append((i + j - k) % 10)
for col, row in enumerate(fibonacci_table):
    print(" " * (n - col - 1), "".join(map(str, row)), sep="")
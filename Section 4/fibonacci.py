def fibo(n):
    """calcule le n-ième nombre de Fibonacci, avec : n de type int et
    fibo(0) valant 0
    fibo(1) valant 1 et
    fibo(n+1) valant fibo(n-1) + fibo(n)
    si n < 0 : fibo(n) retourne None"""
    
    if n == 0 or n == 1:
        return n
    elif n > 1:
        x = 0
        y = 1
        for _ in range(2, n):
            x, y = y, x + y
        return y
    
for i in range(100):
    print(fibo(i))
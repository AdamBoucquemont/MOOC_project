def catalan(n):
    fact_n = 1
    fact_2n = 1
    for i in range(1, 2 * n + 1):
        fact_2n *= i
        if i < n + 1:
           fact_n *= i 
    return int(fact_2n / ((fact_n * (n + 1)) * fact_n))
    
print(catalan(5))
print(catalan(0))
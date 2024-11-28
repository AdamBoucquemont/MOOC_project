from math import sqrt

def premier(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True
    
    
x = int(input())
for i in range(x):
    if premier(i):
        print(i)
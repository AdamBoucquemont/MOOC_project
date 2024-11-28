n = int(input('entier strictement positif : '))
i = 0
while n != 1:
    i += 1
    print(n)
    if n % 2 == 0:
        n = n//2
    else:
        n = n*3+1
print("n :", n)
print("i :", i)
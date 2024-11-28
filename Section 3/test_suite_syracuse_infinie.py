n = 1
i = 0
while i < 9999999:
    n *= 10
    m = n
    while m != 1:
        i += 1
        if m % 2 == 0:
            m = m//2
        else:
            m = m*3+1
    print("n :", n)
    print("i :", i)
    i = 0
    
# 390905
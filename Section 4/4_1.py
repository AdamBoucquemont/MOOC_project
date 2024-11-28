def deux_egaux(a, b, c):
    return a == b or b == c or a == c
    
x = int(input())
y = int(input())
z = int(input())
print(deux_egaux(x, y, z))
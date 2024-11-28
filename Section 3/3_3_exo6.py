from math import sqrt

a = float(input())
b = float(input())

if a >= 0 and b >= 0:
    print(sqrt(a * b))
else:
    print("Erreur")
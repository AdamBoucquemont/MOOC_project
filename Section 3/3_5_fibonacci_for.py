n = int(input('nombre de termes à calculer de la suite de Fibonacci : '))
prec = 0
succ = 1 
print(prec, end = " ")
print(succ, end = " ")
for i in range(n-2):
    prec, succ = succ, prec + succ
    print(succ, end = " ")
print()
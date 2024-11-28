sinx = 0
x = float(input())
new_number = x
fact = 1
i = 1

while (abs(new_number) > 10**(-6)):
    sinx += new_number
    i += 2
    fact = fact * i * (i - 1)
    new_number = ((x**i)/fact)
    if (((i-1)/2)%2 != 0):
        new_number *= -1
print(sinx)
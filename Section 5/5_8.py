def premier(n):
    if n < 2:
        return False
    for i in range(2, int(n ** (1/2) + 1)):
        if n % i == 0:
            return False
    return True

def prime_numbers(nb):
    if not type(nb) == int or nb < 0:
        return None
    
    list_prime_numbers = []
    i = 0
    
    while len(list_prime_numbers) < nb:
        if premier(i):
            list_prime_numbers.append(i)
        i += 1
    
    return list_prime_numbers
    
print(prime_numbers(4))
print(prime_numbers(-2))
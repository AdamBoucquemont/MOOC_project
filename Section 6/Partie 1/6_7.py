def even(n):
    list_even_number = set()
    i = 0
    while i < n+1:
        list_even_number.add(i)
        i += 2
    return list_even_number
    
def prime_numbers(n):
    list_prime_numbers = set()
    for i in range(2, n+1):
        is_prime = True
        for index in range(i-1, 1, -1):
            if i%index == 0:
                is_prime = False
        if is_prime == True:
            list_prime_numbers.add(i)
    return list_prime_numbers

def prime_odd_numbers(numbers):
    list_odd_number = set()
    list_prime_numbers = set()
    list_even_number = even(max(numbers))
    list_all_prime_numbers = prime_numbers(max(numbers))
    for number in numbers:
        if number not in list_even_number:
            list_odd_number.add(number)
        if number in list_all_prime_numbers:
            list_prime_numbers.add(number)
    return (list_prime_numbers, list_odd_number)
    

print(prime_odd_numbers([1, 2, 6, 5, 11, 9, 13, 14, 12, 15, 17, 18]))
print(prime_odd_numbers([1, 4, 6, 12, 9, 15, 16, 21, 18]))
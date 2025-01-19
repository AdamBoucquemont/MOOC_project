def my_pow(m, b):
    if not isinstance(m, int) or not isinstance(b, float):
        return None
    return [b ** i for i in range(m)]

print(my_pow(3, 5.0))
print(my_pow(3.0, 5.0))
print(my_pow('a', 'b'))
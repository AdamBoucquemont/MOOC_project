def my_filter(lst, f):
    return [element for element in lst if f(element)]

print(my_filter(['hello', 666, 42, 'Thierry', 1.5], lambda x : isinstance(x, int)))
print(my_filter([-2, 0, 4, -5, -6], lambda x : x < 0))
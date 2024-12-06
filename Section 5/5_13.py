def my_insert(list, n):
    assert type(n) == int
    new_list = []
    index = 0
    while index < len(list) and list[index] < n:
        index += 1
    list.insert(index, n)

l = [1, 3, 5]
my_insert(l, 4)
print(l)

l = [1, 3, 5]
my_insert(l, 'a')
print(l)
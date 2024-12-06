def my_insert(list, n):
    if type(n) != int:
        return None
    new_list = []
    index = 0
    # while n not in new_list and index < len(list):
    #     if n < list[index]:
    #         new_list.append(n)
    #         new_list.append(list[index])
    #     else:
    #         new_list.append(list[index])
    #     index += 1
    # if n not in new_list:
    #     new_list.append(n)
    while index < len(list) and list[index] < n:
        index += 1
    new_list = list[:index] + [n] + list[index:]
    # new_list[len(new_list): len(new_list)] = list[index:]
    return new_list

print(my_insert([1, 3, 5], 4))
print(my_insert([1, 3, 5], 6))
print(my_insert([2, 3, 5], 1))
print(my_insert([2, 3, 5], 0.5))
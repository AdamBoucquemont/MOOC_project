def intersection(v, w):
    plus_grande_intersection = ''
    for index in range(len(v)):
        new_intersection = ''
        while v[index : index + len(new_intersection) + 1] in w and index + len(new_intersection) < len(v):
            new_intersection = v[index : index + len(new_intersection) + 1]
        if len(new_intersection) > len(plus_grande_intersection):
            plus_grande_intersection = new_intersection
    return plus_grande_intersection

print(intersection('programme', 'grammaire'))
print(intersection('salut', 'merci'))
print(intersection('merci', 'adieu'))
print(intersection('ironique', 'onirique'))
print(intersection('testz', 'oozo'))
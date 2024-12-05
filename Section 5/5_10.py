def dupliques(sequences):
    is_dublique = False
    index = 0
    while not is_dublique and index < len(sequences):
        if sequences[index] in sequences[index+1:]:
            is_dublique = True
        index += 1
    return is_dublique
        
print(dupliques([1, 2, 3, 4]))
print(dupliques(['a', 'b', 'c', 'a']))
print(dupliques('abcda'))
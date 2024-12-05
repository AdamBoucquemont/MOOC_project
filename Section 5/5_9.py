def anagrammes(v, w):
    are_anagrammes = len(v) == len(w)
    index = 0
    while are_anagrammes and index < len(w):
        if v.count(v[index]) != w.count(v[index]):
            are_anagrammes = False
        index += 1
    return are_anagrammes
    
print(anagrammes('marion', 'romina'))
print(anagrammes('bonjour', 'jour'))
print(anagrammes('pate', 'patte'))
print(anagrammes('patee', 'patte'))
print(anagrammes('pates', 'pate'))
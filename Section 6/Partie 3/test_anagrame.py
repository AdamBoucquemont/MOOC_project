def anagramme_str1(a, b):
    res = False
    for i in a:
        res = (i in b)
    return res

def anagramme_str2(a, b):
    res = True
    for i in a:
        if i not in b:
            res = False
    return res

def anagramme_0(a, b):
    return sorted(a) == sorted(b)

def anagramme_1(a,b):
    a.sort()
    b.sort()
    return a == b

def anagramme_2(a,b):
    liste_a = list(a)
    liste_a = liste_a.sort()
    liste_b = list(b)
    liste_b = liste_b.sort()
    return liste_a == liste_b

def anagramme_3(a,b):
    liste_a = list(a)
    liste_a.sort()
    liste_b = list(b)
    liste_b.sort()
    return liste_a == liste_b

def anagramme_dico(a,b):
    res = False
    if len(a)==len(b):
        dic_a = {}
        dic_b = {}
        for i in a:
            dic_a[i] = dic_a.get(i, 0) + 1
        for i in b:
            dic_b[i] = dic_b.get(i, 0) + 1
        res = dic_a == dic_b
    return res

def anagramme_dico2(a,b):
    res = False
    if len(a)==len(b):
        dic_a = {}
        dic_b = {}
        for i in a:
            dic_a[i] = dic_a.setdefault(i, 0) + 1
        for i in b:
            dic_b[i] = dic_b.setdefault(i, 0) + 1
        res = dic_a == dic_b
    return res

def anagramme_list(a,b):
    res = False
    if len(a) == len(b):
        liste_b = list(b)
        res = True
        for i in a:
            if i in liste_b:
                liste_b.remove(i)
            else:
                res = False
    return res

print(anagramme_str1('RâgE', 'gare'))
print(anagramme_str2('RâgE', 'gare'))
print(anagramme_0('RâgE', 'gare'))
# print(anagramme_1('RâgE', 'gare'))
print(anagramme_2('RâgE', 'gare'))
print(anagramme_3('RâgE', 'gare'))
print(anagramme_dico('RâgE', 'gare'))

for f in (anagramme_str1, anagramme_str2, anagramme_0, anagramme_2,
          anagramme_3, anagramme_dico, anagramme_dico2,
          anagramme_list):
    print("avec la fonction", f.__name__)
    print(f('bonjour', 'jourbon'))
    print(f('bonjour', 'jouxron'))
    print(f('bonjour', 'bonjur'))
    print(f('bonjour', 'jjourbon'))
    print(f('RâgE', 'gare'))
    print(f('râge', 'gare'))
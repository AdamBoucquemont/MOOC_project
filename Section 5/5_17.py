def decompresse(liste):
    return [t[1] for t in liste for _ in range(t[0])]

print(decompresse([(4, 1), (0, 2), (2, 'test'), (3, 3), (1, 'bonjour')]))
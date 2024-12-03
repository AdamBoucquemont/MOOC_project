def est_adn(chaine):
    i = 0
    while i != len(chaine) and chaine[i] in 'ACGT':
        i += 1
    return len(chaine) == i and len(chaine) != 0

print(est_adn("ATGGT"))
print(est_adn("ISA"))
print(est_adn("CTaG"))
print(est_adn(""))
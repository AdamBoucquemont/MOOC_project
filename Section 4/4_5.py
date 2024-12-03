def rendre_monnaie(prix, x20, x10, x5, x2, x1):
    prix_paye = x20 * 20 + x10 * 10 + x5 * 5 + x2 * 2 + x1
    monnaie_a_rendre = prix_paye - prix
    if monnaie_a_rendre < 0:
        return (None, None, None, None, None)
    y20 = monnaie_a_rendre // 20
    monnaie_a_rendre -= y20 * 20
    y10 = monnaie_a_rendre // 10
    monnaie_a_rendre -= y10 * 10
    y5 = monnaie_a_rendre // 5
    monnaie_a_rendre -= y5 * 5
    y2 = monnaie_a_rendre // 2
    monnaie_a_rendre -= y2 * 2
    y1 = monnaie_a_rendre
    return (y20, y10, y5, y2, y1)
    
print(rendre_monnaie(38, 1, 1, 1, 1, 1))
print(rendre_monnaie(56, 5, 0, 0, 0, 0))
print(rendre_monnaie(80, 2, 2, 2, 3, 3))
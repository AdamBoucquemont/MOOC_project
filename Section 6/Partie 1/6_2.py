def calcul_prix(produits, catalogue):
    # première version
    # prix = 0
    # for produit in produits:
    #     prix += produits[produit] * catalogue[produit]
    # return prix
    return sum(produits[produit] * catalogue[produit] for produit in produits)
    
produits = {"brocoli":2, "mouchoirs":5, "bouteilles d'eau":6}
catalogue = {"brocoli":1.50, "bouteilles d'eau":1, "bière":2,
             "savon":2.50, "mouchoirs":0.80}
print(calcul_prix(produits, catalogue))
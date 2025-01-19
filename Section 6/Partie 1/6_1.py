def inventaire(offres, objets):
    amis_a_visiter = set()
    for objet in offres:
        if objet in objets:
            amis_a_visiter.add(offres[objet])
    return amis_a_visiter
    
    
offres = {"lit" : "Antoine", "bibliothèque" : "Sébastien", "chaise" : "Isabelle",
            "livre 'Le vieil homme et la mer'" : "Ernest", "sac de bonbons" : "Thierry",
            "smartphone" : "Ted", "table" : "Sophie"}
objets = ["sac de bonbons", "table", "chaise", "lit", "livre 'Le vieil homme et la mer'"]
print(inventaire(offres, objets))
def valeurs(dico):
    sorted_keys = sorted([key for key in dico.keys()])
    sorted_values = [dico[key] for key in sorted_keys]
    return sorted_values
    
print(valeurs({'three': 'trois', 'two': 'deux', 'one': 'un'}))
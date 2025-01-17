# Liste des lettres en communes
print(list(set("pommeee") & set("banane")))

# Liste des mots contenant toutes les voyelles
with open('Section 6\Partie 1\mots.txt') as f:
    print([w.strip() for w in f if {'a','e','i','o','u','y'} <= set(w)])

# compte le npmbre d'occurence de chaque lettre dans un mot
def histogram(s):
    """Renvoie le dictionnaire des lettres dans s avec leur fréquence."""
    d = {}   # dictionnaire vide
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d
 
h = histogram('brontosaurus')
print(h)

# Liste des amis 
def construction_dict_amis(liste_amis):
   """ construit et renvoie un dictionnaire de personnes qui ont chacun
   l'ensemble de leurs amis
   liste_amis : liste de couple (p1, p2) : p1 a comme ami p2"""
   amis = {}
   for prenom1, prenom2 in liste_amis:
       if prenom1 not in amis:
           amis[prenom1] = {prenom2}
       else:
           amis[prenom1].add(prenom2) # pas d'effet si déjà présent
       if prenom2 not in amis:
           amis[prenom2] = set() # nouvelle entrée prenom2
   return amis

t = 'Thierry'
m = 'Michelle'
s = 'Sébastien'
p = 'Pierre'
a = 'Ariane'
q = 'Quidam'
ma_liste = [(t, m), (t, s), (t, p), (t, a), (m, t), (m, a), (m, p),
           (p, a), (a, p), (s, t), (p, s), (s, q)]
print(construction_dict_amis(ma_liste))
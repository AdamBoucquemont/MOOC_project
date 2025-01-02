def triple_double_lettres(mot):
   """renvoie vrai si le mot contient trois double lettres consécutives"""

   i = 0
   n = len(mot)
   res = False
   while not res and i < n - 5:
       res = mot[i] == mot[i + 1] and mot[i + 2] == mot[i + 3] \
             and mot[i + 4] == mot[i + 5]
       i += 1
   return res


def n_double_non_consecutifs(mot, n):
   """renvoie vrai si le mot contient n double lettres
      éventuellement non consécutives"""

   i = 0
   long = len(mot)
   cont = 0
   while cont < n and i < long - 1:
       if mot[i] == mot[i + 1]:
           cont += 1
           i += 2
       else:
           i += 1
   return cont == n


def quadruple_double_non_consecutifs(mot):
   """renvoie vrai si le mot contient quatre double lettres
      éventuellement non consécutives"""

   return n_double_non_consecutifs(mot, 4)


# code principal
print("triple-doubles consécutifs avec words.txt")
with open('Section 5/words.txt', encoding="UTF-8") as mots:
    for m in mots:
        mon_mot = m.strip()
        if triple_double_lettres(mon_mot):
            print(mon_mot)

print("triple-doubles consécutifs avec mots.txt")
with open('Section 5/mots.txt', encoding="UTF-8") as mots:
    for m in mots:
        mon_mot = m.strip()
        if triple_double_lettres(mon_mot):
            print(mon_mot)

print("quadruples-doubles non consécutifs avec mots.txt")
with open('Section 5/mots.txt', encoding="UTF-8") as mots:
    for m in mots:
        mon_mot = m.strip()
        if quadruple_double_non_consecutifs(mon_mot):
            print(mon_mot)

print("quadruples-doubles non consécutifs avec words.txt")
with open('Section 5/words.txt', encoding="UTF-8") as mots:
    for m in mots:
        mon_mot = m.strip()
        if quadruple_double_non_consecutifs(mon_mot):
            print(mon_mot)
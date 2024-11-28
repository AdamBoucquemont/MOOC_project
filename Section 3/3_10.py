nb_employe = int(input())
nb_employe_total = nb_entreprise = 0

while nb_employe != -1:
    nb_employe_total += nb_employe
    nb_entreprise += 1
    nb_employe = int(input())
    
print(nb_employe_total/nb_entreprise)
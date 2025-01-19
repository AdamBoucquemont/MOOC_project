def symetrise_amis(d, englobe):
    amis_a_changer = {}
    for personne in d:
        for ami in d[personne]:
            if personne not in d[ami]:
                if ami not in amis_a_changer:
                    amis_a_changer[ami] = set()
                amis_a_changer[ami].add(personne)
                
    for ami_a_modifier, personne_a_changer in amis_a_changer.items():
        for personne in personne_a_changer:
            if englobe:
                d[ami_a_modifier].add(personne)
            else:
                d[personne].remove(ami_a_modifier)
    
d = {'Thierry': {'Michelle', 'Bernadette'},
     'Michelle': {'Thierry'},
     'Bernadette': set()}
symetrise_amis(d, True)
print(d)

d = {'Thierry': {'Michelle', 'Bernadette'},
     'Michelle': {'Thierry'},
     'Bernadette': set()}
symetrise_amis(d, False)
print(d)
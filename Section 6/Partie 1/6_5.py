def construction_dict_amis(list_amis):
    new_list_amis = {}
    for ami1, ami2 in list_amis:
        if ami1 not in new_list_amis:
            new_list_amis[ami1] = {ami2}
        else:
            new_list_amis[ami1].add(ami2)
        if ami2 not in new_list_amis:
            new_list_amis[ami2] = set()
    return new_list_amis
   
list_amis =  [('Quidam', 'Pierre'),
                        ('Thierry', 'Michelle'),
                        ('Thierry', 'Pierre')]
print(construction_dict_amis(list_amis))
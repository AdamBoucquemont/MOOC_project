def store_email(liste_mails):
    dictionnaire = {}
    for email in liste_mails:
        nom, mail = email.split('@')
        if mail not in dictionnaire:
            dictionnaire[mail] = [nom]
        else:
            dictionnaire[mail].append(nom)
    for key, value in dictionnaire.items():
        value = sorted(value)
        dictionnaire[key] = value
    return dictionnaire
        
    
emails = ["ludo@prof.ur", "andre.colon@stud.ulb",
             "thierry@profs.ulb", "sébastien@prof.ur",
             "eric.ramzi@stud.ur", "bernard@profs.ulb",
             "jean@profs.ulb" ]
print(store_email(emails))
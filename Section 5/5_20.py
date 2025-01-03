import re

def nouveaux_heros(histoire_initiale, nouvelle_histoire):
    with  open(histoire_initiale, encoding = "utf-8") as my_file:
        content = my_file.read()
        content = re.sub('Paul', 'Tom', content)
        content = re.sub('Pierre', 'Paul', content)
        content = re.sub('Jacqueline', 'Mathilde', content)
    with open(nouvelle_histoire, 'w', encoding='utf-8') as output_file:
        output_file.write(content)
    
nouveaux_heros("Section 5/histoire_1.txt", "Section 5/nouvelle_histoire_1.txt")
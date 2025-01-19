def top_3_candidats(moyenne):
    top_candidats = []
    for candidat in moyenne:
        top_candidats.append((candidat, moyenne[candidat]))
    top_candidats = sorted(top_candidats, key=lambda x: x[1], reverse= True)
    top_candidats = top_candidats[:3]
    candidats_top_3 = tuple(candidat[0] for candidat in top_candidats)
    return candidats_top_3

# Optimised version : 

# def top_3_candidats(moyennes):
#     return tuple(
#         candidat for candidat, _ in sorted(moyennes.items(), key=lambda x: x[1], reverse=True)[:3]
#     )
    
moyenne = {'Candidat 7': 2, 'Candidat 2': 38, 'Candidat 6': 85,
                 'Candidat 1': 8, 'Candidat 3': 17, 'Candidat 5': 83,
                 'Candidat 4': 33}
print(top_3_candidats(moyenne))
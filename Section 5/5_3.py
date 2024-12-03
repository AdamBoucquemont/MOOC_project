def duree(debut, fin):
    minutes = fin[1] - debut[1]
    heures = 0
    if minutes < 0:
        minutes += 60
        heures -= 1
    heures += fin[0] - debut[0]
    if heures < 0:
        heures += 24
    return (heures, minutes)

print(duree((14, 39), (18, 45)))
print(duree((6, 0), (5, 15)))
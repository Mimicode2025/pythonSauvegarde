table = []
for i in range(1, 11):
    ligne = []
    for j in range(1, 11):
        resultat = i * j
        ligne.append(resultat)
    table.append(ligne)
for ligne in table:
    print(ligne)
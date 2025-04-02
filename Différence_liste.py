#question 6
def difference_listes(liste1, liste2):
    difference = []
    for element in liste1:
        if element not in liste2:
            difference.append(element)
    return difference


L1 = [11, 3, 22, 7, 13, 23, 9]
L2 = [5, 9, 19, 23, 10, 23, 13]

resultat = difference_listes(L1, L2)
print(f"La différence des listes est :{resultat}")

#ou
Premiere_liste = [11, 3, 22, 7, 13, 23, 9]
Deuxieme_liste = [5, 9, 19, 23, 10, 23, 13]
intermadiaire = set(Premiere_liste) - set(Deuxieme_liste)
inter = list(intermadiaire)
print(f"{inter}")

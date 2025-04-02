def difference_listes(liste1, liste2):
    difference = []
    for element in liste1:
        if element not in liste2:
            difference.append(element)
    for element in liste2:
        if element not in liste1:
            difference.append(element)
    return difference

L1 = [11, 3, 22, 7, 13, 23, 9]
L2 = [5, 9, 19, 23, 22, 23, 13]

L3 = difference_listes(L1, L2)
print(L3)

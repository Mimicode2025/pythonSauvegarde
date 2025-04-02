def l_pair(L):
    liste = [element for element in L if element % 2 == 0]
    return liste


def l_impair(L):
    liste = [element for element in L if element % 2 != 0]
    return liste


L = [11, 3, 22, 14, 31, 18, 12, 7]
resultat = (l_pair(L), l_impair(L))
print(resultat)

#ou

L = [11, 3, 22, 14, 31, 18,12 ,7]
listP = []
listIP = []
couple = []
for i in L:
    if i % 2 == 0:
        listP.append(i)

    if i % 2 != 0:
      listIP.append(i)

couple.append(listP)
couple.append(listIP)

print(tuple(couple))
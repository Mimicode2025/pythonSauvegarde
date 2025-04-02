def Somme(liste1):
    somme = 0
    for i in range(len(liste1)):
        somme += liste1[i]
    return somme

def Somme2(liste1):
    somme = 0
    for element in liste1:
        somme += element
    return somme

L1 = [11, 3, 22, 7, 13, 23, 9]

somme1 = Somme(L1)
print(somme1)
somme2 = Somme2(L1)
print(somme2)
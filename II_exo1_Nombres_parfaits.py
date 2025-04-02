def est_parfait(n):
    s = 0
    for i in range(1, n):
        if n % i == 0:
            s += i
    if n == (s / 2):
        return True
    else:
        return False


def liste_de_nombre_strictes(n):
    liste_parfait = []
    for i in range(1, n+1):
        if est_parfait(i):
            liste_parfait.append(n)
    return liste_parfait

while True:
    x = int(input("veillez saisir un nombre stritemenent positif: "))
    if x > 0:
        break

print(f"voici la liste des nombre parfait inferieur a {x} : {liste_de_nombre_strictes(x)}")

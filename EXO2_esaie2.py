# dinamisation du code
def nombre_premier(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


nombre = int(input("veullez saisir un nombre : "))
for i in range(nombre + 1):
    if nombre_premier(i):
        print(i, end=" ,")

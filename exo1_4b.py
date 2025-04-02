print("Table de multiplication de tout les nombre jusqu'au nombre saisie par l'utilisateur par l'utilisateur")
nb = int(input("veillez saisir un nombre:"))
for i in range(1, nb+1):
    for j in range(11):
        print(i, "*", j, "=", i * j)
    print("\n")

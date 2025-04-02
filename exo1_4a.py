print("Table de multiplication d'un nombre saisie par l'utilisateur")
nb = int(input("veillez saisir un nombre:"))
for i in range(1, nb+1):
    print(nb, "*", i, "=", nb * i)

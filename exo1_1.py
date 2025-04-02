print("somme des nombre paire ")
nombre = int(input("veillez saisir un nombre: "))
somme = 0
for i in range(2, nombre, 2):
    somme = somme + i
print(somme)

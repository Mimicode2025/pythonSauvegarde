print("les nombre premier")
nombre = int(input("veullez saisir un nombre :"))
if nombre == 2 or nombre == 3:
    print(nombre)
elif nombre < 2 or nombre % 2 == 0:
    print("le nombre n'est pas premier")
else:
    for i in range(3, int(nombre**0.5) + 1, 2):
        if nombre / i == 0:
            print("le nombre n'est pas premier")
        else:
            print(nombre, end="")


def factoriel(n):
    if n == 0:
        return 1
    else:
        return n * factoriel(n - 1)


n = int(input("veillez saisir un nombre: "))
print(factoriel(n))
s = 0
for i in range(n+1):
    s = s + factoriel(i)
print(f"la somme des factoriel: {s} ")

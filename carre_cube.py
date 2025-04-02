# question 2
list = []
for i in range(20, 41):
    list.append(i)
carre = [n**2 for n in list]
cube = [n**3 for n in list]
print(f"le carre des nombre de 20 a 40 : {carre}")
print(f"le carre des nombre de 20 a 40 : {cube}")

# question 1
list1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
list2 = ["Janvier", "Fevier", "Mars", "Avril", "Mai", "juin", "Juillet", "Aout", "Octabre", "Septembre", "Novembre ", "Decembre"]
intermadiaire = []
for couple in zip(list2, list1):
        intermadiaire += (list(couple))
print(intermadiaire)
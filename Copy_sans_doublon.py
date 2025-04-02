#question 5
l1 = [9, 8, 5, 5, 5, 6, 3, 4, 1, 2, 1, 8, 7]
l2 = []
for element in l1:
    if l1.count(element) == 1:
        l2.append(element)
l2.sort() # croissant
l2.sort(reverse=True) # décroissante
# fonction sorted() pour ranger dans l.ordre crroissante et decroissante
# fonction copy() pour copie des liste
# fonction set pour elimine les doublont
print(l2)
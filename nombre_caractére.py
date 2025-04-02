#question 4
list = ['Jean-Michel', 'Marc', 'Vanessa', 'Anne', 'Maximilien', 'Alexandre-Benoit', 'Louise']
longueur = []
for i in range(len(list)):
    longueur.append(list[i])
    longueur.append(len(list[i]))

print(f'la nouvelle liste est {longueur}')
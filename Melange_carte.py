from random import shuffle

couleurs = ["Pique", "Trefle", "Carreau", "Coeur"]
valeurs = [2, 3, 4, 5, 6, 7, 8, 9, 10, "valet", "dame", "roi", "as"]
cartes = []
for i in valeurs:
    for j in couleurs:
        carte = (i, j)
        cartes.append(carte)
shuffle(cartes)

joueur1 = [cartes[i] for i in range(0, 14)]
joueur2 = [cartes[i] for i in range(14, 27)]
joueur3 = [cartes[i] for i in range(27, 40)]
joueur4 = [cartes[i] for i in range(40, 52)]

print(f"voici les cartes des joueur : \n"
      f"joueur1: {joueur1}\n"
      f"joueur2: {joueur2}\n"
      f"joueur3: {joueur3}\n"
      f"joueur4: {joueur4}\n")








Etudiant = []
while True:
    nom = input("veullez entrez votre nom: ")
    prenom = input("veullez entrez votre prenom: ")
    matricule = input("veullez entrez votre numero de matricule: ")
    information = (nom, prenom, matricule)
    Etudiant.append(information)
    verification = input("voulez vous continez ?: ")
    if verification.upper() == "FIN":
        break
#Affichage des etudiant
for information in Etudiant:
    print(f"le nom de l'etudiant est {information[0].upper()} le prenom est {information[1]} son numéro de maticule est {information[2]}\n")
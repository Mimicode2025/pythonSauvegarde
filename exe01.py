gpa = float(input("veullez saisir la moyenne générale : "))
score = int(input("veullez saisir le score du text d'aptitude : "))
heures = int(input("veullez saisir l'heure de service : "))
if gpa >= 3.0 and 85 <= score <= 115 and heures <= 50:
    print("Felicitation, Vous etes admis")
else:
    print("Désole, Vous n'estes pas admis")

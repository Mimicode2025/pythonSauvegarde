age = int(input("veullez saisir votre age : "))
etudiant = input("Etes vous etudiant ? (oui/non): ")
premium = input("Voullez vous un siege premium ? (oui/non): ")
heure = int(input("veullez saisir l'heure de seance choisie : "))
prix_total = 0
if age < 12:
    print("le film vous est interdit ")
else:
    if heure < 12:
        prix_total = 4000
    else:
        prix_total = 5000
    if etudiant == "oui":
        prix_total -= 1500
    elif heure > 20 and premium == "oui":
        prix_total += 1000

print(f"le prix final de votre billet est de {prix_total:.2f} francs. ")

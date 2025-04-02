Etudiant_list = []
while True:
    Etudiant_dictionnaire = {}
    nom = input("veuillez saisir le nom: ")
    prenom = input("veuillez saisir le prenom: ")
    numero = input("veuillez saisir le numero de matricule : ")
    Etudiant_dictionnaire[nom] = (nom, prenom, numero)
    Etudiant_list.append(Etudiant_dictionnaire)
    verification = input("Voulez-vous continuer ? Tapez 'FIN' pour arrêter : ")
    if verification.upper() == "FIN":
        break
# Affichage de tous les etudiant
print("Affichage des etudiants")
for etudiant in Etudiant_list:
    for cles, valeur in etudiant.items():
        print(f"""
            le nom de l'etudiant est {valeur[0]}
            le prenom de l'etudiant est {valeur[1]}
            le numero de matricule est {valeur[2]}
        """)
# Affichage de l'etudiant kate
for etudiant in Etudiant_list:
    if "kate" in etudiant:
        print(f"les information de l'etudiant kate sont:{etudiant["kate"]}")

# Affichage de l'etudiant dont la matricule = 12345678
for etudiant in Etudiant_list:
    for cles, valeur in etudiant.items():
        if "12345678" in valeur:
            print(f"les information de l'etudiant avec le matricule 12345678 est : {valeur}")
#Modification du programme


















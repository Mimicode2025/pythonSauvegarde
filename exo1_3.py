print("Nombre d'occurences d'une lettre")
chaine = input("Veuillez saisir une chaîne de caractères : ")
lettre = input("veuillez saisir la lettre que vous voulez enter:")
"""fois = 0
caractere = 0
for caractere in chaine:
    if caractere == lettre:
        fois += 1
print(f"Le nombre occurence de {lettre} est : {fois}")"""

print(f"Le nombre occurence de {lettre} est : {chaine.count(lettre)}")

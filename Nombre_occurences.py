chaine = "je suis une codeuse profesionnel"
occurence = {}
for lettre in chaine:
    nombre = 0
    if lettre in occurence.values():
        nombre += 1
    else:
        occurence["lettre"] = nombre

for cles, valeur in occurence.items():
    print(f"{cles}: {valeur} fois ")






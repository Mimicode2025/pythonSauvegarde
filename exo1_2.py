phrase = input('Veuillez entrer une phrase: ')
voyelle = 0
consonne = 0
for caractere in phrase:
    if caractere in "aoiuey":
        voyelle += 1
    elif caractere in "qwrtpsdfghjklzxcvbnm":
        consonne += 1
print(f"La phrase comporte {voyelle} Voyelles et  {consonne} consonnes")

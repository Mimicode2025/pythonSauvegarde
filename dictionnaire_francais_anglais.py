fr_en = {"Bonjour": "Hello", "chat": "cat",  "Homme": "men", "Femme": "women"}
fr_en["cerveau"] = "brain"
if "cerveau" in fr_en:
    print(f"la traduction de cerveau est: {fr_en["cerveau"]}")
for cles in fr_en.keys():
    print(f"cles du dictionnaire est : {cles}")
en_fr ={}
for cles, valeur in fr_en.items():
    en_fr[valeur] = cles
print(en_fr)
if "brain" in en_fr:
    print(f"la traduction de brain est: {en_fr["brain"]}")
for cles, valeur in en_fr.items():
    if valeur == "cerveau": #if "cerveau" in valeur:
        print(f"la cles correspondant au mot cerveau est: {cles}")
for cles, valeur in en_fr.items():
    print(f"la cles {cles} a la valeur {valeur}")
fr_en_2 = {"Homme": ["men", "man"], "femme": ["woman", "girl"]}
fr_en_2["chemin"] = ["path", "way"]
del fr_en_2["chemin"]
print(f"{fr_en_2}")

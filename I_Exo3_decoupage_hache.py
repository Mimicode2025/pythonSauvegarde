def coupe_chaine(chaine, indice):
    liste = []
    if len(chaine) <= indice:
        return None
    else:
        liste.append(chaine[:indice])
        liste.append(chaine[indice:])
        return liste


print(coupe_chaine("moukarama", 3))


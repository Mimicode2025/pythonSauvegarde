def genere_nom(prefixes, suffixes):
    liste = []
    for i in prefixes:
        liste.append(i + suffixes)
    return liste


print(genere_nom("JKLMNOPQ", "ack"))
3
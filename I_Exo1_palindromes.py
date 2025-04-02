def est_palindrome(chaine):
    """ Vérifie si une chaîne est un palindrome """
    # Vérifier si la chaîne est égale à son inverse
    if chaine == chaine[::-1]:
        return f"La chaîne '{chaine}' est un palindrome"
    else:
        return f"La chaîne '{chaine}' n'est pas un palindrome"

print(f"tester les palindromes")
print(est_palindrome("madam"))
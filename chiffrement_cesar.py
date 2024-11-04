def chiffrement_cesar(texte, decalage):
    resultat = ""
    for caractere in texte:
        # Vérifie si le caractère est une lettre majuscule
        if 'A' <= caractere <= 'Z':
            resultat += chr((ord(caractere) - ord('A') + decalage) % 26 + ord('A'))
        # Vérifie si le caractère est une lettre minuscule
        elif 'a' <= caractere <= 'z':
            resultat += chr((ord(caractere) - ord('a') + decalage) % 26 + ord('a'))
        else:
            # Si ce n'est pas une lettre, on laisse le caractère inchangé
            resultat += caractere
    return resultat

def dechiffrement_cesar(texte, decalage):
    return chiffrement_cesar(texte, -decalage)

# Exemple d'utilisation
texte = "Bonjour tout le monde!"
decalage = 3
texte_crypte = chiffrement_cesar(texte, decalage)
texte_decrypte = dechiffrement_cesar(texte_crypte, decalage)

print("Texte original : ", texte)
print("Texte chiffré  : ", texte_crypte)
print("Texte déchiffré: ", texte_decrypte)

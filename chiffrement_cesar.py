#chiffrement_céssar_v2 
def chiffrement_cesar(texte, decalage):
    resultat = ""
   
    for caractere in texte:
        if 'A' <= caractere <= 'Z':
            resultat += chr((ord(caractere) - ord('A') + decalage) % 26 + ord('A'))
        elif 'a' <= caractere <= 'z':
            resultat += chr((ord(caractere) - ord('a') + decalage) % 26 + ord('a'))
        elif '0' <= caractere <= '9':
            resultat += chr((ord(caractere) - ord('0') + decalage) % 10 + ord('0'))
        else:
            resultat += caractere
    return resultat

def dechiffrement_cesar(texte, decalage):
    return chiffrement_cesar(texte, -decalage)

texte = "zonjour yanis123"
decalage = 3
texte_crypte = chiffrement_cesar(texte, decalage)
texte_decrypte = dechiffrement_cesar(texte_crypte, decalage)

print("Texte original : ", texte)
print("Texte chiffré  : ", texte_crypte)
print("Texte déchiffré: ", texte_decrypte)

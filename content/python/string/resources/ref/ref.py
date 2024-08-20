# Mission 1 : Voyelles et consonnes
# `for`, `in`

texte = "Il est 7h je me lève le matin. Je prends ma douche, je descends l'escalier. Je prends mon bol, je mange mes céréales. Je dois tout boire mais le temps passe vite. Tic tac, tout le monde se presse. Je descends à l'arêt du bus. Je dois prendre mon bus, je vois mes amis ! Sauter sur le siège avant, sauter sur le siège arrière. Il faut que je choisisse quel siège faut-il prendre. C'est vendredi, on fête le vendredi-i. Tout le monde est impatient d'être au week-end. C'est vendredi, fun-fun c'est vendredi-i. Tout le monde est impatient d'être au week-end. On fait la fête, fait la fête (ouais) ! Fait la fête, fait la fête (ouais) ! Fun-fun-fun-fun (chouette) ! On a hâte d'être au week-end."

consonnes = 0
voyelles = 0
symboles = 0

for c in texte:
    if c in "aeiouyAEIOUY":
        voyelles += 1
    elif c in "bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ":
        consonnes += 1
    else:
        symboles += 1

print("Il y a", consonnes, "consonnes,", voyelles, "voyelles et", symboles, "symboles !")

# Mission 2 : Message à l'envers
# `for`, index

phrase = "! serueirépus zeyos ,edia ertov ed nioseb ia’j ,iom zevuorter ,serèirutnevA"
resultat = ""
longueur = len(phrase)

for i in range(longueur):
    resultat += phrase[longueur - 1 - i]

print(resultat)

# Mission 3 : La liste de mots
# compare

liste1 = ["gdklnnfqlp", "fapeakodng", "bniujfkg", "fidoxmropz", "hgifudkml", "jgiofdkngp"]
liste2 = ["cndiogfnle", "fapeakzdng", "bnigjkfg", "mjiogndfea", "hgifuckml", "jgiofdkngp"]

code = []
longueur = len(liste1)

for i in range(longueur):
    code.append(liste1[i] > liste2[i])

print(code)

# Mission 4 : Retrouver le caractère
# `chr`

nombre_binaire = ""

for c in code:
    if c:
        nombre_binaire += '1'
    else:
        nombre_binaire += '0'

code_ascii = int(nombre_binaire, 2)
print(chr(code_ascii))

# Mission 5 : Un message secret !

texte_cache = ['    \t \n\tL41553Z    ', '    \n\n\nM01 ', 'v0Y5     \n\t', '\n\n\n\nGY1D3r\t    ', '            v3r5           ', '\n         c3     \t', '\t   p3R1pl3 ', '     V0Y5\n\n', '   \n\t    \nm3n4nt    \n       \t     \n', ' \n      \td4N5    \n    ', '     \t    \n  Yn  \t\n\n', '\t\t\t\tm0Nd3    \n   ', '     \nm4Gn1F1QY3', '!']

longueur = len(texte_cache)

for i in range(longueur):
    texte_cache[i] = texte_cache[i].strip()
    texte_cache[i] = texte_cache[i].lower()

    texte_cache[i] = texte_cache[i].replace('4', 'a')
    texte_cache[i] = texte_cache[i].replace('3', 'e')
    texte_cache[i] = texte_cache[i].replace('1', 'i')
    texte_cache[i] = texte_cache[i].replace('0', 'o')
    texte_cache[i] = texte_cache[i].replace('5', 's')
    texte_cache[i] = texte_cache[i].replace('y', 'u')

texte = " ".join(texte_cache)
print(texte)

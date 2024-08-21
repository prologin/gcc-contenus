# Mission 1 : On part pour l'aventure !
# index

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
caracteres = ['!', '?', '.', ',', ':', ';']

print(alphabet[6], alphabet[2], alphabet[2], caracteres[0], sep="")

# Mission 2 : Le sac de Julie 
# index

sac = ["Bonjour le monde !", False, 21, False, "Bouteille d'eau", False, 3.14]

print(sac)
sac[2] *= 2
sac[0] = "Hello World!"
sac[1] = True
sac[3] = True
sac[5] = True
sac[6] = "pi"
print(sac)

# Mission 3 : Préparation de la valise
# `append`

valise_julie = ["t-shirts", "pantalons"]

print(valise_julie)
valise_julie.append("tongs")
valise_julie.append("casquette")
print(valise_julie)

# Mission 4 : Entrée et liste
# `input`

article = input("Que voulez-vous commander ?")
valise_julie.append(article)

# Mission 5 : C'est maintenant au tour de ta valise !
# `for`

ma_valise = []

for i in range(6):
    article = input("Que dois-je rajouter ?")
    ma_valise.append(article)
    print(ma_valise)

# Mission 6 : Planning des vacances
# `insert`

planning = ["Voyage aller", "Présentation des GCC!", "Restaurant", "Voyage retour"]

planning.insert(3, "Balade en ville")
planning.insert(1, "Plage")
planning.insert(3, "Glace")
print(planning)

# Mission 7 : Les problèmes commencent...
# `pop`

valise = ["casquette", "t-shirts", "pantalons", "doudou", "crème solaire", "tongs", "parapluie"]

valise.pop()
valise.pop(4)
valise.pop(0)
print(valise)

# Mission 8 : C'est l'heure du goûter !
# `remove`

sac_gouter = ["kouign-amann", "croissant", "pain au chocolat", "tarte à la pomme"]

sac_gouter.remove("kouign-amann")
sac_gouter.remove("pain au chocolat")
print(sac_gouter)

# Mission 9 : Trier les bonbons !
# `for`

carton_bonbons = ["Schtroumpf", "Tagada", "Pompote", "Smarties", "Smarties", "Pompote", "Kinder", "Schtroumpf", "Kinder", "Prolobonbons", "Tagada", "Pompote", "Prolobonbons", "Pompote", "Schtroumpf", "Crocodiles", "Smarties", "Prolobonbons", "Prolobonbons", "Prolobonbons", "Smarties", "Schtroumpf", "Prolobonbons", "Crocodiles", "Tagada", "Pompote", "Crocodiles", "Smarties", "Kinder", "Prolobonbons", "Pompote", "Smarties", "Pompote", "Kinder", "Crocodiles", "Tagada", "Pompote", "Kinder", "Pompote", "Kinder", "Kinder", "Kinder", "Kinder", "Kinder", "Schtroumpf", "Kinder", "Schtroumpf", "Pompote", "Prolobonbons", "Pompote"]

indices = []

for i in range(len(carton_bonbons)):
    if carton_bonbons[i] == "Prolobonbons":
        indices.append(i)

print(indices)

# Mission 10 : Embarquement :
# `for`

passagers = ["Ada Lovelace", "Grace Hopper", "Jean Bartik", "Katherine Johnson", "Margaret Hamilton", "Radia Perlman", "Carol Shaw", "Suzane Kare", "Hedy Lamarr", "Katie Bouman"]

for p in passagers:
    print("Passager", p, "est appelé !")

# Mission 11 : Dernières vérifications !
# `in`, `+`

valise = ["t-shirt", "pantalon", "pull", "chaussette"]
sac = ["passeport", "ordinateur", "micro:bit", "souris", "bouteille d'eau", "crème solaire", "lunettes de soleil", "gâteaux"]

affaires = valise + sac
verifications = ["bouteille d'eau", "éventail", "lunettes de soleil", "casquette", "tongs"]

for e in verifications:
    if e in affaires:
        print(e, "est présent !")
    else:
        print("Il manque", e, "!")

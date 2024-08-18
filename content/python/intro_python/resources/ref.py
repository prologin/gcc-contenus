# Mission 1 : Affiche ton prénom !
# `print`

print("Julie")
print(20)

# Mission 2 : Téléportation !
# `input`

input("Dans quelle ville suis-je tombée ?")

# Mission 3 : Argent de poche
# variables, operations

piece_or = 6
piece_argent = 3
piece_bronze = 10

porte_monnaie = piece_or * 5.12 + piece_argent * 3.25 + piece_bronze * 1.64
print("Le porte-monnaie équivaut à", porte_monnaie, "€")

# Mission 4 : Le menu
# conditions

prix_plat = 3.99 + 9.99 + 5.49

if prix_plat <= porte_monnaie:
    print("J'ai faim, allons-y !")
else:
    print("Je n'ai pas assez d'argent...")

# Mission 5 : Dessert, dessert...
# `while`

porte_monnaie = 37.40
tiramisu = 5.49

while porte_monnaie - tiramisu > 0:
    print("Un autre tiramisu s'il vous plaît !")
    porte_monnaie -= tiramisu

print("Merci chef !")

# Mission 6 : Le long périple...
# `for`

x = 0
y = 0

for i in range(7):
    x += 3
    y += 2
    print("Kawabounga !")

print("x =", x)
print("y =", y)

# Mission 7 : Trésor caché !
# functions

def creuser(nom):
    print("Brothers of the mine rejoice!")
    print("Swing, swing, swing with me")
    print("Raise your pick and raise your voice!")
    print("Sing, sing, sing with me")
    print("I am a dwarf and I’m digging a hole")
    print("Diggy diggy hole, diggy diggy hole")
    print("Come", nom, "and sing with me!")

creuser("Julie")
creuser("Julie")
creuser("Joseph")

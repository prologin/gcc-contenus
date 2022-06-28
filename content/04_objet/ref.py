red = "\033[0;31m"
blue = "\033[0;34m"
reset = "\033[0m"

class Pokemon:
    def __init__(self, name, hp, dmg, lvl):
        self.name = name
        self.hp = hp
        self.dmg = dmg
        self.lvl = lvl

    def status(self):
        print("" + self.name + " [lvl. " + str(self.lvl) + "]\
        \nHP : " + str(self.hp) + " | Dmg : " + str(self.dmg))

    def attack(self, target):
        target.hp-= self.dmg
        #self.status()

def combat(poke1, poke2):
    while poke1.hp > 0 and poke2.hp > 0:
        poke1.attack(poke2)
        poke2.attack(poke1)
    if poke1.hp > poke2.hp:
        print(red + poke1.name + " wins!" + reset)
        return (0, 1)
    elif poke1.hp < poke2.hp:
        print(blue + poke2.name + " wins!" + reset)
        return (1, 0)
    else:
        print("Tied!")
        return (1, 1)

class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemons = []

    def catch(self, target):
        self.pokemons.append(target)

def duel(trainer1, trainer2):
    i, j = 0, 0
    while i < len(trainer1.pokemons) and j < len(trainer2.pokemons):
        result = combat(trainer1.pokemons[i], trainer2.pokemons[j])
        i += result[0]
        j += result[1]
    if i >= len(trainer1.pokemons):
        if j >= len(trainer2.pokemons):
            print("Tied!")
        else:
            print(blue + trainer2.name + " wins!" + reset)
    else:
        print(red + trainer1.name + " wins!" + reset)

'''
main
'''
Amelie = Trainer("Amelie")
Tanguy = Trainer("Tanguy")
Amelie.catch(Pokemon("Pikachu", 50, 10, 11))
Amelie.catch(Pokemon("Dracolosse", 150, 42, 50))
Tanguy.catch(Pokemon("Tiplouf", 42, 8, 4))
Tanguy.catch(Pokemon("Mew", 69, 69, 69))
duel(Amelie, Tanguy)

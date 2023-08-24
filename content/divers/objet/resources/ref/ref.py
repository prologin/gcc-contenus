from __future__ import annotations
import random


class Pokemon:
    def __init__(self, nom, vie, degats):
        self.nom = nom
        self.vie = vie
        self.vie_max = vie  # utile pour la partie PokeCenter
        self.degats = degats

    def affiche_infos(self):
        print(f"{self.nom}\nVie : {self.vie} | Attaque : {self.degats}")

    def attaque(self, pokemon_adv: Pokemon):
        pokemon_adv.vie -= self.degats
        print(f"{self.nom} attaque {pokemon_adv.nom}.")

    def __str__(self) -> str:
        return self.nom

def combat(poke1: Pokemon, poke2: Pokemon):
    while poke1.vie > 0 and poke2.vie > 0:
        poke1.attaque(poke2)
        if poke2.vie > 0:
            poke2.attaque(poke1)

    if poke1.vie > poke2.vie:
        print(f"{poke2.nom} est KO, {poke1.nom} a gagné !")
        return 1
    else:
        print(f"{poke1.nom} est KO, {poke2.nom} a gagné !")
        return 2


class Dresseur:
    def __init__(self, nom):
        self.nom = nom
        self.pokemons : list[Pokemon] = []

    def capture(self, pokemon: Pokemon):
        self.pokemons.append(pokemon)

    def combat(self, pokemon_adv: Pokemon):
        i = 0
        while pokemon_adv.vie > 0 and i < len(self.pokemons):
            combat(self.pokemons[i], pokemon_adv)
            i += 1

        if pokemon_adv.vie > 0:
            print(f"Vous avez perdu contre {pokemon_adv.nom}...")
        else:
            print(f"Vous avez gagné contre {pokemon_adv.nom} !")

    def combat_interactif(self, pokemon_adv: Pokemon):
        pokemon_en_vie = len(self.pokemons)
        while pokemon_en_vie > 0 and pokemon_adv.vie > 0:
            print(f"Vous avez les Pokemons :")
            for i in range(len(self.pokemons)):
                if self.pokemons[i].vie > 0:
                    print(f"{i} {self.pokemons[i].nom}")
            num_pokemon = int(input("Quel Pokemon envoyer ? "))
            mon_pokemon = self.pokemons[num_pokemon]

            resultat = combat(mon_pokemon, pokemon_adv)
            if resultat != 1:
                pokemon_en_vie -= 1

        if pokemon_en_vie == 0:
            print("Vous n'avez plus de Pokémon en vie, vous avez perdu")
        else:
            print(f"Vous avez battu le {pokemon_adv.nom} sauvage. Félicitations !")

    def duel_interactif(self, dresseur_adv: Dresseur):
        pokemon_en_vie = len(self.pokemons)
        indice_pok_adv = 0
        while indice_pok_adv < len(dresseur_adv.pokemons) and pokemon_en_vie > 0:
            pokemon_adv = dresseur_adv.pokemons[indice_pok_adv]
            print(f"{dresseur_adv.nom} envoie {pokemon_adv.nom}")

            print(f"Vous avez les Pokémon :")
            for i, pokemon in enumerate(self.pokemons):
                if pokemon.vie > 0:
                    print(f"{i} {pokemon.nom}")
            num_pokemon = int(input("Quel Pokémon envoyer ? "))
            mon_pokemon = self.pokemons[num_pokemon]

            resultat = combat(mon_pokemon, pokemon_adv)
            if resultat != 1:
                pokemon_en_vie -= 1
            if resultat != 2:
                indice_pok_adv += 1

        if pokemon_en_vie == 0:
            print("Vous n'avez plus de Pokémon en vie, vous avez perdu")
        else:
            print(f"Vous avez battu le dresseur {dresseur_adv.nom}. Félicitations !")

    def pokemon_en_vie(self):
        nb = 0
        for pokemon in self.pokemons:
            if pokemon.vie > 0:
                nb += 1
        return nb


def duel_auto(dresseur1: Dresseur, dresseur2: Dresseur):
    i, j = 0, 0
    while i < len(dresseur1.pokemons) and j < len(dresseur2.pokemons):
        result = combat(dresseur1.pokemons[i], dresseur2.pokemons[j])
        if result != 1:
            i += 1
        if result != 2:
            j += 1

    if i >= len(dresseur1.pokemons):
        print(f"{dresseur2.nom} a gagné !")
    else:
        print(f"{dresseur1.nom} a gagné !")


def visite_PokeCenter(dresseur: Dresseur, quiet=False):
    print("Bienvenue au centre Pokémon. Nous pouvons soigner vos Pokémon.")

    if quiet or input("Voulez-vous les soigner ? 'oui' / 'non'\n") == "oui":
        print("Un instant s'il-vous-plait.")
        for pokemon in dresseur.pokemons:
            pokemon.vie = pokemon.vie_max

        print("Merci d'avoir attendu. Vos Pokémon sont en super forme.")

    print("À une prochaine fois peut-être.")


'''
main
'''
#Amelie = Dresseur("Amélie")
#Tanguy = Dresseur("Tanguy")
#Amelie.capture(Pokemon("Pikachu", 50, 10))
#Amelie.capture(Pokemon("Dracolosse", 150, 42))
#Tanguy.capture(Pokemon("Tiplouf", 42, 8))
#Tanguy.capture(Pokemon("Mew", 69, 69))
#duel_auto(Amelie, Tanguy)

fin = False

print("Cher nouveau dresseur, bienvenue dans le monde Pokémon !")
nom = input("Comment t'appelles-tu ?\n")
moi = Dresseur(nom)

print("Choisis ton Pokémon de départ :")
nom_pokemon = input("Comment s'appelle-t-il ?\n")
moi.capture(Pokemon(nom_pokemon, 40, 12))
print(f"Félicitations pour avoir choisi {nom_pokemon} !\n")

while not fin:
    print("Que souhaites-tu faire :")
    choix = input("'voyager', aller au 'pokecenter', ou 'quitter' ?\n")
    if choix == "voyager":
        rencontre = random.randint(1,2)

        if rencontre == 1: # Pokemon
            pokemon_sauvage = Pokemon("toto", 20, 8)
            print(f"Un {pokemon_sauvage.nom} sauvage apparaît !")

            choix2 = input("Souhaites-tu le 'capturer', se 'battre' ou 'fuire' ?\n")
            if choix2 == "capturer":
                moi.capture(pokemon_sauvage)
                print(f"Tu as capturé {pokemon_sauvage.nom} !")
            elif choix2 == "battre":
                moi.combat_interactif(pokemon_sauvage)
            else:
                print("Tu as pris la fuite...")

        else: # Dresseur
            dresseur = Dresseur("Team Rocket")
            dresseur.capture(Pokemon("poke1", 20, 9))
            dresseur.capture(Pokemon("poke2", 30, 10))
            print(f"Dresseur {dresseur.nom} veut se battre !")

            battu = False
            while not battu:
                choix2 = input("Souhaites-tu le battre en 'auto' ou en 'interactif' ?\n")
                if choix2 == "auto":
                    duel_auto(moi, dresseur)
                    battu = True
                elif choix2 == "interactif":
                    moi.duel_interactif(dresseur)
                    battu = True
                else:
                    print("Je n'ai pas compris.")

        if moi.pokemon_en_vie() == 0:
            print("Tu cours vers un centre Pokémon pour soigner tes Pokemon")
            visite_PokeCenter(moi, True)

    elif choix == "pokecenter":
        visite_PokeCenter(moi)
    elif choix == "quitter":
        fin = True
    else:
        print("Je n'ai pas compris ce que tu voulais faire.")

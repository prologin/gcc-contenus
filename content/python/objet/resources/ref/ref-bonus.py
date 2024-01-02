from __future__ import annotations
import random

red = "\033[0;31m"
green = "\033[0;32m"
blue = "\033[0;34m"
light_magenta = "\033[0;95m"
reset = "\033[0m"

class Pokemon:
    def __init__(self, nom, vie, degats, vitesse, lvl):
        self.nom = nom
        self.vie = vie
        self.vie_max = vie  # utile pour la partie PokeCenter
        self.degats = degats
        self.vitesse = vitesse
        self.xp = 0
        self.lvl = lvl

    def affiche_infos(self):
        print(f"{light_magenta}{self.nom}{reset}\
              \n  Vie : {self.vie}/{self.vie_max} | Attaque : {self.degats} | Vitesse : {self.vitesse} | XP : {self.xp} | Niveau : {self.lvl}")

    def attaque(self, pokemon_adv: Pokemon):
        pokemon_adv.vie = max(0, pokemon_adv.vie - self.degats)
        print(f"{self.nom} attaque {pokemon_adv.nom}.")

    def level_up(self):
        self.lvl += 1
        self.xp = 0
        self.vie_max += self.lvl
        self.vie += self.lvl
        self.vitesse += 2
        self.degats += 2
        print(f"{green}Félicitations ! {self.nom} vient de gagner un niveau, il est au lvl {self.lvl}.{reset}")

    def __str__(self) -> str:
        return self.nom


def combat(poke1: Pokemon, poke2: Pokemon):
    p1 = poke1 if poke1.vitesse > poke2.vitesse else poke2
    p2 = poke1 if poke1.vitesse <= poke2.vitesse else poke2

    while poke1.vie > 0 and poke2.vie > 0:
        p1.attaque(p2)
        if p2.vie > 0:
            p2.attaque(p1)

    if poke1.vie > poke2.vie:
        print(f"{poke2.nom} est KO, {blue}{poke1.nom} a gagné !{reset}")
        poke1.xp += poke2.vie_max
        if poke1.xp > 100:
            poke1.level_up()
        return 1
    else:
        print(f"{poke1.nom} est KO, {red}{poke2.nom} a gagné !{reset}")
        return 2


class Dresseur:
    def __init__(self, nom, argent):
        self.nom = nom
        self.pokemons : list[Pokemon] = []
        self.potions = 2
        self.argent = argent

    def capture(self, pokemon: Pokemon):
        self.pokemons.append(pokemon)

    def combat_interactif(self, pokemon_adv: Pokemon):
        pokemon_en_vie = len(self.pokemons)
        while pokemon_en_vie > 0 and pokemon_adv.vie > 0:
            print(f"Vous avez les Pokemons :")
            for i, pokemon in enumerate(self.pokemons):
                print(f"{i} {pokemon.nom}")
            num_pokemon = int(input("Quel Pokemon envoyer ? "))
            mon_pokemon = self.pokemons[int(num_pokemon)]

            resultat = combat(mon_pokemon, pokemon_adv)
            if resultat != 1:
                pokemon_en_vie -= 1

        if pokemon_en_vie == 0:
            print(f"{red}Vous n'avez plus de Pokemon en vie, vous avez perdu.{reset}")
        else:
            print(f"{green}Vous avez battu le {pokemon_adv.nom} sauvage.{reset}")

    def duel_interactif(self, dresseur_adv: Dresseur):
        pokemon_en_vie = len(self.pokemons)
        indice_pok_adv = 0
        while indice_pok_adv < len(dresseur_adv.pokemons) and pokemon_en_vie > 0:
            pokemon_adv = dresseur_adv.pokemons[indice_pok_adv]
            print(f"{dresseur_adv.nom} envoie {pokemon_adv.nom}")

            print(f"Vous avez les Pokemons :")
            for i, pokemon in enumerate(self.pokemons):
                print(f"{i} {pokemon.nom}")
            num_pokemon = int(input("Quel Pokemon envoyer ? "))
            mon_pokemon = self.pokemons[int(num_pokemon)]

            resultat = combat(mon_pokemon, pokemon_adv)
            if resultat != 1:
                pokemon_en_vie -= 1
            if resultat != 2:
                indice_pok_adv += 1

        if pokemon_en_vie == 0:
            print(f"{red}Vous n'avez plus de Pokemon en vie, vous avez perdu{reset}")
            return False
        else:
            print(f"{green}Vous avez battu le dresseur {dresseur_adv.nom}. Félicitations !{reset}")
            return True

    def pokemon_en_vie(self):
        nb = 0
        for pokemon in self.pokemons:
            if pokemon.vie > 0:
                nb += 1
        return nb
    
    def affiche_stats(self):
        print("Les statistiques des Pokemons:")
        for pokemon in self.pokemons:
            pokemon.affiche_infos()

    def utilise_potion(self, num_pokemon):
        mon_pokemon = self.pokemons[int(num_pokemon)]
        mon_pokemon.vie = min(mon_pokemon.vie + 20, mon_pokemon.vie_max)
        self.potions -= 1
        print(f"{green}{mon_pokemon.nom} est revigoré !{reset}")


def duel_auto(dresseur1: Dresseur, dresseur2: Dresseur):
    i, j = 0, 0
    while i < len(dresseur1.pokemons) and j < len(dresseur2.pokemons):
        result = combat(dresseur1.pokemons[i], dresseur2.pokemons[j])
        if result != 1:
            i += 1
        if result != 2:
            j += 1

    if i >= len(dresseur1.pokemons):
        print(f"{red}{dresseur2.nom} a gagné !{reset}")
        return False
    else:
        print(f"{blue}{dresseur1.nom} a gagné !{reset}")
        return True


def visite_PokeCenter(dresseur: Dresseur, quiet=False):
    print("Bienvenue au centre Pokemon. Nous pouvons soigner vos Pokemons")

    if quiet or input("Voulez-vous les soigner ? 'oui' / 'non'\n") == "oui":
        for pokemon in dresseur.pokemons:
            pokemon.vie = pokemon.vie_max

        print(f"Un instant s'il-vous-plait.\
              \nMerci d'avoir attendu. {green}Vos Pokemons sont en super forme.{reset}")

    print("À une prochaine fois peut-être.")


def visite_shop(dresseur: Dresseur):
    print("Bienvenue au shop Pokemon.")
    potion = ("potion", 100)
    items = f"- '{potion[0]}' : {potion[1]}$\n"

    while True:
        choix = input(f"Que souhaitez-vous acheter ? 'quitter' ?\n{items}")
        if choix == potion[0]:
            if dresseur.argent < potion[1]:
                print(f"{red}Vous n'avez pas assez d'argent pour acheter cet objet.{reset}")
            else:
                dresseur.potions += 1
                dresseur.argent -= potion[1]
                print(f"{green}Vous avez acheté '{potion[0]}'. Il vous reste {dresseur.argent}.{reset}")
        elif choix == "quitter":
            break
        else:
            print("Je n'ai pas compris votre demande.")


fin = False

print(f"{green}Cher nouveau dresseur, bienvenue dans le monde Pokemon !{reset}")
nom = input("Comment t'appelles-tu ?\n")
moi = Dresseur(nom, 500)

print()
print("Choisis ton Pokemon de départ:")
nom_pokemon = input("Comment s'appelle-t-il ?\n")
moi.capture(Pokemon(nom_pokemon, 40, 15, 15, 5))
print(f"{green}Félicitations pour avoir choisi {nom_pokemon} !{reset}")

while not fin:
    print()
    print("Que souhaites-tu faire :")
    choix = input("'voyager', aller en 'ville', voir ton 'equipe', ou 'quitter' ?\n")
    if choix == "voyager":
        rencontre = random.randint(1,2)

        if rencontre == 1: # Pokemon
            pokemon_sauvage = Pokemon(f"Pokemon{len(moi.pokemons)}", random.randint(10, 30), random.randint(5, 18), random.randint(5, 18), random.randint(2, 8))
            print(f"{red}Un {pokemon_sauvage.nom} sauvage apparaît !{reset}")

            choix2 = input("Souhaites-tu le 'capturer', 'battre' ou 'fuire' ?\n")
            if choix2 == "capturer":
                moi.capture(pokemon_sauvage)
                print(f"{green}Tu as capturé {pokemon_sauvage.nom} !{reset}")
                choix3 = input("Veux-tu lui donner un nom ? 'oui' / 'non'\n")
                if choix3 == "oui":
                    nom = input("Quel nom veux-tu lui donner ?\n")
                    pokemon_sauvage.nom = nom
                    print(f"{green}Le Pokemon a bien été renommé en {nom}.{reset}")
            elif choix2 == "battre":
                moi.combat_interactif(pokemon_sauvage)
            else:
                print("Tu as pris la fuite...")

        else: # Dresseur
            dresseur = Dresseur("Team Rocket", random.randint(50, 180))
            for i in range(random.randint(1, 3)):
                dresseur.capture(Pokemon(f"poke{i}", random.randint(10, 60), random.randint(5, 30), random.randint(7, 25), random.randint(5, 12)))
            print(f"{red}Dresseur {dresseur.nom} veut se battre !{reset}")

            battu = False
            gagne = False
            while not battu:
                choix2 = input("Souhaites-tu le battre en 'auto' ou en 'interactif' ?\n")
                if choix2 == "auto":
                    gagne = duel_auto(moi, dresseur)
                    battu = True
                elif choix2 == "interactif":
                    gagne = moi.duel_interactif(dresseur)
                    battu = True
                else:
                    print("Je n'ai pas compris.")

            if gagne:
                moi.argent += dresseur.argent
                print(f"{green}Tu as battu {dresseur.nom}, tu gagnes {dresseur.argent}$.{reset}")
            else:
                argent_avant = moi.argent
                moi.argent = max(moi.argent - 150, 0)
                print(f"{red}Tu as perdu contre {dresseur.nom}, tu perds {argent_avant - moi.argent}$.{reset}")

        if moi.pokemon_en_vie() == 0:
            print(f"{red}Tu cours vers un centre Pokemon pour soigner tes Pokemons{reset}")
            visite_PokeCenter(moi, True)

    elif choix == "ville":
        choix2 = input("Souhaites-tu aller au 'pokecenter' ou au 'shop' ?'\n")
        if choix2 == "pokecenter":
            visite_PokeCenter(moi)
        elif choix2 == "shop":
            visite_shop(moi)

    elif choix == "equipe":
        print(f"{green if moi.argent > 0 else red}Tu as {moi.argent}$.{reset}")
        print(f"Tu as {moi.potions} potions.")
        moi.affiche_stats()
        print()
        if moi.potions > 0:
            choix2 = input("Souhaites-tu utiliser une potion ? 'oui' / 'non'\n")
            if choix2 == "oui":
                num_pokemon = int(input("Sur quel Pokemon ?\n"))
                moi.utilise_potion(num_pokemon)

    elif choix == "quitter":
        fin = True

    else:
        print("Je n'ai pas compris ce que tu voulais faire.")

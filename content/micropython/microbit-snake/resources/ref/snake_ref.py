from microbit import *
from random import randint

# Directions
HAUT = 0
DROITE = 1
BAS = 2
GAUCHE = 3

# Taille de l'ecran
TAILLE_ECRAN = 5

# Intensite lumineuse pour la pomme
INTENSITE_POMME = 3
# Intensite lumineuse pour le serpent
INTENSITE_SERPENT = 6


def dessiner_serpent(serpent):
    """
    Dessine le serpent sur l'ecran du micro:bit
    """

    # Affiche la tete avec plus d'intensite
    display.set_pixel(serpent[0][1], serpent[0][0], 9)

    for (i, j) in serpent[1:]:
        display.set_pixel(j, i, INTENSITE_SERPENT)


def nouvelle_direction(direction):
    """
    Choisit la nouvelle direction
    """
    # TODO: Change la direction en fonction des boutons A, B et de la
    # direction donnee

    # Si on appuie sur le bouton A, on tourne a gauche.
    # Si on appuie sur le bouton B, on tourne a droite.
    btn_a = [GAUCHE, HAUT, DROITE, BAS]
    btn_b = [DROITE, BAS, GAUCHE, HAUT]

    if button_a.was_pressed():
        return btn_a[direction]
    elif button_b.was_pressed():
        return btn_b[direction]
    else:
        return direction


def nouvelle_position_tete(serpent, direction):
    """
    Renvoie les coordonnees (x, y) de la nouvelle tete
    """
    # TODO: Choisi une nouvelle direction en fonction de la direction donnee
    # et de la tete
    offsets = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    off = offsets[direction]

    new = ((serpent[0][0] + off[0] + 5) % 5, (serpent[0][1] + off[1] + 5) % 5)
    return new


# La tete du serpent est le premier element de la liste
# La queue est le dernier element
serpent = [(2, 2)]
longueur_serpent = 2
direction = HAUT
pomme = None

# Tant que le serpent ne remplit pas toutes les cases
while longueur_serpent < 25:

    # TODO: Si la pomme n'existe pas (None), choisi une place aleatoire pour
    # la pomme
    while pomme is None:
        (x, y) = (randint(0, TAILLE_ECRAN - 1), randint(0, TAILLE_ECRAN - 1))
        if not (x, y) in serpent:
            pomme = (x, y)

    # TODO: Change la direction
    dir = nouvelle_direction(dir)

    # TODO: Trouve la nouvelle tete du serpent
    head = nouvelle_position_tete(serpent, dir)

    # TODO: Ajoute la nouvelle tete au serpent (insere la tete en position 0)
    serpent.insert(0, head)

    # TODO: Si la nouvelle tete est sur la pomme, agrandit la taille du serpent
    # Et retire la pomme de la grille (None)
    if pomme == head:
        longueur_serpent += 1
        pomme = None

    # TODO: retire la derniere valeur de la queue du serpent si celui-ci
    # est plus grand que longueur_serpent
    if len(serpent) > longueur_serpent:
        serpent.pop()

    # TODO: Si le serpent se mord, c'est perdu, on casse la boucle
    # Ici, on vérifie si la tete du serpent (serpent[0]) existe deja dans son
    # corps (serpent[1:]). Explication dans la section "Astuces" à la fin du TP.
    if serpent[0] in serpent[1:]:
        break

    display.clear()
    # TODO: Affiche la pomme
    # TODO: Affiche le serpent
    if pomme is not None:
        display.set_pixel(pomme[1], pomme[0], INTENSITE_POMME)
    dessiner_serpent(serpent)
    sleep(500)


# TODO: Affiche un message de victoire/defaire en fonction du score
# Le score est la taille du serpent
display.scroll("Score: " + str(longueur_serpent))

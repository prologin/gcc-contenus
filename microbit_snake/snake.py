from microbit import *
from random import randint

# Directions
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

# Taille de l'ecran
screen_size = 5

# Intensite lumineuse pour la pomme
APP_LIGHT = 3


def draw_snake(snake):
    """
    Dessine le serpent sur l'ecran du micro:bit
    """
    # Intensite lumineuse pour le serpent
    SN_LIGHT = 6

    # Affiche la tete avec plus d'intensite
    display.set_pixel(snake[0][1], snake[0][0], 9)

    for (i, j) in snake[1:]:
        display.set_pixel(j, i, SN_LIGHT)


def new_direction(direction):
    """
    Choisis la nouvelle direction
    """
    # TODO: Change la direction en fonction des boutons A, B et de la
    # direction donnee

    # Si on appuie sur le bouton A, on tourne a gauche. (UP->LEFT, RIGHT->UP...)
    # Si on appuie sur le bouton B, on tourne a droite. (UP-> RIGHT, RIGHT->DOWN...)
    pass


def new_head(snake, direction):
    """
    Renvoie les coordonnees (x, y) de la nouvelle tete
    """
    # TODO: Choisi une nouvelle direction en fonction de la direction donnee
    # et de la tete du serpent
    pass


# La tete du serpent est le premier element de la liste
# La queue est le dernier element
snake = [(2, 2)]
snake_len = 2
direction = UP
apple = None

# Tant que le serpent ne rempli pas toutes les cases de l'écran
while snake_len < 25:

    # TODO: Si la pomme n'existe pas (None), choisis une place aleatoire pour
    # la pomme

    # TODO: Change la direction

    # TODO: Trouve la nouvelle tete du serpent

    # TODO: Ajoute la nouvelle tete au serpent (insere la tete en position 0)

    # TODO: Si la nouvelle tete est sur la pomme, agrandis la taille du serpent de 1
    # Et retire la pomme de la grille (None)

    # TODO: retire la derniere valeur de la queue du serpent si celui-ci
    # est plus grand que snake_len

    # TODO: Si le serpent se mord, c'est perdu, on casse la boucle
    if snake[0] in snake[1:]:
        break

    display.clear()
    # TODO: Affiche la pomme si elle existe
    draw_snake(snake)
    sleep(500)


# TODO: Affiche un message de victoire/defaire en fonction du score
# Le score est la taille du serpent
display.scroll("Score: " + str(snake_len))

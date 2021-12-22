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
    Draw the snake on the screen
    """
    # Intensite lumineuse pour le serpent
    SN_LIGHT = 6

    # Affiche la tete avec plus d'intensite
    display.set_pixel(snake[0][1], snake[0][0], 9)

    for (i, j) in snake[1:]:
        display.set_pixel(j, i, SN_LIGHT)


def new_direction(dir):
    """
    Choose the new direction
    """
    # TODO: Change la direction en fonction des boutons A, B et de la
    # direction donnee

    # Si on appuie sur le bouton A, on tourne a gauche.
    # Si on appuie sur le bouton B, on tourne a droite.
    btn_a = [LEFT, UP, RIGHT, DOWN]
    btn_b = [RIGHT, DOWN, LEFT, UP]

    if button_a.was_pressed():
        return btn_a[dir]
    elif button_b.was_pressed():
        return btn_b[dir]
    else:
        return dir


def new_head(snake, dir):
    """
    Return the tuple (x, y) of the new head
    """
    # TODO: Choisi une nouvelle direction en fonction de la direction donnee
    # et de la tete
    offsets = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    off = offsets[dir]

    new = ((snake[0][0] + off[0] + 5) % 5, (snake[0][1] + off[1] + 5) % 5)
    return new


# La tete du serpent est le premier element de la liste
# La queue est le dernier element
snake = [(2, 2)]
snake_len = 2
dir = UP
apple = None

# Tant que le serpent ne rempli pas toutes les cases
while snake_len < 25:

    # TODO: Si la pomme n'existe pas (None), choisi une place aleatoire pour
    # la pomme
    while apple is None:
        (x, y) = (randint(0, screen_size - 1), randint(0, screen_size - 1))
        if not (x, y) in snake:
            apple = (x, y)

    # TODO: Change la direction
    dir = new_direction(dir)

    # TODO: Trouve la nouvelle tete du serpent
    head = new_head(snake, dir)

    # TODO: Ajoute la nouvelle tete au serpent (insere la tete en position 0)
    snake.insert(0, head)

    # TODO: Si la nouvelle tete est sur la pomme, agrandi la taille du serpent
    # Et retire la pomme de la grille (None)
    if apple == head:
        snake_len += 1
        apple = None

    # TODO: retire la derniere valeur de la queue du serpent si celui-ci
    # est plus grand que snake_len
    if len(snake) > snake_len:
        snake.pop()

    # TODO: Si le serpent se mord, c'est perdu, on casse la boucle
    if snake[0] in snake[1:]:
        break

    display.clear()
    # TODO: Affiche la pomme
    # TODO: Affiche le serpent
    if apple is not None:
        display.set_pixel(apple[1], apple[0], APP_LIGHT)
    draw_snake(snake)
    sleep(500)


# TODO: Affiche un message de victoire/defaire en fonction du score
# Le score est la taille du serpent
display.scroll("Score: " + str(snake_len))

from microbit import *
from random import randint

MAX_Y = 4
MIN_X = 0
MAX_X = 4

def show_joueur(x:int, show: bool):
    display.set_pixel(x, MAX_Y, 9 if show else 0)

def show_pomme(x:int, y:int, show:bool):
    display.set_pixel(x, y, 9 if show else 0)

alive = True
score = 0

panier_x = 2  # milieu

pomme_x = randint(MIN_X, MAX_X)
pomme_y = 0
show_pomme(pomme_x, pomme_y, True)

NB_TICKS = 5
current_ticks = 0

SCORE_INCREASE_LEVEL = 5

while alive:
    show_joueur(panier_x, False)
    if button_a.was_pressed():
        panier_x -= 1
        if panier_x < MIN_X:
            panier_x = MIN_X
    if button_b.was_pressed():
        panier_x += 1
        if panier_x > MAX_X:
            panier_x = MAX_X
    show_joueur(panier_x, True)

    current_ticks += 1
    if current_ticks == NB_TICKS:
        current_ticks = 0
        show_pomme(pomme_x, pomme_y, False)
        pomme_y += 1
        show_pomme(pomme_x, pomme_y, True)

        if pomme_y == MAX_Y:
            if panier_x == pomme_x:
                score += 1
                # reset panier
                pomme_x = randint(MIN_X, MAX_X)
                pomme_y = 0
                show_pomme(pomme_x, pomme_y, True)

                if score % SCORE_INCREASE_LEVEL == 0:
                    NB_TICKS -= 1
                    if NB_TICKS == 0:
                        NB_TICKS = 1
            else:
                alive = False

    sleep(150)


display.scroll("Perdu ! Score = " + str(score))
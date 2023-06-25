from microbit import *
from random import randint
import music

MIN_X = 0
MAX_X = 4
MAX_Y = 4

pos_panier = 2
perdu = False

pomme_x, pomme_y = randint(MIN_X, MAX_X), 0
tour = 0
tour_max = 8

score = 0

while not perdu:
    # Affichage et mouvements du panier
    display.set_pixel(pos_panier, MAX_Y, 0)

    if button_a.was_pressed() and pos_panier > MIN_X:
        pos_panier -= 1
    if button_b.was_pressed() and pos_panier < MAX_X:
        pos_panier += 1

    display.set_pixel(pos_panier, 4, 9)


    # Affichage et mouvements de la pomme
    display.set_pixel(pomme_x, pomme_y, 0)

    if tour < tour_max:
        tour += 1
    else:
        tour = 0
        pomme_y += 1

    if pomme_y == MAX_Y:
        if pomme_x == pos_panier:
            pomme_x, pomme_y = randint(MIN_X, MAX_X), 0
            score += 1
            music.play("F:2")
            
            if score % 4 == 0 and tour_max >= 0:
                tour_max -= 1

        else:
            perdu = True

    display.set_pixel(pomme_x, pomme_y, 5)

    sleep(150)

display.scroll("Perdu ! " + str(score))
from microbit import *
from random import randint


def deplace_oiseau(ois_x, ois_y, ois_int):
    display.set_pixel(ois_x, ois_y, 0)
    if button_a.was_pressed() and ois_y != 0:
        ois_y -= 1
    if button_b.was_pressed() and ois_y != 4:
        ois_y += 1
    display.set_pixel(ois_x, ois_y, ois_int)

    return ois_y


def genere_trou():
    trou_y = randint(0, 3)
    return trou_y


def affiche_tuyaux(tuy_x, tuy_int, trou_y):
    for i in range(5):
        display.set_pixel(tuy_x, i, tuy_int)
    for i in range(trou_y, trou_y + 2):
        display.set_pixel(tuy_x, i, 0)


def efface_tuyaux(tuy_x):
    for i in range(5):
        display.set_pixel(tuy_x, i, 0)


def deplace_tuyaux(tuy_x, tuy_int, trou_y):
    efface_tuyaux(tuy_x)
    affiche_tuyaux(tuy_x - 1, tuy_int, trou_y)
    return tuy_x - 1


def collision(ois_x, ois_y, tuy_x, trou_y):
    if ois_x != tuy_x:
        return False
    if ois_y == trou_y or ois_y == trou_y + 1:
        return False
    return True


oiseau_x = 1
oiseau_y = 2
oiseau_intensite = 9
display.set_pixel(oiseau_x, oiseau_y, oiseau_intensite)

tuyaux_intensite = 5
tuyau_x = 4
trou_y = genere_trou()
affiche_tuyaux(tuyau_x, tuyaux_intensite, trou_y)

temps = 150
tour = 0
tour_max = 5
score = 0

sleep(300)
while True:
    if tour == tour_max:
        tuyau_x = deplace_tuyaux(tuyau_x, tuyaux_intensite, trou_y)
        tour = 0
    tour += 1
    oiseau_y = deplace_oiseau(oiseau_x, oiseau_y, oiseau_intensite)
    if collision(oiseau_x, oiseau_y, tuyau_x, trou_y):
        break

    sleep(temps)

    if tuyau_x < oiseau_x:
        score = score + 1
        trou_y = genere_trou()
        efface_tuyaux(tuyau_x)
        tuyau_x = 4
        affiche_tuyaux(tuyau_x, tuyaux_intensite, trou_y)
        sleep(temps)



display.scroll("Game Over! Score: " + str(score))

# Accelerer le jeu a la fin quand tt marche

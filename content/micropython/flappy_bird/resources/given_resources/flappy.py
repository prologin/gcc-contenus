from microbit import *
from random import randint


def deplace_oiseau(ois_x, ois_y, ois_int):
    """
    @ois_x, ois_y : coordonnées de l'oiseau
    @ois_int : intensité de la led de l'oiseau

    vérifie si le bouton `a` ou `b` a été appuyé et, si oui, déplace l'oiseau dans la direction voulue
    return (valeur retournée): nouvelle coordonnée en y de l'oiseau
    """
    pass


def genere_trou():
    """
    return : valeur aléatoire qui sera la nouvelle valeur de trou_y
    """
    pass


def affiche_tuyaux(tuy_x, tuy_int, trou_y):
    """
    @tuy_x : colonne où sont situés les tuyaux à afficher
    @tuy_int : intensité des leds des tuyaux

    affiche les tuyaux sur le microbit
    """
    pass


def efface_tuyaux(tuy_x):
    """
    @tuy_x : colonne des tuyaux

    met l'intensité des pixels de la colonne à 0.
    """
    pass


def deplace_tuyaux(tuy_x, tuy_int, trou_y):
    """
    @tuy_x : colonne des tuyaux
    @tuy_int : intensité des leds des tuyaux
    @trou_y : numéro de la ligne du haut du trou

    déplace les tuyaux d'un cran vers la gauche
    return : nouvelle colonne des tuyaux
    """
    pass


def collision(ois_x, ois_y, tuy_x, trou_y):
    """
    @ois_x, ois_y : coordonnées de l'oiseau
    @tuy_x : colonne actuelle des tuyaux
    @trou_y : numéro de la ligne du haut du trou

    return : True si l'oiseau est en collision avec un tuyau, False sinon
    """
    pass


# variables initiales de l'oiseau
oiseau_x = 1
oiseau_y = 2
oiseau_intensite = 9
display.set_pixel(oiseau_x, oiseau_y, oiseau_intensite)

# variables initiales du tuyau
tuyaux_intensite = 5
tuyaux_x = 4
trou_y = genere_trou()
affiche_tuyaux(tuyaux_x, tuyaux_intensite, trou_y)

# variables initiales du jeu
temps = 150
tour = 0
tour_max = 5
score = 0

sleep(300)
while True:
    # TODO 2 : Si la variable `tour` est égale à `tour_max`, appeler la fonction `deplace_tuyaux` et réinitialise `tour`
    # Augmente `tour` de 1

    # TODO 1 : Appeler la fonction `deplace_oiseau` 

    if # TODO 3 : Regarder la collision entre l'oiseau et un tuyau :
        # Sortir de la boucle
        pass

    # Cette ligne arrête le programme pendant 'temps' millisecondes
    sleep(temps)

    if # TODO 4 : Vérifier si les tuyaux sont derrière l'oiseau :
        # Augmenter le score de 1
        # Générer un nouveau trou
        # Effacer les tuyaux
        # Remettre tuyaux_x à sa valeur initiale
        # Afficher les tuyaux
        sleep(temps)

# TODO 5 : Afficher "Game Over ! Score : " + le score

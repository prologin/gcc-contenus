from microbit import *
from random import randint
import radio

# TODO: Créer la liste des possibilités
possibilites = []

# TODO: Créer une variable pour avoir la longueur
# de la liste `possibilites`
NB_POSSIBILITES = 0

# Le choix du joueur est à 0 par défaut
choix_joueur = 0

# TODO: Modifier la condition d'arrêt de la boucle avant les `:`
while False:
    # TODO: Afficher le choix actuel du joueur

    # TODO: Que faire si A est appuyé ?

    # TODO: Que faire si B est appuyé ?

    # Permet de mettre en pause le programme le
    # temps de lire l'entrée du joueur
    sleep(100)

# TODO: Générer le choix du micro:bit
# entre 0 et `NB_POSSIBILITES` exclu
choix_adversaire = 0

# Éteint toutes les LEDs de l'écran
display.clear()

# Met en pause le programme pendant 500 millisecondes
sleep(500)

# TODO: Afficher le choix du joueur


# Met en pause le programme pendant 2 secondes
sleep(2000)

display.scroll("VS")

# TODO: Afficher le choix du micro:bit


# Met en pause le pause le programme pendant 2 secondes
sleep(2000)

# TODO: Si égalité, afficher "Egalite !"

# TODO: Sinon si tu as gagné, afficher "Tu as gagne !"

# TODO: Sinon, tu as perdu, afficher "Tu as perdu..."

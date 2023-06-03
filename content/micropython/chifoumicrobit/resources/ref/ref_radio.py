from microbit import *
from random import randint
import radio

# La liste des possibilités
possibilites = [Image.SKULL, Image.PACMAN, Image.GHOST]

# Le nombre de possibilités
# La fonction `len` renvoie la longueur d'une liste
NB_POSSIBILITES = len(possibilites)

# On rajoute une valeur booléenne pour savoir si
# on veut jouer avec la radio ou non
multijoueur = -1

# Cette image indique au joueur de choisir un mode de jeu
display.show(Image.SWORD)

while multijoueur == -1:
    if button_a.was_pressed():
        multijoueur = 1

    elif button_b.was_pressed():
        multijoueur = 0

# Le choix du joueur est à 0 par défaut
choix_joueur = 0

# On affiche le choix actuel le temps qu'il n'est pas validé
# par un appui simultané sur A et B
while not (button_a.is_pressed() and button_b.is_pressed()):
    # Affiche le choix actuel du joueur
    display.show(possibilites[choix_joueur])

    # Si A est appuyé
    if button_a.was_pressed():
        # On enlève 1 au choix du joueur
        # Le modulo permet de revenir au début de la liste des choix
        choix_joueur = (choix_joueur - 1) % NB_POSSIBILITES

    # Si B est appuyé
    if button_b.was_pressed():
        # On ajoute 1 au choix du joueur
        # Le modulo permet de revenir au début de la liste des choix
        choix_joueur = (choix_joueur + 1) % NB_POSSIBILITES

    # Permet de mettre en pause le programme
    # le temps de lire l'entrée du joueur
    sleep(100)

# On initialise le choix de l'adversaire à 0
# par défaut
choix_adversaire = 0

if multijoueur == 0:
    # Choix aléatoire du microbit
    # entre 0 et `NB_POSSIBILITES` exclu
    choix_adversaire = randint(0, NB_POSSIBILITES - 1)

# Gérer la radio si on est en mode `multijoueur`
if multijoueur == 1:
    # Allume la radio
    radio.on()

    # Configure le channel de la radio (entre [0, 83])
    radio.config(channel=42)

    # Cette image indique le début de la transmission radio
    display.show(Image.BUTTERFLY)

    # Initialise une variable pour recevoir
    # un message de notre adversaire
    message_adversaire = None

    while message_adversaire == None:
        # Essaye de recevoir un message
        message_adversaire = radio.receive()

        # Envoie le choix du joueur 1
        radio.send(str(choix_joueur))

    # Nous avons donc reçu le choix du joueur 2
    # Il faut le convertir en entier pour ensuite l'utiliser
    choix_adversaire = int(message_adversaire)

    # Éteindre la radio
    radio.off()

# Éteint toutes les LEDs de l'écran
display.clear()
sleep(500)

# Affiche le choix du joueur
display.show(possibilites[choix_joueur])
sleep(2000)

display.scroll("VS")

# Affiche le choix du micro:bit
display.show(possibilites[choix_adversaire])
sleep(2000)

# Égalité si les joueurs ont fait le même choix
if choix_joueur == choix_adversaire:
    display.scroll("Egalite !", delay=50)

# Tu as gagné si notre choix bat celui de l'adversaire
elif choix_joueur == 0 and choix_adversaire == 1:
    display.scroll("Gagne !", delay=50)

elif choix_joueur == 1 and choix_adversaire == 2:
    display.scroll("Gagne !", delay=50)

elif choix_joueur == 2 and choix_adversaire == 0:
    display.scroll("Gagne !", delay=50)

# Tu as perdu sinon
else:
    display.scroll("Perdu...", delay=50)

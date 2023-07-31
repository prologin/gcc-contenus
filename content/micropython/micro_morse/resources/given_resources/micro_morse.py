from microbit import *
from morse import *
import radio


def morse_vers_lettre(code, arbre):
    """
    Traduit la chaîne `code` formatté en un caractère de l'alphabet classique
    On considère que `code` est correctement formatté
    """
    pass

def creer_message():
    """
    Récupère l'entrée utilisateur et retourne la chaîne formée
    """
    pass


# Partie principale

radio.on() # Allume la radio
radio.config(channel=42) # Configure le canal utilisé (doit être compris entre 0 et 83)

display.scroll("Go!")
while True:
    message_recu = radio.receive() # Essaye de recevoir un message
    if message_recu != None:
        display.scroll(message_recu) # Affiche le message reçu s'il existe

    # Code pour écrire un message et l'envoyer

from microbit import *
from morse import *
import radio

def morse_vers_lettre(code, arbre):
    """
    Traduit la chaîne `code` formatté en un caractère de l'alphabet classique
    On considère que `code` est correctement formatté
    """
    if code == "":
        return arbre.cle

    elif code[0] == '.':
        return morse_vers_lettre(code[1:], arbre.gauche)

    else:
        return morse_vers_lettre(code[1:], arbre.droit)



def creer_message():
    """
    Récupère l'entrée utilisateur et retourne le caractère formé
    """
    display.scroll("Send")
    message = ""
    display.show(Image.HEART)

    while not (button_a.was_pressed() and button_b.was_pressed()):
        letter = ""
        while not pin_logo.is_touched():
            if button_a.was_pressed():
                letter += "."
            
            if button_b.was_pressed():
                letter += "-"

        message += morse_vers_lettre(letter, MORSE)
        sleep(1000)
    
    display.scroll(message)
    return message


radio.on() # Allume la radio
radio.config(channel=42) # Configure le canal utilisé (doit être compris entre 0 et 83)

display.scroll("Go !")
while True:
    message_recu = radio.receive() # Essaye de recevoir un message
    if message_recu != None:
        display.scroll(message_recu) # Affiche le message reçu s'il existe

    if pin_logo.is_touched():
        message = creer_message()
        radio.send(message)


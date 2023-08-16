from microbit import *
from morse import *
import radio

def morse_vers_lettre(code, arbre):
    """
    Traduit la chaîne `code` formatté en un caractère de l'alphabet classique
    Si le code n'est pas correctement formatté, renvoyer None
    """
    if code == "":
        if arbre == None:
            return None
        else:
            return arbre.cle

    elif code[0] == '.':
        return morse_vers_lettre(code[1:], arbre.gauche)

    else:
        return morse_vers_lettre(code[1:], arbre.droit)

def creer_message():
    """
    Récupère l'entrée utilisateur et retourne le caractère formé
    """
    display.scroll("Envoi !")
    message = ""

    valider = False
    while not valider:
        code = ""
        display.show(Image.GHOST)

        while not pin_logo.is_touched():
            if accelerometer.was_gesture('shake'):
                valider = True
                break

            if button_a.was_pressed():
                code += "."

            if button_b.was_pressed():
                code += "-"

        lettre = morse_vers_lettre(code, MORSE)
        
        if lettre != None:
            display.show(Image.HAPPY)
            message += lettre

        elif code != "":
            display.show(Image.ANGRY)

        sleep(1000)
    
    display.scroll(message)
    return message


# Partie principale

radio.on() # Allume la radio
radio.config(channel=42) # Configure le canal utilisé (doit être compris entre 0 et 83)

display.scroll("Allumage...", delay=50)
while True:
    message_recu = radio.receive() # Essaye de recevoir un message
    if message_recu != None:
        display.scroll(message_recu) # Affiche le message reçu s'il existe

    if pin_logo.is_touched():
        message = creer_message()
        radio.send(message)


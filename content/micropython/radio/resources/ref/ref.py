import radio
from microbit import *
import machine
import time

# image
image_emetteur = Image(
    "99900:"
    "00090:"
    "99009:"
    "00909:"
    "90909:"
)

# le mode de la carte
est_emetteur = True

# la puissance minimale pour entrer dans le rayon d'action.
puissance_minimum = -60

# le nombre de clients connectes en mode balise.
connections = set()

# configure la radio
radio.config(channel=42)

# allume la radio
radio.on()

id = machine.unique_id()

compteur = time.tick_ms()

while True:
    if button_a.was_pressed():
        est_emetteur = not est_emetteur

    if est_emetteur: # le naufragé
        msg = str(radio.receive_bytes())
        if msg == "MAYDAY":
            radio.send_bytes(bytes(f"{id}:OK", "utf-8")) #la connection est établie
            display.show(Image.HAPPY)
        else:
            radio.send_bytes(bytes(f"{id}:SOS", "utf-8"))
            display.show(Image.SAD)
    else: # balise centrale
        recu = radio.receive_full()
        while recu is not None:
            msg, puissance, _ = recu
            [client, msg] = str(msg).split(":")
            if puissance >= puissance_minimum:
                if msg == "SOS":
                    radio.send_bytes(bytes(f"{client}:MAYDAY", "utf-8"))
                elif msg == "OK":
                    connections.add(client)
            recu = radio.receive_full()
    compteur2 = time.tick_ms()
    if compteur2 - compteur >= 5000:
        connections.clear()
        compteur = compteur2
    sleep(100)


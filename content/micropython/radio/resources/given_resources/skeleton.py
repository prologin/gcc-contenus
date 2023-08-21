import radio
from microbit import *

# L'image à afficher pour l'émetteur.
image_emetteur = Image(
    "99900:"
    "00090:"
    "99009:"
    "00909:"
    "90909:"
)

# La variable pour savoir si la carte est émettrice.
est_emetteur = True
# La puissance minimum requise pour détecter un autre naufragé.
puissance_minimum = -60

# configuration du module radio
radio.config(channel=42)

# activation du module radio
radio.on()

while True:
    # TODO : remplir le code ici

    # Cette instruction permet au code de marquer un pause de 100 millisecondes
    # entre chaque itération de la boucle pour réduire la puissance nécéssaire
    # pour faire fonctionner la carte.
    sleep(100)


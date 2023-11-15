# Commençons !

## Mise en place
Tout d'abord, télécharge le squelette du TP via le bouton `Code à compléter`,
en haut de la page, puis ouvre ce fichier dans ton éditeur de texte préféré.

## Explication du squelette

Avant tout, il faut importer les bons modules pour pouvoir utiliser la
radio sur la carte `micro:bit`.

Voici le code du squelette :
```python
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
```

Voici le motif de `image_emetteur`. Il s'agit d'une image de 5x5 pixels,
ce qui est la définition d'affichage d'une carte `micro:bit`.
{{< figure src="./resources/images/EmetteurImage.png" height="200" >}}

Ensuite, il faut configurer le module radio et l'activer.

```python
# configuration du module radio
# le paramètre channel correspond au canal sur lequel le module radio doit
# écouter et recevoir des informations.
radio.config(channel=42)

# activation du module radio
radio.on()
```

{{% box type="info" %}}

Il existe beaucoup de paramètres pour configurer la radio que nous
n'explorerons pas ici, mais n'hésite pas à regarder plus en profondeur la
[documentation](https://microbit-micropython.readthedocs.io/en/v1.0.1/radio.html#radio.config)
du module si cela t'intéresse.

{{% /box %}}

Finalement, pour permettre aux autres naufragés de te recevoir à
n'importe quel moment, il faut ajouter une boucle qui se répète indéfiniment.

```python
while True:
    # TODO : remplir le code ici

    # Cette instruction permet au code de marquer une pause de 100 millisecondes
    # entre chaque itération de la boucle pour réduire la puissance nécessaire
    # pour faire fonctionner la carte.
    sleep(100)
```

{{% box type="info" %}}

L'instruction `sleep(100)` marque une pause de `100` millisecondes entre chaque
tour de boucle pour éviter à la carte d'avoir à exécuter trop d'instructions à
la suite.
{{% /box %}}

## Changer le mode de la balise
Nous voulons utiliser la balise dans plusieurs modes.
> Un mode est un moyen pour une même carte d'utiliser plusieurs codes
> différents en fonction du contexte dans lequel elle se trouve.  
> Nous devons effectivement recevoir les appels des autres naufragés et 
> être capable de leur envoyer des messages aussi.

Il faut que la balise puisse savoir si elle doit émettre ou recevoir.

{{% box type="exercise" %}}

Rajoute des instructions de code dans la boucle, qui vont permettre à la balise de changer de mode lorsque le bouton `A`
est pressé.

Pour rappel, le mode de la balise est représenté par la variable
`est_emetteur`.
{{% /box %}}
{{% box type="info" %}}

Tu peux utiliser la fonction `was_pressed` de `button_a` qui
t'indique si le bouton a été appuyé depuis la dernière fois que cette fonction
a été appelée.

{{% /box %}}


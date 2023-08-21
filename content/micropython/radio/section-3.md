---
show_toc: true
---

# Le module radio


## Le mode émetteur

Le mode émetteur permet à la balise d'émettre des messages à intervalles
réguliers. Ils seront reçus par les récepteurs afin que des sauveteurs puissent
te retrouver en pleine mer.

{{% box type="info" %}}

La fonction `send(mesage)` du module `radio` permet d'envoyer un
message via la radio du `micro:bit`.
{{% /box %}}

Voici un exemple d'utilisation de la fonction `radio.send` : 

```python
from microbit import *
import radio

# Configuration de la radio.
radio.config(channel=42)

# Allumage de la radio.
radio.on()

# Envoie un message lorsque la carte démarre.
radio.send("Demarrage")

while True:
    # Envoie un message a chaque fois que le bouton A est appuyé.
    if button_a.was_pressed():
        radio.send("appui")

    sleep(100)
```

{{% box type="exercise" %}}

Écris un code dans la boucle infinie, qui, lorsque la balise est en mode
émetteur, envoie le message `SOS` à toutes les balises réceptrices.

*Note: Par défaut, lorsqu'un message est envoyé, il est envoyé à toutes les
cartes `micro:bit` qui écoutent.*

{{% /box %}}

## Le mode récepteur

Grâce à la première partie du TP, ta balise peut maintenant envoyer des
messages mais ne peut pas recevoir d'informations d'une autre balise.
Il serait vraiment mieux si tu pouvais retrouver les autres naufragés.

{{% box type="info" %}}

Le module `radio` ne permet pas de connaître la distance parcourue par un message 
reçu. Il va donc falloir utiliser la puissance du signal reçu pour
estimer la distance.

La puissance d'un signal s'exprime en décibels (de symbole `dB`),
comme le son !
Plus la source d'émission du signal est loin, moins la puissance en décibels
sera importante.
{{% /box %}}

{{% box type="info" %}}

La fonction `receive_full()` du module `radio` permet, entre autres, de savoir
avec quelle force le message a été reçu.

Cette fonction renvoie un `tuple`, ou `None` si aucun message n'est reçu. 

> Le `None` est une valeur propre à `Python` qui signifie qu'il n'y a rien.
> En d'autres termes cela veut dire qu'il s'agit d'une valeur vide. Dans notre
> cas, si la fonction `receive_full` renvoie `None`, alors aucun message n'a
> été reçu.

Ce tuple contient :
- Le contenu du message
- La puissance du signal (c'est-à-dire la force avec laquelle le message
a été reçu) de `-255` (le plus faible) à `0` (le plus fort).
- Le moment auquel le message a été reçu.

*Rappel : Un `tuple` en Python est un groupement de valeurs permettant à
une fonction de renvoyer plusieurs informations.*


Il est possible d'extraire les valeurs contenues dans ce `tuple` :

```codepython
# création d'un tuple contenant les valeurs 1, 2, et 3
tup = (1, 2, 3)

# il est possible d'accéder aux éléments d'un tuple comme dans une liste
# par exemple, accéder au premier élément.
print(tup[0]) # Affiche 1
# ou accéder au troisième élément.
print(tup[2]) # Affiche 3

# il est également possible de mettre les valeurs dans des variables
x, y, z = tup # x = 1, y = 2, z = 3

# ce qui revient à faire
print("x = " + str(tup[0])) # x = 1
print("y = " + str(tup[1])) # y = 2
print("z = " + str(tup[2])) # z = 3
```
{{% /box %}}


*Voici un exemple de l'utilisation de la méthode `receive_full`* :

```python
recu = radio.receive_full()

# si aucun message n'a été reçu, il ne faut rien faire.
# dans ce cas, le message reçu serait None.
if recu is not None:
    # le premier élément du tuple est le contenu du message
    # Içi SOS par exemple.
    message = recu[0]

    # le deuxième élément est la puissance du signal.
    puissance = recu[1]

    # Affiche le message reçu par la balise client (émétteur).
    display.scroll(message)

    # Affiche la puissance du signal.
    display.scroll(str(puissance))
```

{{% box type="exercise" %}}

Écris la partie récepteur de la balise.

<details>
<summary>Clique ici pour avoir de l'aide !</summary>

*Aide : Le code peut suivre cette procédure, écrite en pseudo-code :*

```text {nocopy=true}
si la balise est réceptrice, alors
    message_reçu <- radio.receive_full()
    si message_reçu est None, alors
        On ne capte pas de balise aux alentours.
    sinon,
        message, puissance, temps <- message_reçu
        si puissance > puissance_minimum, alors
            # Une balise proche et d'autres naufragés sont détectés
            Affiche l'image Image.HAPPY
        sinon,
            # La puissance n'est pas suffisante, aucune balise n'est proche.
            Affiche l'image Image.SAD
```

</details>

{{% /box %}}

Bravo ! Tu sais maintenant si des naufragés sont proches, et tu peux 
envoyer des messages aux secours.

Cette première partie du TP t'as permis de mieux comprendre l'utilisation du
module radio. Dans la prochaine partie, tu vas pouvoir utiliser ce module radio
pour faire évoluer ta balise.

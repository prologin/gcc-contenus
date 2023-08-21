---
show_toc: true
---

# Aller plus loin

Maintenant que tu as un système de balises fonctionel, il serait intéressant de
pouvoir connaître le nombre de naufragés repérés. Pour cela, il faut que la
balise centrale garde un compte de toutes les balises qui lui ont envoyé un
message.


## Établissement du protocole
Pour être sûr que l'émetteur et le récepteur se comprennent, il faut établir ce
que l'on appelle un protocole.

{{% box type="info" %}}

Un protocole est une liste de règles précises qui doivent être respectées afin
de s'assurer que toutes les personnes utilisant ce protocole se comprennent.

En d'autres termes, il s'agit du langage que nous souhaitons utiliser.
{{% /box %}}

Puisqu'il s'agit d'un langage, tu es libre d'utiliser ce que tu veux comme
convention pour permettre aux cartes de communiquer entre elles.

Par exemple, on peut dire que lorsque la balise centrale (le récepteur) reçoit
la chaîne de caractères `SOS`, alors un client a commencé à établir une 
communication avec la balise centrale. À ce moment-là, la balise centrale
envoie à son tour le message `MAYDAY`, pour signifier aux naufragés qu'elle
reçoit leur signal.

Voici un schéma explicatif de la manière dont notre protocole va fonctionner :
{{< figure src="./resources/images/schema_2.png" >}}

Pour résumer :
1. L'émetteur envoie `SOS`
2. Quand le récepteur reçoit `SOS`, il renvoie `MAYDAY`.
3. Quand l'émetteur reçoit `MAYDAY`, la connexion est établie, il renvoie `OK` pour faire valider la connexion par le récepteur.
4. Quand le récepteur reçoit `OK`, alors il sait qu'un nouvel émetteur est connecté.
5. L'émetteur et le récepteur peuvent communiquer.
6. Quand le récepteur ne reçoit plus de message, alors il considère que l'émetteur n'est plus dans sa zone de détection.


Une fois la connexion établie, le but va être de connaître le nombre de
naufragés aux alentours.

Nous pouvons estimer qu'un client qui n'a pas envoyé de messages depuis
un certain temps est déconnecté.


### Côté naufragé (client/émetteur)

Désormais, il faut que le naufragé envoie le message `OK` lorsqu'il reçoit
le message `MAYDAY`.

{{% box type="exercise" %}}

Écris le code permettant au client d'envoyer le message `OK` lorsque le message
`MAYDAY` est reçu.
{{% /box %}}

### Côté balise centrale (serveur/récepteur)

Maintenant que le client répond au message de la balise, il faut permettre
à la balise de lire les messages de tous les clients.

{{% box type="info" %}}

Lorsque le module `radio` de la carte `micro:bit` reçoit un message, le
message est stocké dans la mémoire avant d'être lu. Tu peux lire les messages
stockés avec la fonction `receive` du module `radio` qui renvoie une
chaîne de caractères s'il y a encore des messages non lus, sinon `None`.

Ainsi, si le message renvoyé par `receive` vaut `None` alors, tous les messages
ont été lus.
{{% /box %}}

Nous savons que le récepteur peut recevoir deux messages différents :
 - `SOS`: Si un naufragé ignore que la balise existe et est proche.
 - `OK`: Lorsque le naufragé sait que la balise existe.


{{% box type="exercise" %}}

Modifie le code de la balise centrale pour qu'elle tienne un compte des
naufragés actuellement connectés à celle-ci.

Astuce : Le nombre de clients connectés correspond au nombre de messages
reçus contenant la chaîne de caractères `OK` sur les dernières 5 secondes
(par exemple).

Tu peux t'aider du pseudo-code ci-dessous.

```text {nocopy=true}
# la balise est réceptrice.

tant qu'il y a des messages:
    récupérer la puissance et le contenu du message
    si la puissance est suffisante, alors:
        si le message est `SOS`, alors:
            envoyer le message `MAYDAY`
        sinon si le message est `OK`, alors:
            # un naufragé est détecté.
            Incrémenter le compteur de naufragés.
```

N'oublie pas de remettre le compteur de naufragés à 0 après 5 secondes !

{{% /box %}}

{{% box type="info" %}}

Pour calculer le temps entre deux instants, tu peux utiliser le module
`time`, et les fonctions `ticks_ms` et `ticks_diff`

```python
import time

compteur_1 = time.ticks_ms()

compteur_2 = time.ticks_ms()

# donne la différence en millisecondes entre compteur_1 et compteur_2
difference = time.ticks_diff(compteur_1, compteur_2)

```
{{% /box %}}

{{% box type="info" %}}

Rappel : pour envoyer un message, tu peux utiliser la fonction `send` du 
module `radio` qui prend une chaîne de caractères en paramètre.
{{% /box %}}

Si jamais tu as besoin d'aide n'hésite pas à demander à un organisateur,
ils sont là pour toi !

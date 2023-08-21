---
show_toc: true
---

# Toujours plus loin !

## Générer un identifiant pour chaque client

Tu auras remarqué que le compte de balises n'est pas très précis. Cela est dû
au fait que la balise centrale ne sait pas de qui provient chaque message.

Pour remédier à cela, il faut trouver un système fiable permettant à chaque 
client d'avoir un identifiant unique.


{{% box type="info" %}}

Pour générer un identifiant unique par machine, le plus simple étant d'utiliser
la fonction `unique_id` du module `machine`. Cette fonction va te renvoyer
une chaîne de caractères particulière qui peut contenir n'importe quel 
caractère. Ce genre de chaînes de caractères s'appelle des `byte string` et
représentent en fait des listes d'octets.

*Note: Un octet est un groupement de 8 bits qui forment un nombre entre 0 et
255. Chaque octet représente un caractère grâce à ce que l'on appelle la table
__ASCII__. Cette table est l'équivalent de l'alphabet où le `A` vaut 1 et le 
`Z` 26 par exemple ou encore l'alphabet morse ou le `A` vaut `.-` et le `Z`
vaut `--..`.*

Pour utiliser le module `machine`, il faut l'importer au début de ton fichier grâce à cette ligne : 
```python
import machine
```
Tu peux ensuite créer une variable `id` qui contiendra `machine.unique_id()` avant de commencer ta boucle while, pour créer l'identifiant de ce `micro:bit`
{{% /box %}}

{{% box type="exercise" %}}

Adapte le mode émetteur de la balise pour que tous les messages envoyés par 
celle-ci soient de la forme `<ton_identifiant_unique>:<ton_message>`.
Comme spécifié par le protocole.

Par exemple, si ma balise a pour identifiant unique `123456`, et qu'elle doit
envoyer le message `SOS`, le message final doit etre `123456:SOS`.

{{% /box %}}

## Connexion !

Désormais, chaque client possède un identifiant unique. Tu peux donc
savoir exactement combien de clients sont connectés à ta balise.

Comme spécifié dans le protocole, tous les messages envoyés par le client
doivent être sous la forme `<identifiant>:<mon_message>`, et le serveur doit
également répondre au client avec des messages de la même forme en spécifiant
l'identifiant du client.

Maintenant que tu as un moyen de savoir qui est l'émetteur d'un message,
pour connaître exactement le nombre de naufragés dans le rayon de la 
balise, il faut savoir combien de naufragés différents ont envoyé des
messages dans les cinq dernières secondes.

{{% box type="exercise" %}}
Modifie le code du serveur pour stocker l'heure du dernier message 
reçu pour chaque client.

Astuce : tu peux modifier la liste des identifiants et remplacer par des
tuples contenant l'identifiant et l'heure du dernier message pour 
cet identifiant.
{{% /box %}}

Tu peux maintenant savoir précisément quand chaque client a envoyé un message
pour la dernière fois.

Il ne te reste plus qu'à récupérer tous les identifiants dont le dernier
message remonte à moins de 5 secondes pour connaître le nombre de clients
connectés en ce moment !

---
# Conclusion
Bravo, tu es arrivée à la fin de la partie (plus ou moins) guidée de ce TP !
Tu as maintenant tous les outils nécessaires pour utiliser le module radio
pour toute sorte de projets.

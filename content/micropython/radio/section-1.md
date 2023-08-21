---
show_toc: true
---

# Introduction

Oh non !
Tu t'es perdue en pleine mer après que ton bateau ait coulé,
il faut absolument que tu puisses détecter les bateaux aux alentours. En plus, tu n'as plus qu'un `micro:bit`
et un ordinateur avec juste assez de batterie pour t'en sortir.

{{% box type="info" %}}

Le but de ce TP est de créer un système de balises grâce aux cartes `micro:bit`.
Ces balises vont permettre de se détecter entre elles, et ainsi de savoir si d'autres naufragés,
ou encore des bateaux de sauvetage sont aux alentours.

Pour cela, il va falloir utiliser une balise centrale qui sera chargée de détecter 
les autres naufragés lorsque ceux-ci entreront dans sa zone de détection.

Ce TP va te permettre de comprendre le fonctionnement du module
`radio` de la carte `micro:bit`.
{{% /box %}}

Voila une petite mise en scène de la situation : 

{{< figure src="./resources/images/explication.png" >}}

## Utilisation

Suite au naufrage du navire, tu as perdu les autres membres de l'équipage.
Il faut donc qu'ils puissent te détecter également.

{{% box type="info" %}}

Ici, tu vas créer une balise qui va te permettre à la fois de
détecter les autres naufragés ainsi que les bateaux aux alentours.

Ainsi, la carte `micro:bit` peut agir à la fois comme une balise
`réceptrice` (aussi appelée `serveur` ou balise `centrale`), et comme une
balise `émettrice` (aussi appelée `client`).

La balise `réceptrice` agit comme un phare permettant aux clients de savoir
s'ils sont à côté de celle-ci.

La balise `émettrice` est donc une carte `micro:bit` qui va tenter de détecter la balise
centrale.

{{% /box %}}

Voici un schema simplifié des interactions entre les deux balises, que nous allons réaliser lors de ce TP.
{{< figure src="./resources/images/schema_1.png" >}}

Attention, si le récepteur est trop loin, le signal va se perdre dans l'eau !

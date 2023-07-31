# Joseph est dans de beaux draps...

Au cours d'une balade en forêt, Joseph Marchand et sa soeur tombent sur une
cave mystérieuse. En soif d'aventure, Joseph décide d'aller voir à
l'intérieur... 

Soudain, une porte se referme sur lui !

Joseph regarde alors autour de lui pour trouver une sortie, mais rien à
l'horizon. Il aperçoit alors une phrase mystérieuse sur le mur :

> La parole du morse ouvrira la voie...

Cette phrase est suivie d'une suite incompréhensible de points et de traits...
Joseph comprend alors qu'il va devoir déchiffrer ces symboles pour pouvoir
sortir.

Il se souvient avoir déjà vu ces symboles, dans le
[code morse](https://fr.wikipedia.org/wiki/Code_Morse_international). Mais
malheureusement, il ne connait pas cet alphabet par coeur, et lorsqu'il appelle
à l'aide, aucune réponse de la part de sa soeur...

Sa soeur, quant à elle, voit un clavier à coté de l'entrée de la cave. Il va
falloir qu'elle rentre un code pour délivrer son frère.

Peux-tu les aider en créant un programme qui traduit le code morse et qui leur
permet de communiquer ? 

{{% box type="info" title="Le code morse, qu'est-ce que c'est ?" %}}

Le code morse est un langage constitué uniquement de points (`·`) et de traits 
(`-`). Chaque lettre correspond à une suite de points et de traits dont l'ordre
permet de donner un sens à chaque séquence. Par exemple, pour écrire la lettre
`A` en morse, il faut écrire `.-`.

<br/>

Voici un tableau représentant les traductions de toutes les lettres et tous les
chiffres en morse :

{{<figure src="./resources/images/International_Morse_Code.png" >}}

Tu l'as peut-être remarqué, certaines lettres ont une partie commune. Par
exemple, `A` et `J` commencent toutes les deux par `.-`. On appelle
cette partie un **préfixe commun**. Nous allons utiliser cette caractéristique
pour passer du morse au français, et inversement.

{{% /box %}}

{{% box type="exercise" title="Mission 1 : Utilisation du code morse" %}}

Avant d'avancer, il va falloir tester des connaissances sur le code morse !
Peux-tu traduire le mot `GCC` en code morse ?

<br/>

<details>
<summary>Clique ici pour avoir la solution !</summary>

En utilisant le tableau juste au-dessus, nous pouvons combiner les lettres pour
obtenir la traduction du mot `GCC` en morse.

<br/>

La lettre G correspond au code `--.`, tandis que la lettre C correspond à `-.-.`.
En combinant ces informations, nous pouvons avoir le code suivant :
`--. -.-. -.-.`.

</details>

{{% /box %}}
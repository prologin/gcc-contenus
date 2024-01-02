## La Team Rocket veut se battre !

Dans les hautes herbes, il y a des Pokemon sauvages mais aussi **des Dresseurs qui cherchent à s'affronter**.

Et il s'agit même de la team Rocket !

{{<figure src="resources/images/team-rocket.webp" height=300 caption="">}}

Pour le bien du monde Pokemon, il faut les battre !

Crée une fonction `duel` qui prend en paramètre 2 dresseurs.

Nous allons créer un **combat automatique**, où les dresseurs enverront chacun leur premier Pokemon, puis leur second et ainsi de suite, jusqu'à ce qu'un dresseur ait tous ses Pokemon KO.

Pour cela, comme dans la méthode précédente `combat` de la classe `Dresseur` où le dresseur affrontait un Pokemon sauvage de manière automatique, nous allons parcourir les listes de Pokemon des dresseurs.

D'abord, les dresseurs envoient chacun leur premier Pokemon.  
Ensuite, suite au combat :
- si le Pokemon KO appartient au 1er dresseur, alors celui-ci envoie son 2e Pokemon pour se battre ; tandis que l'autre dresseur garde le même Pokemon pour combattre,
- sinon, c'est l'autre dresseur qui envoie son prochain Pokemon.
Et ainsi de suite, jusqu'à ce qu'un dresseur n'ait plus de Pokemon.

La boucle va ressembler à ceci :
```python
poke1 = 0
poke2 = 0
while poke1 < len(dresseur1.pokemons) and poke2 < len(dresseur2.pokemons):
    resultat = combat(pokemon1, pokemon2)
    if resultat == 1: # le 1er Pokemon est gagnant
        poke2 = poke2 + 1 # passe au Pokemon suivant du 2e dresseur
    else:
        poke1 = poke1 + 1
```

{{% box type="warning" %}}

Attention, dans le code donné ci-dessus, `pokemon1` et `pokemon2` n'existent pas.

À toi de les remplacer par la bonne instruction.

{{% /box %}}

À la fin du combat, tu peux afficher quel dresseur a gagné le combat !

{{<figure src="resources/images/bye-team-rocket.gif" height=300 caption="">}}
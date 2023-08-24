## Bienvenue au centre Pokémon

Suite à autant de combats Pokémon, votre équipe peut avoir du mal à continuer.

Créons un **centre Pokémon pour les soigner** !

Nous allons définir le passage dans un Centre Pokémon comme une simple fonction, `visite_PokeCenter()`.

{{% box type="info" %}}

Pour cette partie, tu auras besoin des fonctions `print` et `input`, ainsi que de savoir parcourir une liste.

{{% /box %}}

### Dialogue

Tout d'abord, lorsqu'un dresseur entre dans un Centre Pokémon, l'infirmière Joëlle l'acceuille avec le texte :
```text
Bienvenue au centre Pokémon. Nous pouvons soigner vos Pokémon.
```

Puis, l'infirmière propose au dresseur de soigner ses Pokémon :
```text
Voulez-vous les soigner ?
```

Si le dresseur répond "oui" à sa question, l'infirmière demande d'attendre un instant, récupère les Pokémon et les soigne.

{{% box type="info" %}}

En Python, il est possible de comparer des chaînes de caractères entre elles simplement :
```codepython
poke1 = "Pikachu"
poke2 = "Rattata"
poke3 = "Rattata"

print(poke1 == poke2)
print(poke2 == poke3)

if poke2 == poke3:
    print("Les Pokemon 2 et 3 ont le même nom")
```

{{% /box %}}

{{<figure src="resources/images/infirmiere-joelle-pokemon.webp" height=300 caption="">}}

### Soigner les Pokémon

Pour soigner les Pokémon du dresseur, l'infirmière va avoir besoin d'accéder à l'équipe du dresseur.

Pour cela, nous pouvons **ajouter un paramètre** `dresseur` à la fonction `visite_PokeCenter`.

Grace au dresseur, nous pouvons accéder à la liste de Pokémon, avec :
```python
dresseur.pokemons
```

Ainsi, il est possible de changer l'attribut `vie` de chaque Pokémon de la liste, avec une simple boucle.

Mais **quelle est la valeur maximum de la vie** de chaque Pokémon ?

Nous avons à présent, aucun moyen de savoir quels étaient les points de vie maximum des Pokémon, valeur qu'ils avaient avant de combattre.

Pour résoudre ce problème, **ajoutons un attribut** `vie_max` à la classe `Pokemon`.

Il sera défini lors de la création d'un Pokémon, avec la même valeur que l'attribut `vie`.

Mais la valeur `vie_max` ne sera jamais modifiée lors d'un combat, contrairement à `vie`. Donc nous pouvons l'utiliser dans la fonction `visite_PokeCenter` pour remettre `vie` du Pokémon à sa valeur initiale.

{{<figure src="resources/images/soin.gif" height=300 caption="">}}

### Dialogue de fin

L'infirmière Joëlle, après avoir soigné les Pokémon du dresseur, l'informe que tout s'est bien passé :
```text
Merci d'avoir attendu. Vos Pokémon sont en super forme.
```

Enfin, lorsque le dresseur s'éloigne de l'infirmière, elle l'incite à revenir une prochaine fois :
```text
À une prochaine fois peut-être.
```

{{<figure src="resources/images/joelle.gif" height=300 caption="">}}
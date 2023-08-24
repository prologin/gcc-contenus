## Dresseur

> Cher dresseur, le monde Pokémon est vaste.
> Explore-le, rencontre un maximum de Pokémon et crée la meilleure équipe !

Créons une nouvelle classe `Dresseur`, pour créer ton personnage dans ce jeu Pokémon.

Chaque dresseur aura un nom et une liste de Pokémon.

Lors de la création d'un dresseur, le nom est donné en paramètre, et la liste est créée vide.

{{% box type="info" title="Rappel sur les listes" %}}

Une liste vide est définie avec :
```codepython
ma_liste = []
print(ma_liste)
```

{{% /box %}}

<details>
<summary>Solution</summary>

```python
class Dresseur:
    def __init__(self, nom):
        self.nom = nom
        self.pokemons = []
```

</details>

Crée à présent le dresseur qui sera ton personnage dans la partie.

{{<figure src="resources/images/dresseur.png" height=250 caption="">}}

### Attrapez-les tous !

Que serait un jeu Pokémon, sans **capture Pokémon** !

Nous allons pour le moment simplifier au maximum la capture.

Créons une nouvelle méthode `capture` dans la classe `Dresseur`, qui prend en paramètre le Pokémon à attraper, et qui l'**ajoute à la liste de Pokémon du dresseur**, sans aucune vérification.

{{% box type="info" title="Rappel sur les listes" %}}

Pour ajouter un élément à la fin d'une liste :
```codepython
ma_liste = []
print(ma_liste)
ma_liste.append(2)
print(ma_liste)
ma_liste.append(8)
print(ma_liste)
```

{{% /box %}}

Crée ensuite un Pokémon, qui sera ton premier Pokémon, ton starter !

Tu n'as plus qu'à le capturer.

{{<figure src="resources/images/attrapez-les-tous.jpg" height=350 caption="">}}
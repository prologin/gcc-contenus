## Pokemon

Grâce à notre nouvelle classe Pokemon, nous pouvons commencer à jouer avec eux !

Crée un premier Pokemon, pourquoi pas Pikachu ?  
Crée un autre Pokemon, un Piafabec ?

Attention, le Piafabec sauvage attaque Pikachu !

{{<figure src="resources/images/piafabec-vs-pikachu.jpg" height=250 caption="">}}

### À l'attaque !

Pour savoir comment coder l'attaque du Pokemon, il faut **d'abord réfléchir** à ce qu'on veut.

Qu'est ce que ça signifie qu'un Pokemon attaque un autre Pokemon ?  
Qu'avons nous comme paramètre ? Que faut-il regarder ?

On peut dire que lorsqu'un Pokemon attaque un autre, il va retirer des points de vie à celui-ci.

Mais combien ?  
On peut par exemple, utiliser le nombre de points de dégâts du Pokemon attaquant.

En mathématiques, ça donnerait
```text
vie du pokemon attaqué = vie du pokemon avant attaque
                         - points de dégâts du pokemon attaquant
```

**Créons une nouvelle méthode dans la classe Pokemon**, qui se nomme `attaque`.

Cette méthode sera appelée depuis le Pokemon attaquant, sur le Pokemon attaqué. Si on reprend l'exemple donné :
```python
piafabec.attaque(pikachu)
```

Donc la méthode `attaque` aura un paramètre : le Pokemon attaqué.  
Elle sera donc de la forme :
```codepython
class Pokemon:
    def attaque(self, pokemon_adverse):
        pass
```

{{% box type="exercise" %}}

Remplace l'instruction `pass` par le calcul pour retirer des points de vie à `pokemon_adverse`.

{{% /box %}}

Tu peux également afficher une phrase lorsqu'un Pokemon en attaque un autre, comme :
```text
[...] attaque [...].
```

{{<figure src="resources/images/picpic.gif" height=250 caption="">}}

### Combat

Suite à l'attaque du Piafabec, Pikachu replique !  
S'en suit un combat entre les 2 Pokemon, jusqu'à ce que l'un d'entre tombe KO.

Créons une fonction `combat`, en dehors de la classe `Pokemon`, pour appliquer leur combat.

Cette fonction prend en paramètres les 2 Pokemon.

Un combat est un enchaînement d'attaques de chaque Pokemon l'un vers l'autre, le tout répété tant que les 2 Pokemon sont encore en vie.

Dès qu'un Pokemon est KO, le combat est arrêté, c'est le Pokemon opposant qui gagne le combat.

Si on traduit ces contraintes en programmation, on peut voir la structure d'une boucle, et celle-ci s'arrête lorsqu'un Pokemon est KO, donc lorsque sa vie tombe à 0. Il s'agit d'une boucle `while`.

{{% box type="info" %}}

Tu peux utiliser l'opérateur logique `and` pour tester 2 conditions en même temps :
```codepython
print(1 < 2)
print(3 < 4)
print(1 < 2 and 3 < 4)
print(False)
print(1 < 2 and False)
```

L'opérateur `and` renvoit True si les conditions à droite et à gauche de l'opérateur sont vraies.

Si un des conditions, ou les 2, sont fausses alors l'opérateur `and` remvoit False.

{{% /box %}}

Enfin, pour donner le résultat du combat, la fonction retournera :
- `1` si le Pokemon gagnant est le premier donné,
- `2` si le Pokemon gagnant est le deuxième paramètre de la fonction.

{{% box type="info" %}}

Le mot-clé `return` permet à une fonction ou à une méthode, de retourner une valeur.
```codepython
def ma_fonction():
    return 10

a = ma_fonction()
print(a)
```

{{% /box %}}

On peut également afficher la phrase "[nom du Pokemon] est KO, [nom de l'autre Pokemon] a gagné !" à la fin du combat.
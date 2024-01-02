## Un Pokémon sauvage apparaît !

Fort de ton premier Pokémon, tu te sens confiante pour t'aventurer dans les hautes herbes.

Oh ! Un Pokémon sauvage !

{{<figure src="resources/images/sauvage-apparait.png" height=300 caption="">}}

Vite, crée une méthode dans la classe `Dresseur` pour combattre ce Pokémon.

On peut nommer cette **méthode `combat`**, qui prend en paramètre le Pokémon adverse.

Nous allons pour le moment nous contenter d'un **combat automatique**, où le dresseur envoie un à un ses Pokémon lors du combat.

Pour donner un exemple :

*Le dresseur a 2 Pokémon, le 1er étant Carapuce, et le 2e étant Salamèche.*  
*Il rencontre un Pokémon sauvage, un Rattata.*

- Le dresseur va envoyer son 1er Pokémon automatiquement pour combattre le Pokémon sauvage.
  Donc vont d'abord s'affronter Carapuce et Rattata.
- Si **Rattata est mis KO**, ça signifie que Carapuce a gagné, ainsi que le dresseur a gagné le combat.
- Sinon, ça signifie que **Carapuce est KO**, le dresseur va ainsi envoyer son prochain Pokémon, Salamèche.  
  Dans ce cas, si Salamèche gagne, c'est le dresseur qui l'emporte sur le Pokémon sauvage ; sinon, le dresseur n'a plus de Pokémon capable de se battre, c'est le Rattata sauvage qui gagne.


On peut voir dans cette trame que nous répétons l'action de combat de Pokémon tant que le Pokémon sauvage est en vie, et que le dresseur possède encore des Pokémon.

Si on exprime cette trame en utilisant des outils de programmation :
```text
Méthode combat(dresseur, pokemon_sauvage):
    pokemon = 1er pokemon du dresseur
    tant que (pokemon_sauvage est en vie) et (pokemon existe):
        combat(pokemon, pokemon_sauvage)
        pokemon = pokemon suivant du dresseur
    si pokemon_sauvage est en vie:
        pokemon_sauvage a gagné
    sinon:
        dresseur a gagné
```

Traduisez ce texte pour créer la méthode `combat`.

{{% box type="info" title="Rappel sur les listes" %}}

Il est possible de parcourir tous les éléments d'une liste avec une boucle `while`:
```codepython
ma_liste = [2, 3, 4, 5]
index = 0  # Premier élément est à l'indice 0
while index < len(ma_liste):  # inférieur à la taille de la liste
    print(ma_liste[index])  # accès à l'élément à l'indice `index`
    index += 1  # passer à l'indice suivant
```

{{% /box %}}

Tu peux afficher à la fin de la méthode si le dresseur a gagné ou perdu face au Pokémon sauvage.

> Vous n'avez plus de Pokémon en vie, vous avez perdu.  
ou  
> Vous avez battu le Pokémon sauvage. Félicitations !


### Go Pikachu !

Nous pouvons à present nous battre contre les Pokémon sauvages. Mais il serait préférable de pouvoir **choisir quel Pokémon envoyer combattre**, pour ajouter un élément de stratégie à notre jeu.

Créons une **nouvelle méthode `combat_interactif`** dans la classe `Dresseur`, qui prend en paramètre le Pokémon adverse.

Cette méthode aura les mêmes éléments que la méthode précédente.

Le changement principal sera le **choix du Pokémon de l'équipe** du dresseur qui va combattre.

{{<figure src="resources/images/pikachu-fighting.gif" height=250 caption="">}}

Pour faciliter le choix du joueur, nous allons lui **afficher la liste de ses Pokémon en vie**, avec un nombre associé, que le joueur devra par la suite entrer, pour sélectionner le Pokémon.

Pour faciliter l'utilisation de ce nombre, nous allons simplement utiliser l'indice du Pokémon dans l'équipe de Pokémon du dresseur.

Par exemple :
```text {nocopy=true}
0 Carapuce
1 Salamèche
```

Affiche uniquement les Pokemon qui ne sont pas KO.

Après cet affichage, nous allons **demander quel Pokémon** le dresseur choisit pour combattre le Pokémon sauvage.

Pour cela, nous allons utiliser la fonction `input`.

{{% box type="info" title="Rappel sur `input`" %}}

La fonction `input` permet de poser une question à l'utilisateur, d'attendre sa réponse, et de la récupérer :
```codepython
prenom = input("Comment tu t'appelles ?") # on récupère la réponse dans la variable `prenom`
print("Bonjour", prenom)
```

{{% /box %}}

Demande à l'utilisateur quel Pokémon il veut envoyer et stocke sa réponse dans une variable.

{{% box type="warning" title="" %}}

Attention, la réponse envoyée par `input` est tout le temps du type `string` (chaîne de caractères).

Il faut donc transformer le nombre entré en entier, avant de s'en servir.

Pour cela, il suffit d'utiliser `int()`:
```codepython
chaine = "6"
nombre = int(chaine)
print(nombre + 3)
```

{{% /box %}}

Il est maintenant possible de **récupérer le Pokémon désiré dans l'équipe du dresseur**, avec un simple accès à un élément dans la liste, à l'indice donné.

Ensuite, nous pouvons reprendre la méthode précédente pour le combat entre le Pokémon choisi et le Pokémon adverse.

Comme pour la méthode précédente, on **envoie un autre Pokémon lorsque celui de l'équipe du dresseur est KO**. Nous allons donc retrouver une boucle `while`, qui demande à chaque fois au dresseur quel Pokémon envoyer.

Le choix du Pokémon étant dépendant du dresseur, nous devons modifier la condition de la boucle pour s'arrêter, nous ne pouvons pas juste regarder si on a fini la liste.

Pour cela, nous pouvons **créer une nouvelle variable**, qui va compter le nombre de Pokémon en vie du joueur.

Et à chaque fin de combat entre 2 Pokémon, si le Pokémon du dresseur est KO, on peut retirer `1` à cette variable.

Et le combat continue tant que le dresseur a encore au moins 1 Pokémon en vie.
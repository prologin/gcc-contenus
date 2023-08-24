## Bonus

### Avec de la couleur !

Pour rendre ton jeu plus agréable à lire et à jouer, tu peux **changer la couleur des textes que tu affiches**.

Par exemple, lorsque ton Pokemon gagne un combat, on peut afficher la phrase "[...] a gagné !" en bleu, et si c'est le Pokemon adverse qui gagne, on peut l'afficher en rouge.

Ou encore, on peut afficher les phrases de victoire sur un dresseur en vert, de même que le soin de tes Pokemon.

Pour cela, nous allons rajouter un caractère spécial au début de la chaîne de caractères à afficher.

```python
print("\033[0;32m Félicitations !")
print("normal ?")
print("\033[0m Il faut reset la couleur")

print("\033[0;34m Comme ceci \033[0m")
print("ici tout va bien")
```

Les couleurs ne marchant pas sur notre site, copie colle les lignes ci-dessus et teste les sur ton ordinateurs.

{{% box type="info" title="Rappel sur les f-string" %}}

Python permet d'utiliser rapidement des variables dans les chaînes de caractères, avec ce qu'on appelle les f-string.

```codepython
a = 10
print(f"Il y a {a} bananes dans mon panier.")

price = 6
print(f"{a} bananes coûtent {price} euros.")
```

{{% /box %}}

Grâce aux f-string, il est possible de sauvegarder ces valeurs spécifiques dans des variables.

```python
red = "\033[0;31m"
reset = "\033[0m"

print(f"{red}Bravo!{reset}, vous avez réussi")
```

Il existe énormément de couleurs disponibles, voici une liste non exhaustive :
```python
BLACK = "\033[0;30m"
RED = "\033[0;31m"
GREEN = "\033[0;32m"
BROWN = "\033[0;33m"
BLUE = "\033[0;34m"
PURPLE = "\033[0;35m"
CYAN = "\033[0;36m"
GRAY = "\033[0;37m"
MAGENTA = "\033[0;95m"
RESET = "\033[0m"
```

### Voir les stats de ses Pokemons

Il peut être très pratique de connaître les statistiques de tes Pokemon, ne serait ce que pour savoir s'il faut aller les soigner, avant qu'ils ne tombent tous KO.

Pour cela, nous allons ajouter une **méthode dans la classe Dresseur**, qui peut s'appeller `affiche_stats`.

Cette méthode pourra parcourir tous les Pokemon du dresseur, et appeler une **nouvelle méthode de la classe Pokemon**, qui peut s'appeler `affiche_infos`.

La méthode `affiche_infos` peut afficher le nom du Pokemon, ainsi que son nombre de points de vie, son nombre de points de dégâts.

Un format possible d'affichage :
```text
Carapuce
  Vie : 24/24 | Dégâts : 13
```

Pour pouvoir l'utiliser dans la boucle de jeu, nous pouvons **ajouter une action** possible, par exemple avec le nom clé "equipe".  
Si le joueur entre "equipe", on affiche les statistiques des Pokemon du dresseur.

{{<figure src="resources/images/poke-stats.jpg" height=450 caption="">}}

### Rencontre avec des Pokemons et Dresseurs aléatoires

Pour ajouter plus de suspense dans ton jeu, tu peux rendre les rencontres avec des Pokemon sauvages ou des dresseurs ennemis plus aléatoires.

Tu peux par exemple, faire en sorte que le nombre de points de vie et nombre de dégâts varient.

Tu peux également rendre le nombre de Pokemon d'un dresseur ennemi aléatoire, potentiellement compris entre 1 et 3.

Tous ces aléatoires portent sur des nombres. On peut donc utiliser la même fonction qu'auparavant :
```codepython
import random

alea = random.randint(1, 3)
       # 1 et 3 sont compris dans les valeurs possibles
print(alea)
```

### Veux-tu donner un surnom à ton Pokemon ?

Pour que le dresseur puisse personnaliser son équipe, donnons lui la possibilité de donner des surnoms à ses Pokemon.

{{<figure src="resources/images/surnom.webp" height=300 caption="">}}

Lors de la phase de capture dans la boucle de jeu, demande au dresseur s'il souhaite donner un nom à son nouveau Pokemon !
```text
Veux-tu lui donner un nom ? 'oui' / 'non'
```

{{% box type="info" %}}

Pense à la fonction `input` !

{{% /box %}}

Si le joueur répond non, nous avons rien à modifier, le dresseur capture le Pokemon directement.

Si le joueur répond oui, nous devons ensuite lui demander quel nom il souhaite donner au Pokemon.  
Ensuite, on change le nom de celui-ci.

{{% box type="info" %}}

Il est possible de changer le nom du Pokemon, avant ou après l'appel à la méthode `capture`.

En effet, l'objet Pokemon sera donné en *référence* à la fonction `capture` et dans la liste `dresseur.pokemons`. Ce qui signifie que le même objet est utilisé à plusieurs endroits, et que s'il est modifié d'un côté, alors il sera aussi modifié de l'autre.

{{% /box %}}

### Potion

Lorsque l'on voyage, on peut faire de très longs chemins sans passer devant un centre Pokemon.

Pour revigorer ses Pokemon fatigués, il existe un certain objet, les `potion`. Celles-ci sont capables de redonner des points de vie à un Pokemon choisi.

Habituellement dans les jeux Pokemon, les potions sont mélangés aux autres objets dans le Sac du dresseur.  
Ici, nous allons utiliser qu'un seul type d'objets : les potions, donc nous allons les gérer spécifiquement.

Prenons des potions toutes simples, celle qui donne 20 points de vie à un Pokemon.

Toutes les potions étant les mêmes, nous pouvons gérer nos potions avec un simple entier, qui comptera le nombre de potions que le dresseur possède.

Pour utiliser une potion, nous allons créer la méthode `utilise_potion`.  
La potion s'utilisant sur un Pokemon précis, la méthode prendra un paramètre, qui permet de retrouver le Pokemon en question.  
Pour plus de simplicité, ce paramètre sera l'indice du Pokemon choisi dans la liste de Pokemon du dresseur.

À quel moment l'utiliser ?

Tu peux ajouter l'action d'utilisation d'une potion où tu le souhaites.  
Nous te conseillons d'ajouter directement l'action à la boucle de jeu, avec le mot-clé "potions".

Une fois l'action choisie, il faut demander au joueur sur quel Pokemon l'utiliser.

{{<figure src="resources/images/potion.gif" height=300 caption="">}}

{{% box type="exercise" %}}

Étapes à réaliser :
- ajouter un attribut `potions`, un entier, à la classe `Dresseur`
- créer la méthode `utilise_potion` qui prend en paramètre l'indice d'un Pokemon dans la liste du dresseur, et qui lui ajoute 20 points de vie
- ajoute l'action dans le jeu, pour pouvoir l'utiliser

{{% /box %}}

{{% box type="warning" %}}

Pense à retirer `1` à l'attribut lorsque la méthode `utilise_potion` est appelée.

Attention à ne pas dépasser le nombre de points de vie maximal des Pokemon.

Attention, lorsque le nombre de potions tombe à 0, il n'est plus possible d'en utiliser.

{{% /box %}}

Le joueur peut commencer la partie avec 2 potions.

### Pokemoney

Allons encore plus loin !

Grâce au bonus précédent, nous avons accès à un objet : les potions. Mais celles-ci sont à usage unique, donc rapidement épuisées.

Rajoutons un **système d'argent à notre jeu**, pour pouvoir en acheter !

L'argent serait possédé par le dresseur, et **acquis grâce à ses combats contre d'autres dresseurs**.

On peut par exemple donner 200 Pokédollar (monnaie des jeux Pokémon) au joueur au début de sa partie.

Ensuite, à chaque dresseur vaincu, on ajouterait 100 Pokédollar.

Attention, on retire également de l'argent lorsque le joueur perd un combat !

Enfin, le joueur doit pouvoir choisir d'**aller au PokeShop**, pour acheter des potions. Il nous faut donc rajouter une action à notre boucle de jeu, qui appelerait une nouvelle fonction : `visite_PokeShop`.

{{<figure src="resources/images/pokeshop.jpg" height=250 caption="">}}

Cette fonction ressemblerait à la fonction `visite_PokeCenter` dans sa forme :
- Souhaiter la bienvenue au dresseur
- Demander le nombre de potions que le joueur souhaites acheter en affichant le prix
- Remercier le joueur

Il faudra **vérifier que le joueur possède assez d'argent** pour acheter les potions demandées.

{{% box type="exercise" %}}

Étapes à réaliser :
- ajouter un attribut à la classe `Dresseur` pour gérer son argent
- ajouter de l'argent au joueur lorsque celui-ci bat un autre dresseur
- retirer de l'argent au joueur lorsque celui-ci est mis KO (attention à ne pas passer en négatif)
- coder la fonction `visite_PokeShop` qui permet au joueur d'acheter des potions avec son argent
- ajouter l'action d'aller au PokeShop dans la boucle de jeu

{{% /box %}}

### Pikachu monte au niveau 10 !

Rendons nos Pokemon encore plus forts et devenons Maître Pokemon !

Pour le moment, les Pokemon d'un dresseur ne s'améliorent pas avec les combats, ils restent avec leurs caractéristiques définies lors de la capture de chacun.

Faisons en sorte que les Pokemon du joueur deviennent les meilleurs.

Pour cela, ajoutons 2 caractéristiques :
- xp : pour les points d'expérience
- niveau : pour le niveau actuel d'un Pokemon

Au cours d'un combat, si un Pokemon met KO un autre Pokemon, alors il **gagne de l'expérience** (pourquoi pas le montant de la vie maximale du Pokemon adverse ?).

Lorsque l'expérience d'un Pokemon atteint un certain palier, par exemple 100 points, alors le Pokemon **monte de niveau** et devient plus puissant !

On peut ajouter une **nouvelle méthode** à la classe `Pokemon` : `augmente_niveau`.  
Cette méthode va :
- augmenter le niveau du Pokemon,
- remettre à 0 ses points d'expérience
- et augmenter chacune de ses caractéristiques, avec les valeurs que tu as choisies.

Ensuite, il ne reste plus qu'à appeler cette méthode lorsqu'un Pokemon dépasse le palier d'expérience suite à un combat contre un autre Pokemon (donc dans la méthode `combat` de la classe `Pokemon`).

{{<figure src="resources/images/level-up.gif" height=300 caption="">}}

---

Félicitations !

Tu es arrivée à la fin de ce projet Pokemon.

On espère que tu as aimé, n'hésite pas à nous faire des retours et à améliorer ton jeu avec tout ce qu'il te passe par la tête !

{{<figure src="resources/images/bye-pokemon.webp" height=300 caption="">}}
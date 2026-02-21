Ton jeu est quasi complet ! Félicitations ! 🎉

Nous allons maintenant créer la partie "chef d'orchestre" de notre jeu, l'endroit où le joueur va pouvoir choisir ce qu'il veut faire, la **boucle de jeu**.

## Dresseur et son starter

Premièrement, nous allons pouvoir **créer le dresseur** du joueur, avec son prénom.

Il nous faut donc :
- Demander son prénom
- Créer le dresseur

Avant de lui demander, on peut également commencer le jeu est souhaitant la bienvenue au joueur :
```text
Cher nouveau dresseur, bienvenue dans le monde Pokémon !
```

{{<figure src="resources/images/dresseuses.png" height=300 caption="">}}

Ensuite, il va pouvoir **choisir son Pokémon de départ**, son starter !

Le choix portera uniquement sur le nom du Pokémon. Ses statistiques seront fixes.  
On peut par exemple mettre 40 en points de vie et 12 en points de dégats.

Voici un exemple de dialogue pour le choix du starter, tu peux le modifier à ta guise :
```text
Choisis ton Pokémon de départ :
Comment s'appelle-t-il ?
Félicitations pour avoir choisi [...] !
```

{{<figure src="resources/images/starters.jpg" height=350 caption="">}}

## Choisir une action

Après la mise en place du joueur, celui-ci va pouvoir effectuer des actions, comme :
- aller au centre Pokémon
- voyager dans les hautes herbes (rencontre avec un Pokémon sauvage ou un Dresseur)

Voici un exemple de dialogue pour le choix des actions :
```text
Que souhaites-tu faire :
'voyager' ou aller au 'pokecenter' ?
```

### Visite du centre Pokémon

{{<figure src="resources/images/PokeCenter.png" height=300 caption="">}}

Si la réponse du joueur est "pokecenter", alors nous pouvons l'emmener au centre Pokémon, en utilisant la fonction `visite_pokecenter`.

### Voyager

Si le joueur choisit l'action "voyager", alors celui-ci se balade dans les hautes herbes.

{{<figure src="resources/images/voyager.gif" height=250 caption="">}}

Sur le chemin, il peut **croiser un Pokémon sauvage ou un Dresseur ennemi**.

Pour choisir entre les 2, nous pouvons utiliser de l'aléatoire.  
Générons un **nombre aléatoirement** entre 1 et 2, si celui-ci est égal à 1, alors le joueur rencontre un Pokémon sauvage, sinon le joueur rencontre un dresseur de la Team Rocket !

{{% box type="info" %}}

Il est très facile de générer un nombre aléatoirement, avec le module `random`.

Pour créer un nombre aléatoirement compris entre 2 nombres :
```codepython
import random  # à mettre au début du fichier

nombre = random.randint(0, 10)  # nombre aléatoire entre 0 et 10 compris
print(nombre)
```

{{% /box %}}

#### Pokémon sauvage

Si le joueur rencontre un Pokémon sauvage, plusieurs choix s'offrent à lui :
- le capturer
- le combattre
- fuire

Tout d'abord, créons un Pokémon, celui qui vient d'apparaître devant le joueur.  
Par exemple, ce Pokémon peut s'appeler "Rattata", et avoir 20 points de vie et 8 points de dégâts.

On peut également afficher au joueur quel Pokémon il vient de rencontrer :
```text
Un [nom du pokemon] sauvage apparaît !
```

Ensuite, nous lui demandons ce qu'il veut faire :
```text
Souhaites-tu le 'capturer', se 'battre' ou 'fuire' ?
```

Si le joueur souhaite capturer le Pokémon, on peut simplement appeler la méthode `capture` de la classe `Dresseur` avec ce Pokémon.
```text
Tu as capturé [nom du pokemon] !
```

Si le joueur souhaite se battre contre le Pokémon, on peut appeler la méthode `combat` de la classe `Dresseur` avec ce Pokémon.

Sinon, le joueur fuit le Pokémon, aucune action n'est faite.
```text
Tu as pris la fuite...
```

#### Team Rocket

Si le joueur rencontre un dresseur ennemi sur son chemin, celui-ci provient certainement de la Team Rocket !

Créons ce dresseur, et donnons lui de nouveaux Pokémon, disons 2 Pokémon assez faibles : 25 points de vie et 10 points de dégâts.

Ensuite appelons la méthode `duel` de la classe `Dresseur` pour le battre !

#### Après un combat

Le joueur peut se retrouver avec tous ses Pokémon KO suite à un combat, contre un Pokémon sauvage, ou un dresseur de la Team Rocket.

Dans cette éventualité, le joueur doit courir vers le centre Pokémon le plus proche pour les soigner, ce que nous pouvons forcer :
```text
Tu cours vers un centre Pokémon pour soigner tes Pokémon.
```
Ensuite, on appelle la fonction `visite_pokecenter`.

### Autre

Si le joueur entre un nom d'action différent de 'voyager' ou 'pokecenter', cette action n'est pas reconnue par notre programme.

Nous pouvons lui signifier avec la phrase :
```text
Je n'ai pas compris ce que tu voulais faire.
```

<br>

{{% box type="info" %}}

Une structure conditionnelle nous permet de récupérer tous les autres cas en Python.

Rappelons que :
- `if`, signifie "si" en français, et permet de tester une condition, avant de faire des actions
- `else`, signifie "sinon" en français, et permet d'exécuter des actions, si la condition du `if` précédent est fausse
- `elif`, est la contraction de `else` et `if`, "sinon si" en français, et permet d'exécuter des actions si les conditions précédentes sont fausses et que la condition actuelle est vraie.

```codepython
heures = 2.5
if heures < 1:
    print("Ce cours est très court !")
elif heures < 2:
    print("C'est le temps parfait.")
elif heures < 3:
    print("Ce cours est long...")
else:
    print("Ce cours est interminable :'(")
```

{{% /box %}}

En utilisant cette structure pour comparer nos actions, nous pouvons récupérer toutes les actions non reconnues dans la partie `else`.

## Boucle de jeu

Après avoir lié la réponse du joueur aux actions qu'il va effectuer, il ne nous reste plus qu'à faire en sorte que le jeu ne s'arrête pas. Il continue tant que le joueur souhaite jouer.

Pour cela, nous allons créer une **boucle de jeu**.

Ne connaissant pas le nombre de tours de boucle que le joueur souhaite faire à l'avance, ce sera une boucle `while` et non une boucle `for`.

On peut créer **une variable `en_cours` qui décide si le jeu doit continuer, ou s'arrêter**.

Elle sera la condition de la boucle `while`, ainsi les instructions de la boucle se répéteront tant que `en_cours` vaut `True`, et la boucle s'arrête lorsque `en_cours` vaut `False`.

La variable `en_cours` est initialisée à `True` au début du jeu.

### Qu'est ce qu'on veut répéter ?

Pour savoir où mettre la boucle, et définir les lignes qui doivent se répéter, nous devons relire notre programme.

Tout d'abord, nous avons créé un dresseur, avec le nom du joueur.  
Est ce qu'il faut créer plusieurs dresseurs pour le joueur pendant la partie ?  
Non, un seul suffit. Donc cette partie ne sera pas dans la boucle.

Ensuite, nous avons défini le Pokémon de départ du joueur.  
Est ce qu'il aura plusieurs Pokémon de départ ?  
Non, il peut ensuite en capturer lors de ses voyages. Donc cette partie ne sera pas dans la boucle.

Après, nous demandons au joueur quelle action il souhaite faire (voyage ou centre Pokémon).  
Est ce qu'il peut faire plusieurs actions lors du jeu ?  
Oui ! **Donc nous allons commencer la boucle juste avant de demander l'action que le joueur souhaite faire**.

### Quitter le jeu

Pour pouvoir quitter le jeu, maintenant que celui-ci se répète, nous pouvons ajouter un nouveau choix d'actions : "quitter".

Si la réponse du joueur est "quitter", alors nous pouvons changer la valeur de la variable `en_cours`, valeur qui va arrêter la boucle.

{{<figure src="resources/images/Pokemon-logo.png" height=150 caption="">}}

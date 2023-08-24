---
show_toc: true
---

Félicitations pour être arrivée jusqu'ici ! Tu as pu apprendre à faire tes premiers programmes, et à utiliser des types complexes comme les listes.

Nous allons à présent te parler de Programmation Orientée Objet (POO), ou plus simplement d'objets et de classes.

Et nous allons introduire ce sujet avec les très célèbres **Pokémon** !

{{<figure src="resources/images/pokemons.jpg" height=300 caption="">}}

Le but de ce TP sera de créer ton propre mini jeu Pokémon.

## Pourquoi on a besoin de programmation objet pour notre jeu ?

Tout d'abord, réfléchissons à ce que nous voulons mettre dans un jeu Pokémon.

Nous aurons besoin :
- d'avoir plusieurs Pokémon,
- de leur donner des noms,
- nous voulons également les capturer,
- s'affronter avec les autres dresseurs,
- etc

Pour pouvoir faire tout ça, nous allons avoir besoin de définir une manière de représenter un Pokémon.

{{<figure src="resources/images/pika.png" height=230 caption="Pika !">}}

Comment définir un Pokémon ? Qu'est ce qui le caractérise ?

Nous pouvons donner un nom à un Pokémon, pour qu'il soit facilement reconnaissable.
Il aura également un nombre de points de vie, et un nombre de points d'attaque.

Pour faire simple, on va se limiter à ces caractéristiques dans ce mini jeu. Vous trouverez [ici](https://fr.wikipedia.org/wiki/Syst%C3%A8me_de_jeu_de_Pok%C3%A9mon) la liste des caractéristiques du jeu original.

Pour résumer, pour chaque Pokémon que nous utiliserons dans notre jeu, il faut qu'on définisse 3 variables (nom, points de vie, attaque).
Facilement faisable si nous avons 1, 2, voire 3 Pokémon, mais ensuite ça va devenir très dur de s'y retrouver.

Une manière simple en programmation pour ce genre de problèmes est la **programmation orientée objet**. Elle utilise la notion d'**objet qui rassemble variables et opérations**.

## Premier objet

Un **objet** est assimilé à une variable et le type d'un objet est appelé **classe**.

Définir une classe revient à créer un **nouveau type de variable**.

{{< codestep steps=2 lang="py" desc="" >}}

{{< codestep-block desc="Créons la classe `Pokemon`" >}}
class Pokemon:
    def __init__(self):
        pass
{{< /codestep-block >}}

{{< codestep-block desc="`pokemon1` est un **objet** de la **classe** `Pokemon`" >}}
pokemon1 = Pokemon()
{{< /codestep-block >}}

{{< /codestep >}}

Grâce à ce petit bout de code, nous avons créé notre première classe et notre premier objet !

## Une méthode

```python
class Pokemon:
    def __init__(self):
        pass
```

La fonction `__init__()` est définie à l'**intérieur de la classe** `Pokemon`. On le voit grâce à l'indentation avant le mot-clé `def` (qui définit une fonction), sous la définition de la classe `Pokemon`.

`__init__()` est donc une **méthode**.

Voici d'autres exemples de méthodes :
```codepython
class Toto:
    def __init__(self): # une méthode de Toto
        pass
    def affiche_oui(self): # une autre méthode de Toto
        print("OUI!!!!")

    def nope(self): # encore une autre méthode de Toto
        print("ah non hein")

def f(): # simple fonction
    print("pourquoi ? :'(")

toto = Toto()
toto.affiche_oui()
print("Bonbons ?")
toto.nope()
f()
```

### Paramètres d'une méthode

Il est possible d'ajouter autant de paramètres que l'on souhaite à une méthode, tout comme on le ferait pour une fonction :

```codepython
class Toto:
    def __init__(self):
        pass
    def peut_etre(self, oui, non):
        if oui > non:
            print("Yes !")
        else:
            print("Dommage...")

toto = Toto()
toto.peut_etre(10, 3)
print("Et pour l'autre ?")
toto.peut_etre(10, 50)
```

### Constructeur d'un objet

Nous avons dit précédemment que `__init__()` était une méthode, c'est même une méthode particulière en Python.

La méthode `__init__()` est la méthode **constructeur** des objets de la classe.

Cette méthode peut également prendre plusieurs paramètres.

C'est la fonction appelée par Python lorsqu'on écrit `toto = Toto()`:

```codepython
class Toto:
    def __init__(self):
        print("Félicitations pour avoir créer un objet !")

toto = Toto()
```

### Mais qu'est ce que `self` en paramètre des méthodes ?

Le mot-clé `self` est toujours le **1er paramètre** d'une méthode.

Il permet de **représenter l'objet**, pour l'utiliser à l'intérieur de la méthode.

On peut l'utiliser notamment pour définir les **attributs** d'un objet.

## Les attributs d'un objet

Un attribut est une **variable** contenue dans un objet.

L'accès à un attribut se fait depuis l'objet.

Au lieu de définir plusieurs variables à différents endroits, on les stocke toutes dans un objet :

```codepython
# avec plusieurs variables
nom = "Salamèche"
age = 5
taille = 0.8
joie = 6
entrainement = 0

# avec un objet
class FirstPokemon:
    def __init__(self):
        self.nom = "Salamèche"
        self.age = 5
        self.taille = 0.8
        self.joie = 6
        self.entrainement = 0

objet = FirstPokemon()
print(objet.nom)
print(objet.age)
print(objet.taille)
print(objet.joie)
print(objet.entrainement)

print("après:")

# modifier un attribut
objet.entrainement = 3
print(objet.entrainement)
```


{{% box type="info" %}}

Un attribut peut être récupéré et modifié par tout élément ayant accès à l'objet dans lequel il est contenu.

{{% /box %}}

Si on reprend une méthode, elle peut y accéder avec `self` :

```codepython
class Toto:
    def __init__(self, nom):
        self.nom = nom
        self.age = 10
    def presentation(self):
        print("Je m'appelle", self.nom)
        print("J'ai", self.age, "ans.")

toto = Toto("TOTO")
toto.presentation()
```


{{% box type="exercise" title="Créons un Pokémon !" %}}

Ayant appris à créer un objet, passons à la pratique !

Crée un Pokémon, avec :
- un surnom,
- un nombre de points de vie,
- et une puissance d'attaque,

donnés dans le constructeur (`__init__()`).

Et affiche le nom du Pokémon créé !

{{% /box %}}
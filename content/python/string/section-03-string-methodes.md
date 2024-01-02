# Méthodes sur les string

Python met à disposition plusieurs méthodes sur les chaînes de caractères, qui permettent plus de fonctionnalités et d'efficacité sur l'utilisation des string.

## lower

`lower()` : Renvoie la chaîne de caractères en transformant les lettres majuscules en lettres minuscules :
```codepython
print("GCC!".lower())

nom = "Joseph Marchand, membre Prologin"
print(nom.lower())
```

## upper

`upper()` : Renvoie la chaîne de caractères en transformant les lettres minuscules en lettres majuscules :
```codepython
prenom = "Joseph"
nom = "Marchand"
print("Bonjour", prenom, nom.upper())
```

## split

`split()` : Découpe la chaîne de caractères en plusieurs éléments, regroupés dans une liste, en utilisant comme séparateur les "espaces blancs" (les espaces, retour à la ligne, tabulation, etc)
```codepython
phrase = "Bienvenue au stage"
liste_mot = phrase.split()
print(liste_mot)

ip = "127.0.0.1"
numeros = ip.split('.')
print(numeros)

conjugaison = "je joue, tu joues, il joue, nous jouons, vous jouez, ils jouent"
individuel = conjugaison.split(', ')
print(individuel)
```

Comme le montre l'exemple précédent, il est également possible de couper sur une chaîne de caractères précise, donnée en paramètre.

## join

`join()` : Concatène les éléments de la liste donnée en paramètre les uns à la suite des autres, en intercalant entre chaque un séparateur donné lui aussi en paramètre, qui peut être n'importe quelle chaîne de caractères.

```codepython
sujets = ["intro", "listes", "string"]
chaine = "; ".join(sujets)
print(chaine)
```

## strip

`strip()` : Enlève n'importe quelle combinaison « d'espace(s) blanc(s) » sur les bords d'une chaîne de caractères.

```codepython
chaine = " \t  Il y a \t trop    d'espaces;   \n"
print(chaine.strip())
```

{{% box type="exercise" title="Exercice 3" %}}

Des études de discours de personnages célèbres montrent qu'ils ont tendance à répéter plusieurs fois les mots, pour se faire comprendre et marquer leurs intentions.

Trouve le mot le plus utilisé dans la citation ci-dessous.

```text
« Avec cette foi, nous serons capables de travailler ensemble,
de prier ensemble, de lutter ensemble, d'aller en prison ensemble,
de défendre la liberté ensemble. » (Martin Luther King Jr.)
```

Combien de fois ce mot est utilisé ? Calcule-le en Python en utilisant la méthode `split()` et la comparaison de mot.

{{% /box %}}
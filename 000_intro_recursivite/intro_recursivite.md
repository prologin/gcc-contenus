---
date: 2021
author: Dorian Péron
---

# Récursivité

> Prérequis: aucun

## Introduction

Le principe de récursivité est fondamental en informatique. Il permet de résoudre de nombreux problèmes que nous allons pouvoir aborder dans ce sujet.

Un exemple de phénomène que l'on pourrait qualifier de récursif est le fait de se placer entre 2 miroirs qui se font face. En regardant le miroir 1, on voit ce qu'il y a dans le miroir 2, qui réfléchi l'image du miroir 1 en plus petit, qui lui même réfléchi l'image du miroir 2 en plus petit etc...

![Un miroir face à un miroir](imgs/rec_mirror.jpg){width=0.7\linewidth}

Voici un example de fonction récursive qui permet de compter à rebours de n à 0:

```python
def countdown(n):
    print(n)
    if n > 0:
        countdown(n - 1)

>>> countdown(3)
3
2
1
0

>>> countdown(0)
0
```

Comme vous l'avez remarqué, la fonction `countdown` s'appelle elle-même si `n` est supérieur à 0. C'est ce qu'on appelle un **appel récursif**. La condition `n > 0` est appelée la **condition d'arrêt**. On remarque également que l'on rappelle `countdown` avec l'argument `n - 1`, car si l'on gardait `n` le programme entrerait dans une boucle infinie avant de planter par manque de mémoire dans l'ordinateur.

Voici maintenant une petite variante de la fonction `countdown`:

```python
def countup(n):
    if n > 0:
        countup(n - 1)
    print(n)

>>> countup(5)
0
1
2
3
4
5
```

Comme vous le remarquez, la structure de `countup` est très similaire à `countdown` et pourtant `countup` compte de manière croissante (de 0 à `n`). Cela est dû au placement de notre appel récursif dans la fonction. Dans `countdown`, on affiche d'abord n, puis on fait l'appel récursif avec `n - 1`, alors que dans `countup`, on commence par faire l'appel récursif, puis une fois cela terminé, on affiche n.

Vous maîtrisez maintenant les bases de la notion de récursivité

## À vos claviers

### **Exercice 1 : Factorielle**

La fonction factorielle est une fonction mathématique représentée par un point d'exclamation placée derrière un nombre (`3!` par exemple). Cette fonction correspond au produit de tous les entiers naturels à partir de 1 jusqu'à n (aussi on fixe `0! = 1`).

Exemples:

```text
1! = 1
2! = 1 * 2 = 2
...
5! = 1 * 2 * 3 * 4 * 5 = 120
...
```

En observant cette fonction, on remarque par exemple que `5! = 5 * 4! = 5 * (4 * 3!)` etc...
D'une manière générale on sait que:

```text
n! = | 1            si n = 0 ou n = 1
     | n * (n - 1)! sinon
```

Le but de cet exercice est d'implémenter la fonction `facto(n)` qui implémente la fonction factorielle.

```python
def facto(n):
    # FIXME
```

### **Exercice 2 : Suite de Fibonacci**

La suite de Fibonacci est une suite mathémathique définie de la manière suivante :

```text
fibo(n) = | n                           si n = 0 ou n = 1
          | fibo(n - 1) + fibo(n - 2)   sinon
```

But de l'exercice: implémenter la fonction `fibo(n)`.

> ⚠ Pendant vos tests, ne dépassez pas fibo(30), car cela deviendra très long à calculer.

> ℹ La suite de Fibonacci est par nature récursive, mais il existe un moyen itératif bien moins coûteux pour calculer les valeurs de cette suite ! (Nous ne l'abordons pas dans ce TP mais cela peu être un challenge intéressant).

### **Exercice 2.1 (Bonus) : Fonction d'Arckermann**

But de l'exercice : implémenter la fonction d'Ackermann définie ci dessous:

```txt
            | n + 1                     si m = 0
ack(m, n) = | ack(m - 1, n)             si m > 0 et n = 0
            | ack(m - 1, ack(m, n - 1)) si m > 0 et n > 0
```

### **Conclusion**

Voici qui conclus notre introduction à la récursivité. Afin d'approfondir cette notion, vous pouvez vous diriger vers les TPs sur les arbres ou sur les fractales. Bonne chance !

## Sources

[Wikipédia : Algorithme récursif](https://fr.wikipedia.org/wiki/Algorithme_r%C3%A9cursif)

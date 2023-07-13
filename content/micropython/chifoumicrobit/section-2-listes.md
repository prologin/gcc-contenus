# Passons à la pratique !

Nous t'invitons d'abord à télécharger le code source à modifier en cliquant
sur le bouton `Code à compléter` en haut de la page ! Tu retrouveras dans
le fichier donné un code non complet que tu ne peux pas encore lancer.

{{% box type="warning" title="Code incomplet !" %}}

Différentes parties du code sont manquantes ! Elles sont désignées par le mot-clé
`TODO` qui se traduit par "À faire" en français. Tout au long du sujet, tu vas
pouvoir compléter le code en écrivant juste en dessous des commentaires
(les lignes de code commençant par un `#`).

{{% /box %}}

## Les possibilités d'affichage

Au début du code donné, tu trouveras la variable `possibilites`, tu vas devoir
t'en servir pour stocker les trois images que l'on veut pouvoir afficher :
`Image.SKULL`, `Image.PACMAN` et `Image.GHOST`. Cependant, il nous faut trouver
une manière pour stocker trois valeurs dans une seule variable. Pour cela, tu
vas utiliser ce qu'on appelle une liste.

{{% box type="info" title="Mais comment construit-on une liste en Python ?" %}}

Lorsqu'on veut stocker de nombreuses valeurs pour pouvoir les réutiliser
par la suite, on utilise des listes. Elles vont nous permettre de stocker
plusieurs valeurs dans une seule variable.

{{<figure src="resources/images/liste.png" height=80% width=80% alt="Liste en Python">}}

Par exemple,

```python
# Liste de lettres
ma_liste_lettres = ["a", "b", "c", "d"]
```

Tu peux accéder aux éléments d'une liste à l'aide de l'indice. Ce sont des nombres
qui désignent l'emplacement de la case que tu veux regarder. Attention,
en programmation, les indices commencent à 0. Si on nomme la longueur de la liste `l`,
les indices peuvent prendre des valeurs entre `0` et `l - 1`.

En Python, pour accéder à un élément à l'indice 2, tu peux faire comme ceci :

{{< codestep steps=5 lang="py" >}}

{{< codestep-block desc="Initialise une liste de lettres" >}}
ma_liste_lettres = ["a", "b", "c", "d"]
{{< /codestep-block >}}

{{< codestep-block desc="Récupère la 3<sup>ème</sup> valeur de la liste" >}}
ma_variable = ma_liste_lettres[2]
{{< /codestep-block >}}

{{< codestep-block desc="Affiche `c`" >}}
print(ma_variable)
{{< /codestep-block >}}

{{< codestep-block desc="Calcule la longueur de la liste" >}}
longueur = len(ma_liste_lettres)
{{< /codestep-block >}}

{{< codestep-block desc="Affiche `4`" >}}
print(longueur)
{{< /codestep-block >}}

{{< /codestep >}}

{{% /box %}}

{{% box type="exercise" title="Exercice 1 : Les différentes possibilités" %}}

Dans la liste `possibilites`, rajoute les trois images représentant les
différents choix possibles (`Image.SKULL`, `Image.PACMAN` et `Image.GHOST`). Tu
vas devoir également trouver la longueur de ta liste `possibilites`. Pour
cela, sers-toi de la fonction `len`. Tu dois mettre ce nombre dans la variable
`NB_POSSIBILITES`.

{{% /box %}}
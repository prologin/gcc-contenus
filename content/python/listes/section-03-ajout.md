# Ajouter des éléments dans une liste

Une des opérations importantes sur les listes est la possibilité d'**ajouter des
éléments** dans cette dernière. Il existe deux manières différentes d'effectuer
l'ajout.

## Ajouter à la fin d'une liste

Il est possible d'**ajouter des éléments** dans une liste **à la fin** de cette
dernière. On dit qu'on modifie la queue de la liste. On utilise alors la méthode
`append`.

```codepython
ma_liste = ['a', 'b', 'c']

# Affiche `ma_liste`
# `print` est une fonction
print(ma_liste)

# Ajoute l'élément 'd' à `ma_liste`
# `append` est une méthode
ma_liste.append('d')

# Affiche `ma_liste`
print(ma_liste)
```

{{% box type="info" title="Méthodes et fonctions" %}}

Les **méthodes** et les fonctions sont deux choses très similaires en
programmation.

Sur l'[Introduction à Python](https://tp.girlscancode.fr/python/intro_python/),
tu as pu découvrir les fonctions. Elles sont définies avec le mot-clé `def`,
elles prennent des paramètres et sont appelées avec des arguments.

Les **méthodes** reprennent les mêmes codes que les fonctions. La principale
différence réside sur la manière d'appeler une méthode. Pour appeler une
méthode, il faut spécifier impérativement **sur quel objet (variable)** porte la
méthode. Pour appeler une méthode, on utilise la syntaxe
`variable.methode(argument1, argument2, ...)` avec :

- `variable`, l'objet sur lequel on veut appliquer la méthode ;
- `methode`, le nom de la méthode utilisée ;
- `argument1, argument2, ...`, les arguments de la méthode (il peut ne 
pas y en avoir).

{{% /box %}}

{{% box type="exercise" title="Mission 3 : Préparation de la valise" %}}

Julie a vraiment hâte de partir en vacances ! Cependant, elle doit d'abord
remplir sa valise pour pouvoir profiter de ses vacances.

Crée une liste `valise_julie` qui correspondra à la valise de Julie. Elle doit
déjà contenir les chaînes de caractères suivantes : `"t-shirts"` et
`"pantalons"`.

Utilise la fonction `print` pour vérifier le contenu de la valise actuellement.

Après avoir vérifié le contenu, tu fais remarquer à Julie qu'elle a oublié des
affaires ! Ajoute les éléments `"tongs"`, `"casquette"` dans la valise et
affiche le contenu à la fin pour vérifier que tu as tout !

{{% /box %}}

{{% box type="exercise" title="Mission 4 : Entrée et liste" %}}

Julie vient de remarquer qu'elle a oublié d'acheter de la crème solaire pour ses
vacances !

Par chance, il est possible de commander sur Internet des choses en utilisant la
fonction `input` que tu as pu voir dans
l'[Introduction à Python](https://tp.girlscancode.fr/python/intro_python/).

Utilise-la pour demander à l'utilisateur *"Que voulez-vous commander ?"* et
ajouter l'élément dans la liste `valise_julie` que tu as pu créer dans la
mission précédente.

</br>

<details>
<summary>Clique ici si tu ne te souviens pas de l'utilisation de la fonction input !</summary>

On peut **lire et récupérer du texte** en demandant à l'utilisateur de répondre
à une question en utilisant l'instruction `input`. On peut alors garder en
mémoire la réponse de l'utilisateur dans une variable.

```codepython
# Demande à l'utilisateur "Quel est ton prénom ?"
prenom = input("Quel est ton prénom ?")

# Affiche la réponse de l'utilisateur
print(prenom)
```

</details>

{{% /box %}}

{{% box type="exercise" title="Mission 5 : C'est maintenant au tour de ta valise !" %}}

C'est maintenant à ton tour de remplir ta valise. Pour cela, on va utiliser le
même principe que sur la mission précédente. Pour cela, tu devras **demander**
à Julie quels articles tu dois rajouter dans ta valise en utilisant la fonction
`input`.

Tu sais qu'il y aura **6 objets** à mettre dans ta valise. Tu peux alors
utiliser les *boucles `for`* pour répondre à ton besoin.

Crée une liste `ma_valise` vide que tu rempliras petit à petit. Pour demander à
Julie quel élément tu dois rajouter dans ta valise, tu peux lui poser la
question *"Que dois-je rajouter ?"*.

Vérifie le contenu de ta valise petit à petit en l'**affichant** après avoir
ajouté un élément.

<details>
<summary>Clique ici pour avoir un rappel sur les boucles for !</summary>

La boucle `for` est utile lorsque tu sauras **combien de fois** tu veux répéter
tes instructions.

```codepython
# Répète 5 fois l'action d'afficher "Prologin !"
for i in range(5):
    print("Prologin !")
```

Le nombre indiqué dans les parenthèses du mot-clé `range` indique le nombre de
répétitions des instructions.

</detail>

{{% /box %}}

## Ajouter un élément à un certain indice

En utilisant la méthode `insert`, il est possible d'ajouter un élément à une
**position précise**.

```codepython
# Crée une liste `ma_liste`
ma_liste = ['a', 'c', 'd']

# Ajoute l'élément 'b' à l'indice 1
ma_liste.insert(1, 'b')

# Affiche `ma_liste`
print(ma_liste)
```

Il est également possible d'ajouter un élément **à la fin** de la liste en
utilisant la méthode `insert`.

```codepython
# Crée une liste `ma_liste`
ma_liste = ['a', 'b']

# Ajoute l'élément 'c' à l'indice 2,
# à la fin de la liste
ma_liste.insert(2, 'c')

# Affiche `ma_liste`
print(ma_liste)
```

{{% box type="warning" title="Attention aux indices !" %}}

Comme pour accéder à un élément dans une liste, il faut faire attention que ce
dernier **ne dépasse pas les limites** de la liste.

Pour une liste contenant 3 éléments, les indices possibles pour utiliser la
méthode `insert` sont `0`, `1`, `2` et `3`.

{{< figure src="./resources/images/insert.png" caption="Insertion d'un élément" >}}

{{% /box %}}

{{% box type="exercise" title="Mission 6 : Planning des vacances" %}}

Julie a déjà préparé un planning pour les vacances. Cependant, tu voudrais
ajouter à ce programme quelques activités de loisirs dans un ordre précis.
Le planning est représenté par la liste `planning` décrite ci-dessous. Tu
voudrais insérer ces activités :

- `"Balade en ville"` avant le voyage retour ;
- `"Plage"` après le voyage aller ;
- `"Glace"` entre la présentation des stages GCC! et le restaurant.

```python
planning = ["Voyage aller", "Présentation des GCC!", "Restaurant", "Voyage retour"]
```

{{% /box %}}

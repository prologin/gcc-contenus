## Les boucles

En programmation, il est souvent utile de répéter certaines actions un certain
nombre de fois ou tant qu'une condition est vérifiée. Il existe alors les
**boucles** qui peuvent répondre à cette problématique.

### Tant que

La boucle **while** (*tant que* 🇫🇷) est une boucle dont le bloc de code est
répété tant qu'une condition est vérifiée. On l'écrit similairement à des
conditions `while condition:`. On peut trouver des examples dans la vie
courante :

{{<figure src="resources/images/algo-while.png" caption="Algorithme avec l'utilisation d'une boucle tant que" >}}

Illustrons cette boucle à travers un exemple de code :

{{< codestep steps=5 lang="py" run="true" >}}

{{< codestep-block desc="Garde en mémoire le nombre secret" >}}
nombre_secret = 8
{{< /codestep-block >}}

{{< codestep-block desc="Demande à l'utilisateur un nombre et le garde en mémoire" >}}
entree = input("Choisis un nombre entre 1 et 10 : ")
nombre_entree = int(entree)
{{< /codestep-block >}}

{{< codestep-block desc="Tant que le nombre secret est différent au nombre entré, on répète les prochaines instructions" >}}
 
while nombre_secret != nombre_entree:
{{< /codestep-block >}}
    
{{< codestep-block desc="Demande à l'utilisateur un nouveau nombre" >}}
    print("Le nombre n'a pas encore été trouvé !")
    entree = input("Choisis un nombre entre 1 et 10 : ")
    nombre_entree = int(entree)
{{< /codestep-block >}}

{{< codestep-block desc="Dès que la condition de la boucle `while` est fausse, on a trouvé le nombre secret et on affiche un message" >}}
 
print("Bravo, tu as trouvé le nombre secret !")
{{< /codestep-block >}}

{{< /codestep >}}

{{% box type="exercise" title="Mission 5 : Dessert, dessert..." %}}

Après avoir mangé ton menu, tu as encore faim ! Tu as particulièrement aimé le
tiramisu et tu voudrais en manger tant qu'il te reste de l'argent ! Il te reste
37,40 € et le tiramisu est à 5.49 € !

Pour cela, commande des tiramisus tant que la valeur de ton porte-monnaie moins
le prix d'un tiramisu est supérieur à 0 ! Pour commander des tiramisus, tu peux
appeler le serveur en affichant *"Un autre tiramisu s'il vous plaît !"*.
N'oublie pas d'enlever le prix d'un tiramisu à ton porte-monnaie à chaque fois
que tu commandes ! Lorsque tu n'as plus d'argent, tu peux afficher
*"Merci chef !"*.

{{% /box %}}

### Pour un certain nombre de fois

Il existe une autre manière de créer une boucle. La boucle `while` est pratique
pour répéter une action tant qu'une condition vérifiée. La boucle `for` te sera
utile lorsque tu sauras **combien de fois** tu veux répéter tes instructions.

```codepython
# Répète 5 fois l'action d'afficher "Prologin !"
for i in range(5):
    print("Prologin !")
```

Le nombre indiqué dans les parenthèses du mot-clé `range` indique le nombre de
répétitions des instructions. Voici un petit schéma pour bien différencier les
différents blocs de code : 

{{<figure src="resources/images/for_loop.png" caption="Blocs de code dans une boucle for" >}}

{{% box type="info" title="La fonction `range` "%}}

La fonction `range` permet de créer une suite de nombres qui peut être utilisée
dans une boucle. La fonction peut-être utilisée de plusieurs manières
différentes.

{{< codestep steps=3 lang="py" >}}

{{< codestep-block desc="Prends les valeurs entre **0** et **5** : 0, 1, 2, 3, 4, 5 (et donc 6 valeurs au total)" >}}
range(6)
{{< /codestep-block >}}

{{< codestep-block desc="Prends les valeurs entre **1** et **5** : 1, 2, 3, 4, 5" >}}
range(1, 6)
{{< /codestep-block >}}

{{< codestep-block desc="Prends les valeurs entre **1** et **5** avec un pas de **2** : 1, 3, 5 " >}}
range(1, 6, 2)
{{< /codestep-block >}}

{{< /codestep >}}

{{% /box %}}

{{% box type="info" title="À quoi correspond `i` ?" %}}

`i` est une variable qui existe seulement dans notre boucle `for`. Elle
correspond aux différentes valeurs des suites créées par la fonction `range`.
À chaque fois que l'ordinateur va répéter les actions dans la boucle, il va
prendre successivement les valeurs de la fonction `range`. Voici un petit
exemple :

```codepython
for i in range(5):
    # Affiche la valeur de `i` à chaque tour de boucle
    print("Numéro de répétition :", i)
```

`i` étant une variable, tu peux changer son nom si tu en as envie :

```codepython
for un_autre_nom in range(3):
    print(un_autre_nom)
```

Si tu n'as pas compris cette partie, n'hésite pas à appeler un organisateur !

{{% /box %}}

{{% box type="exercise" title="Mission 6 : Le long périple..." %}}

En remerciant le chef de la Prolotaverne, il te remet une liste d'instructions
pour aller à un trésor caché ! Tu le remercies et tu décides de suivre son
parchemin !

> Chère aventurière, j'ai caché mon trésor dans un temple dissimulé dans la
> forêt... Si tu oses aller à sa recherche, prends garde aux différents monstres
> sur le chemin... Utilise les coordonnées `x` et `y` pour retrouver mon
> précieux !
> 
> Pour trouver mon trésor, il te suffit de répéter 7 fois les instructions
> suivantes :
> - Vers la droite je vais durant 3 pas, en ajoutant 3 à `x`...
> - Vers le haut je me dirige durant 2 pas, en ajoutant 2 à `y`...
> - "Kawabounga !" je crierai en utilisant la fonction `print` pour éloigner les
> monstres !
> 
> Prend garde à toi aventurière !

Sachant que tu te trouves aux coordonnées `x = 0` et `y = 0`, quelles sont les
coordonnées du trésor ?

{{% /box %}}

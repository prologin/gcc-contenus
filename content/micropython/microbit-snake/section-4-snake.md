# Notre version de Snake sur `micro:bit`

## Le serpent

### Création

Dans notre code, nous allons représenter le serpent comme une liste de coordonnées sur l'écran. Ces coordonnées sont composées de 2 valeurs : une position sur l'axe X et une autre sur l'axe Y. Pour pouvoir regrouper les coordonnées entre elles, nous utiliserons les **tuples**.

{{<figure src="resources/images/microbit_axes.png" width=500 caption="Le pixel aux coordonnées (2, 4) est allumé">}}

Sur le `micro:bit`, on représente l'axe X à l'horizontal et l'axe Y à la verticale. Le pixel en haut à gauche est aux coordonnées `(0, 0)``.

{{% box type="info" title="Les tuples en bref" %}}

Un tuple c'est un couple de valeurs. Nous allons alors avoir deux valeurs assignées à une seule variable, comme une petite liste de deux éléments.
Comme toujours, un petit exemple ne fait jamais de mal :


{{< codestep steps=5 lang="py" >}}

{{< codestep-block desc="Création du tuple">}}
mon_tuple = (1, 2)
{{< /codestep-block >}}

{{< codestep-block desc="Affiche : (1, 2)" >}}
print(mon_tuple)
{{< /codestep-block >}}

{{< codestep-block desc="Affiche : 1">}}
print(mon_tuple[0])
{{< /codestep-block >}}

{{< codestep-block desc="Affiche : 2">}}
x = mon_tuple[1]
print(x)
{{< /codestep-block >}}

{{< codestep-block desc="Affiche : (9, 4)">}}
mon_tuple = (9, 4)
print(mon_tuple)
{{< /codestep-block >}}

{{< /codestep >}}


{{% box type="warning" %}}
Attention, tu ne peux pas modifier une seul valeur d'un tuple !
```codepython
mon_tuple = (5, 6)
mon_tuple[0] = 8 #Erreur
```
{{% /box %}}
{{% /box %}}


Notre serpent est donc une liste de tuples de nombres entiers, où chaque tuple donne les coordonnées d'une partie du corps du serpent. On a donc les coordonnées de la tête au début de la liste, et les coordonnées de la queue ensuite.

```python
serpent = [(2, 2), (2, 3), (3, 3), (3, 4)]
longueur_serpent = 4 # Le serpent a une taille de 4 cases
```

L'exemple ci-dessus correspond au serpent sur l'image suivante (la tête est le pixel le plus lumineux en coordonnées `(2, 2)`).

{{< figure src="resources/images/snake_0.png" >}}

{{% box type="exercise" title="Mission 1 : As-tu tout compris ?" %}}
Tout ce que tu as à faire dans cette partie est de t'assurer que tu as bien tout compris sur ce que l'on t'a expliqué précédemment. N'oublie pas de lire le code fourni aussi, il n'y a pas grand chose mais assure toi de bien comprendre ce que chaque parti fait et fera.

Si tu n'es pas sûre, n'hésite pas à demander à un organisateur.
{{% /box %}}

### Direction

Passons donc aux déplacements du serpent. Pour cela, il faut savoir dans quelle direction il va. C'est à ça que sert la variable `direction` que l'on initialise par défaut à `HAUT` dans le code donné. Au début de la partie, le serpent ira donc vers le haut.

{{% box type="info" title="Rappel" %}}

Pour rappel, nous souhaitons diriger le serpent avec les boutons A et B du `micro:bit` de la façon suivante :



- si l'on appuie sur **A**, le serpent tourne dans le sens anti-horaire
- si l'on appuie sur **B**, il tourne dans le sens horaire
- sinon, le serpent ne change pas de direction
{{% /box %}}

{{% box type="exercise" title="Mission 2 : Haut, droit, bas, gauche... Quel sera ton choix ?" %}}

Implémente la fonction `nouvelle_direction()` qui :
1. prend en paramètre la direction actuelle du serpent
2. vérifie si les boutons ont été pressés 
3. renvoie la nouvelle direction du serpent

Pour cela, tu peux t'aider des variables définies au début du ficher :

```python
# Directions
HAUT = 0
DROITE = 1
BAS = 2
GAUCHE = 3
```

Tu peux utiliser des conditions ou t'aider de modulos pour connaître la prochaine direction !
Si tu te demandes ce qu'est un modulo, c'est simplement le reste d'une division. 

Prenons un exemple, lorsqu'on divise 13 par 5 on obtient 2 au quotient et il nous reste 3. Ainsi le modulo de 13 par 5 est 3. Si la notion n'est pas encore claire pour toi tu peux essayer de dessiner un schéma de l'exemple ci dessus ou appeler un organisateur. 

Dans notre cas, nous allons utiliser les modulos afin de ne pas sortir des coordonnées utiliser pour allumer les LEDs sur la carte micro:bit.
{{% /box %}}

### Déplacement
Après avoir trouvé la direction du serpent, il faut le déplacer. Imaginons que dans l'exemple précédent, le serpent aille vers la gauche. Après s'être déplacé, l'écran ressemblera à l'image suivante.

{{< figure src="resources/images/snake_0.png" caption="Avant déplacement" >}}
{{< figure src="resources/images/snake_1.png" caption="Après déplacement" >}}

Comme tu peux le voir sur l'image, la tête du serpent s'est déplacée d'une case vers la gauche, et le bout de la queue du serpent a disparu !

{{% box type="exercise" title="Mission 3 : Une nouvelle position ?" %}}

Implémente la fonction `nouvelle_position_tete()` qui :
1. prend en paramètres le serpent et sa direction actuelle
2. renvoie les coordonnées de sa nouvelle tête

_Attention :_ Si le serpent arrive contre le bord il passe de l'autre côté de l'écran !
{{% /box %}}

### Le coeur du code

Maintenant que les fonctions `nouvelle_direction()` et `nouvelle_position_tete()` fonctionnent, tu peux les appeler dans la boucle principale du jeu. La première étape est de mettre à jour la direction du serpent. Après ça, tu vas devoir trouver la nouvelle tête du serpent pour l'insérer au début de ta liste.

Pour finir, il faut supprimer le dernier élément de la liste à condition que la longueur de la liste, qui représente le serpent, soit plus grande que `longueur_serpent`.

Pour insérer la nouvelle tête dans la liste du serpent en première place, tu peux utiliser la fonction `insert()` :

```codepython
liste = [1, 2, 3]

# Insert '8' à la position '0' dans la liste 'liste'
liste.insert(0, 8)
print(liste)
```

Tu peux utiliser la méthode suivante pour retirer le dernier élément d'une liste :

```codepython
liste = [1, 2, 3]

# Enlève le dernière élément d'une liste
liste.pop()
print(liste)
```

{{% box type="exercise" title="Mission 4 : Mise en commun" %}}
Maintenant que tu as tous les outils en main, mets à jour la boucle principale pour que ton serpent puisse bouger librement.
{{% /box %}}

À cette étape, tu devrais être capable de faire bouger ton serpent sur le `micro:bit` en appuyant sur les boutons ! Mais il n'y a pas encore de challenge car le serpent ne grandit pas encore.

{{% box type="warning" title="Un p'tit bilan ?" %}}

Avant de passer à la prochaine partie, assure toi bien que les précédentes étapes sont bien implémentées. Ton serpent doit :

- Avancer tout seul, d'une case toute les demi-secondes (`sleep(500)`)
- S'il touche un mur, se retrouver de l'autre côté de l'écran
- Tourner dans le bon sens lorsqu'on appuie sur le bouton A ou le bouton B

N'hésite pas à interpeler un organisateur si tu veux t'assurer que ton jeu marche bien ou si tu as un quelconque problème.

{{% /box %}}

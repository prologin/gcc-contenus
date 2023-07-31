# .-.. (Ça veut dire L en morse)

Pour pouvoir aider Joseph à sortir de la grotte, tu peux télécharger le code à
compléter en cliquant sur le bouton en haut de la page. Une fois dézippé, c'est dans le fichier
`micro_morse.py` que tu vas pouvoir écrire ton code. Pense à mettre tous les fichiers que tu as dézippé au même endroit.

{{% box type="warning" %}}

Le mot clé `pass` indique simplement que la fonction ne fait rien, pense à le
retirer avant d'écrire ton propre code.

{{% /box %}}

{{% box type="exercise" title="Mission 4 : Traduire du morse" %}}

Complète la fonction `morse_vers_lettre(code, arbre)` qui prend en paramètre
un code en morse et retourne une lettre de l'alphabet. On considèrera que le code
morse donnée est toujours valide.

<br/>

Pour rappel, le point `.` correspond au chemin vers le fils gauche et que le
trait `-` amène vers le fils droit. L'arbre ci-dessous représente l'arbre `MORSE`
qui te sera utile pour aider Joseph.

{{<figure src="resources/images/bintree_morse_code.png" >}}


<details>
<summary>Besoin d'aide ? Clique ici !</summary>

1. Pour récupérer la **clé** d'un **noeud**, tu peux utiliser `noeud.cle`.
2. Pour récupérer le **fils gauche** d'un **noeud**, tu peux utiliser
   `noeud.gauche`.
3. Pour récupérer le **fils droit** d'un **noeud**, tu peux utiliser
   `noeud.droit`.
4. Pour accéder au premier caractère d'une chaîne de caractères, tu peux
   utiliser l'indice 0 : `chaine[0]`. Pour accéder au reste de la chaîne, tu
   peux faire `chaine[1:]`.
5. Pour t'aider à l'écriture de la fonction, tu peux essayer de répondre aux
   questions suivantes :
    - Quand est-ce que je dois m'arrêter ? Quel est mon cas d'arrêt ?
    - Où est-ce que je dois aller si je tombe sur un point ? Et sur un trait ?
6. Pour parcourir l'arbre, il suffit de parcourir chacun de ses `noeud` en
   allant à droite ou à gauche suivant le caractère rencontré. C'est comme si
   l'encodage était notre itinéraire, et que nous avancions au fur et à mesure.

   Voici un exemple de fonction pour parcourir un arbre : 

```py
def parcours(arbre):       # Ici `arbre` est un arbre de type 'Noeud'

    print(arbre.cle)       # Ici on affiche la clé de la racine `arbre`

    parcours(arbre.gauche) # Ici on rappelle la fonction avec comme nouvel arbre :
                           # celui dont la racine est le fils gauche de `arbre`

    parcours(arbre.droit)  # De même ici avec le fils droit de `arbre`
```
</details>

{{% /box %}}

Tu peux tester ta fonction en lui donnant une chaîne correspondant à une lettre,
et en vérifiant qu'elle renvoie la bonne lettre. 

Par exemple :

```py
morse_vers_lettre(".-", MORSE)   # Renvoie 'A'
morse_vers_lettre("-.-.", MORSE) # Renvoie 'C'
```
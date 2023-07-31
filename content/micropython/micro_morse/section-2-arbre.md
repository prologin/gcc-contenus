# Utilisons les arbres !

En informatique, une structure est particulièrement adaptée pour utiliser cette
notion de **préfixe commun** : les arbres.
Les arbres permettent en fait d'organiser des données et de les lier facilement.
morse, les **lettres** ont un préfixe commun.

{{% box type="info" title="Un peu de vocabulaire" %}}

{{<figure src="resources/images/tree_example.svg" width=700 >}}

Comme tu peux le voir, un arbre est composé de plusieurs **noeuds**. Ce sont les
ronds noirs sur l'image. Le premier noeud, celui tout en haut, est appelé
**racine** de l'arbre, car comme dans un vrai arbre, c'est ici que tout commence.

<br/>

Chaque **noeud** possède une _clé_, qui correspond à ce qui est marqué à
l'intérieur du rond sur l'image. Les **noeuds** sont reliés entre eux par des
_branches_ (ici en rouge et en bleu).

<br/>

Pour s'y retrouver plus facilement, on appelle **fils gauche** le noeud qui est
_en bas à gauche_ d'un autre noeud, et **fils droit** celui qui est _en bas à
droite_ d'un autre noeud. On accède au **fils gauche** en suivant le lien
rouge, et au **fils droit** en suivant le lien bleu. 

{{% /box %}}

## Parcourons les arbres !

Pour utiliser un arbre, nous disons que nous le **parcourons**. Un parcours
d'arbre, c'est un peu comme suivre un itinéraire en voiture :

- La **racine** est notre point de départ
- Chaque **noeud** correspond à une intersection
- Chaque **branche** correspond à une route possible
- Chaque **clé** correspond à un panneau indicateur. 

Nous devons donc, à chaque intersection, suivre la bonne route en fonction de
l'itinéraire qui nous est donné et des panneaux que nous allons rencontrer. 

{{% box type="warning" %}}

Pour nous faciliter la tâche par la suite, nous partons du principe qu'un
point (`'.'`) signifie que l'on doit aller à **gauche**, et qu'un tiret (`'-'`)
que l'on doit aller à **droite**.

{{% /box %}}

Prenons l'exemple de l'arbre que nous allons utiliser :

{{<figure src="resources/images/bintree_morse_code.png" >}}

Comme tu peux le voir, la lettre **A** se trouve _avant_ la lettre **J**. Cela
nous permet donc de se diriger _dans la bonne direction_ peu importe le début de
l'encodage. 

{{% box type="exercise" title="Mission 2 : À quoi correspond le code ?" %}}

Pour essayer de mieux comprendre, essaye de deviner à quelle lettre correspond
l'encodage `-..-`.

<br/>

<details>
<summary>Clique ici pour avoir la solution !</summary>

`-..-` est la traduction de la lettre `X` en morse.

Faisons ensemble toutes les étapes pour mieux comprendre.

Nous utiliserons ce schéma afin que les explications soient plus claires :

{{<figure src="resources/images/bintree_morse_code_x_example.png" >}}

1. Le mot `-..-` commence par un trait (`-`). Nous allons donc d'abord aller
   vers la droite en empruntant le <font color="#4287f5">chemin bleu</font>.
2. Nous avons ensuite un point (`.`), nous prenons donc ensuite le chemin allant
   vers la gauche (<font color="#f54242">en rouge</font>)
3. Nous rencontrons un autre point (`.`), nous prenons donc le
   <font color="#f54242">chemin rouge</font>.
4. Enfin, nous avons un trait (`-`), nous prenons le
   <font color="#4287f5">chemin bleu</font>, vers la droite.
5. Nous avons traité tous les caractères, nous sommes arrivés à destination !

Si tu n'as pas compris quelque chose, n'hésite pas à demander de l'aide aux
organisateurs.

</details>

{{% /box %}}

{{% box type="info" title="Représentation des arbres en Python" %}}

Les **arbres**, en informatique, ne sont en fait que des **noeuds** qui sont
reliés entre eux. C'est pour ça que pour les représenter, nous avons choisi de
stocker ces **noeuds** dans un objet Python qui contient trois variables :

- `noeud.cle` : la **clé** du noeud
- `noeud.gauche` : le **fils gauche** du noeud
- `noeud.droit` : le **fils droit** du noeud

Si tu souhaites en savoir plus sur cet objet, n'hésite pas à demander à un
organisateur !

{{% /box %}}
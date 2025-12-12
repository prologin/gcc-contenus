## Les attributs

Les balises ont encore quelques secrets à nous livrer. On peut en effet leur ajouter des attributs.

Un attribut `HTML` est un composant de la balise utilisé pour ajuster le comportement ou l'affichage de l'élément de la balise. Par exemple, les attributs peuvent être utilisés pour modifier la couleur, la taille ou la fonctionnalité des éléments.

Pour ajouter un attribut, il suffit de l'inclure dans une balise `HTML` ouvrante :

```codehtml
<p attribut="valeur"> Ceci est un paragraphe avec un attribut </p>
```

Un attribut comprend le nom de celui-ci suivi du signe égal ``=`` et d'une valeur placée entre guillemets ``""``.

### Liens

L'une des premières balises mettant à profit les attributs concerne une des fonctionnalités essentielles du web : les liens.

La balise de lien `<a>` utilise l'attribut `href` pour proposer un élément cliquable qui déplacera le visiteur vers un autre site, une autre page, ou simplement un endroit différent de la page.

```codehtml
<p> Un lien vers <a href="https://prologin.org"> Prologin </a></p>
```

De plus, les liens permettent également de rejoindre un endroit spécifique de la page avec l'aide de points d'ancrage. Pour définir un point d'ancrage, il suffit d'ajouter un attribut `id`  à une balise ouvrante et spécifier une valeur. Il sera alors possible de créer un lien vers ce point d'ancrage en ajoutant à l'attribut `href` d'une balise `<a>` la valeur choisie, précédée d'un `#`. Attention tous les `id` doivent être uniques.

```codehtml
<a href="#article2"> Direction le deuxième article </a>
<h2 id="article2"> Article 2 </h2>
```

{{% box type="exercise" %}}

Mets à jour ton sommaire pour qu'il soit possible de cliquer sur les éléments et atteindre les articles.

1. Commence par ajouter des `id` à tes titres d'article
2. Transforme ton sommaire en une liste de liens, afin que chaque élément de la liste dirige vers l'article correspondant

{{% /box %}}

### Images

Du texte c'est bien, des images c'est encore mieux !

Pour afficher une image, il faut deux choses : la balise image `<img/>` et l'attribut `src`. L'attribut `src` prend comme valeur l'URL vers une image.

```codehtml
<img src="https://prologin.org/static/img/logo_cube.png" />
```

{{% box type="info" title="Qu'est-ce-que c'est qu'une URL ?" %}}

Une URL, c'est l'adresse d'un site, ce qui te permet de le retrouver. C'est comme l'adresse d'une maison, qui te permet de trouver ton chemin jusqu'à elle. 

Cette URL permet ensuite au navigateur de trouver le chemin menant à une page internet.
Par exemple, les URLs des sites tels que `Google` ou `Youtube` sont : `https://www.google.com` et `https://www.youtube.com`.
Donc si tu mets ces URLs dans la barre de recherche de ton navigateur internet, ils mèneront vers leurs sites respectifs.

D'ailleurs, ce système d'URL est unique à chaque page web, tout comme l'adresse d'une maison est elle aussi unique à chaque maison. 
Ces URLs peuvent aussi désigner l'adresse d'images, comme avec [https://prologin.org/static/img/logo_cube.png](https://prologin.org/static/img/logo_cube.png). 

{{% /box %}}

Tu remarqueras que la balise `<img/>` est à la fois ouvrante et fermante. Elle ne fonctionne pas par pair, mais se suffit à elle même, en ajoutant un `/` avant le chevron fermant `>`.

{{% box type="exercise" %}}

C'est maintenant l'heure d'utiliser un outil formidable : `Google Image`. 

Pour ce faire :
1. Recherche sur Google une image pour chacun de tes articles
2. Pour chaque image, copie son lien 
3. Pour chaque article, ajoute une image entre le titre et le texte

{{% /box %}}

Il existe des arguments pour mettre l'image à la taille que tu veux !
Tu peux lui donner une hauteur (`height`) et une largeur (`width`).
Ces attributs prennent comme paramètre un nombre, la taille que tu veux en pixel.

Par exemple :

```codehtml
<img src="https://prologin.org/static/img/logo_cube.png" width="50">
```

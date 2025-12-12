# Balises

La particularité du `HTML` par rapport à du texte simple, c'est qu'il permet de structurer la page (titres, paragraphes, liens, images...) à l'aide de balises.

{{% box type="info" title="Mais qu'est-ce qu'une balise ?" %}}

Une balise est composée d'un texte entouré de chevrons (les symboles `<` et `>`). Elles viennent généralement par paires : une balise ouvrante (`<nom de la balise>`) et une balise fermante (`</nom de la balise>`), permettant d'encadrer du texte pour en définir la nature.

```codehtml
Bonjour, je m'appelle <strong> Joseph Marchand </strong> et j'aime le web !
```

Seul le texte `Joseph Marchand`, contenu entre les balises ouvrantes `<strong>` et fermantes `</strong>` est en gras, le reste ne l'est pas.

{{% /box %}}

{{% box type="warning" title="Attention à l'ordre des balises !" %}}

Comme les poupées russes, les balises peuvent en contenir d'autres. Toute balise ouverte doit être fermée, donc dans l'ordre inverse d'ouverture.

```codehtml
<strong><em> Hello World! </em></strong> <!-- Correct -->
```

Ici on ouvre `strong`, puis on ouvre `em`, puis on ferme `em`, et enfin on ferme `strong` ; ce qui est correct.

```html
<strong><em> Hello World! </strong></em> <!-- Incorrect -->
```

Ici on ouvre `strong` puis on ouvre `em`, puis on ferme `strong`, et enfin on ferme `em` ; c'est incorrect puisque les balises s'entremêlent.

{{% /box %}}

Les navigateurs connaissent un certain nombre de balises, qui vont leur permettre de comprendre ce que tu veux afficher.

Dans la suite de ce TP, tu vas rencontrer petit à petit différentes balises et comprendre leur rôle. Tu auras l'occasion de les utiliser, à chaque fois dans un fichier fourni. **Tu devras écrire exclusivement entre les balises `<body>` et `</body>`** (nous reviendrons plus tard sur leur utilité et celle des autres balises présentes dans ce fichier).

## Balises, balises everywhere

### Titres

Comme tout bon blog qui se respecte, le tien a besoin de titres ! Le titre principal, et un titre pour chaque article.

Toutefois, tous les titres n'ont pas la même importance. En effet, comme sur une page web classique, il existe généralement en grand format le titre principal du site, puis de plus en plus petit les autres titres.

Pour représenter cette hiérarchie, les navigateurs connaissent 6 niveaux de titres, identifiés par les balises suivantes :

```codehtml
<h1> Le titre le plus important!! </h1>
<h2> Un titre un peu moins important! </h2>
<h3> Un titre encore moins important. </h3>
...
<h6> Un titre vraiment vraiment moins important </h6>
```

### Paragraphes

Des titres, c'est bien, mais un blog c'est aussi et surtout du contenu, du texte !

On a déjà vu tout à l'heure qu'il était possible de mettre du texte partout dans un fichier `HTML`, mais il est aussi important de préciser au navigateur ce qu'il représente.

Pour cela, il existe la balise `<p>`.

```codehtml
<h1> Ceci est un titre </h1>
<p> Ceci est un paragraphe </p>
```

{{% box type="exercise" %}}

Tu peux modifier le fichier `blog.html` pour inclure différents articles en-dessous des titres ajoutés précédemment.

1. Sous le premier titre d'article, écrit un paragraphe avec la balise appropriée.
2. Sous le deuxième titre d'article, écrit deux paragraphes.

{{% /box %}}

### Indentation

Tu as pu le remarquer dans le fichier `blog.html`, toutes les lignes ne sont pas collées à gauche de l'écran, certaines sont décalées vers la droite par des espaces.

On appelle cela l'**indentation**. Indenter permet d'obtenir un code plus propre, plus lisible et donc plus compréhensible. Il sera possible de discerner plus facilement les différents éléments ou parties de code.

Il n'y a pas en HTML de règle absolue concernant l'indentation. Généralement, quand le contenu de balises s'étend sur plus d'une ligne, on indentera ce contenu d'un rang de plus que les balises. Chaque rang d'indentation est construit à l'aide de 4 espaces, ou 1 tabulation.

```codehtml
<html>
    <body>
        <h1> Titre sur une ligne </h1>
        <p> Hello World! </p>
    </body>
</html>
```

Ici, le contenu de la balise `html` est identé d'un rang. Ensuite, le contenu de la balise `body` est indenté d'un rang de plus, donc de deux rangs.


### Mise en valeur du texte

De temps en temps, tu auras envie de mettre en valeur une partie du texte pour le faire ressortir. Une citation par exemple. Tu vas voir 2 manières de le faire.

Tu peux mettre en gras avec la balise `<strong>` et tu peux également mettre en italique avec la balise `<em>`:

```codehtml
<p> Ceci est un <strong> mot important </strong> dans un pragraphe </p>
<p> Ceci est aussi un <em> mot important </em> dans un pragraphe </p>
```

{{% box type="exercise" %}}

Mets en valeur des mots dans tes articles

1. Mets en **gras** un mot dans ton premier article
2. Mets en *italique* un mot du dans ton deuxième article
3. Choisis un mot dans ton blog et mets le en gras et en italique

{{% /box %}}

### Listes

Pour structurer ta page, tu peux également utiliser des listes. Il en existe deux types : les listes à puces (en utilisant la balise `<ul>`) et les listes numérotées (en utilisant la balise `<ol>`).

La première liste permet d'énumérer sans notion d'ordre, la seconde ajoute un numéro devant chaque élément de la liste.

Chaque élément de la liste doit être encadré des balises `<li>` `</li>`.

```codehtml
<h1> Liste de courses </h1>
<ul>
    <li> Pain </li>
    <li> Lait </li>
    <li> Oeufs </li>
</ul>

<h1> Classement </h1>
<ol>
    <li> Dominique </li>
    <li> Sacha </li>
    <li> Frédérique </li>
</ol>
```

{{% box type="exercise" %}}

Profitons des listes pour ajouter un sommaire à ton blog.

1. Crée une liste sous le titre principal
2. Ajoute autant d'éléments à la liste que tu as d'articles

{{% /box %}}

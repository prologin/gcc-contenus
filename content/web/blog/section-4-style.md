# Ajouter du style

Tu as maintenant un blog, mais il manque un peu de couleurs. Le style d'un site web ne se fait pas en `HTML`, mais dans un autre langage : le `CSS`.

Tu vas pouvoir modifier la couleur du fond, modifier la taille du texte, ajouter des bordures, et plein de choses encore.

Le CSS permet d'appliquer un style à un type d'élément (tous les titres, toutes les images, ...), ou à un élément en particulier grâce à son `id`.

{{% box type="info" title="La feuille CSS"%}}

On appelle feuille CSS le fichier qui contient toutes les règles CSS d'une page. Ce fichier est communément nommé `style.css`.

Pour qu'une page `HTML` puisse utiliser une feuille CSS, il faut lui indiquer le nom de cette feuille dans une balise `<link/>`. Dans le fichier 'blog.html' fourni, cette balise est déja ajoutée en haut de la page.

```html
<link rel="stylesheet" href="style.css" />
```

La balise `<link/>` permet de spécifier une relation entre le document actuel et une ressource extérieure. Par exemple, ici, on annonce au document `HTML` qu'une feuille CSS est disponible dans le fichier `style.css`.

{{% /box %}}

{{% box type="exercise" %}}

Crée une feuille CSS qui se nomme `style.css`

{{% /box %}}

Les règles CSS, qui permettent de déterminer le style à appliquer, sont composées de 2 éléments : le sélecteur, et les propriétés.

Une règle se présentera donc de la façon suivante :

```css
selecteur {
    propriete;
    ...
    propriete;
}
```

## Le sélecteur

Le selecteur indique l'élément qui est ciblé par cette règle. Il s'écrit simplement avec le nom de la balise.

Par exemple, pour les balises paragraphes, `<p>` :

```css
p {
    /* Ici je modifie le style de toutes les balises paragraphes de mon site */
}
```

Ou bien pour les balises de lien `<a>` :
```css
a {
    /* Ici je modifie le style de toutes les balises de lien de mon site */
}
```

Tu peux également cibler une balise précise grâce à son `id`. Il suffit de mettre '#' puis son id.
N'hésite pas à retourner à la partie `id` ou à appeler un organisateur si tu as un problème.

```css
#mon_id {
    /* Ici je modifie le style de la balise ayant l'id: 'mon_id' */
}
```

## Les propriétés

Les propritées sont composées comme suit :

```css
nom: valeur;
```

Il est possible de mettre autant de propriétés qu'on veut dans chaque règle. Tu verras par la suite quels sont les différents `nom` possibles.

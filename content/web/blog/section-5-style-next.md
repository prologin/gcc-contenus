## Le noir et blanc, c'est fini !

Pourquoi se contenter de deux couleurs quand il en existe des millions !
Sur ton blog tu vas pouvoir changer la couleur des arrière-plans (par exemple le fond de la page), ou même des textes.

Pour changer la couleur des fonds, tu vas utiliser la propriété `background-color`. Cette propriété prend pour valeur le nom d'une couleur en anglais (par exemple, red, blue, green). Tu peux retrouver la liste complète [ici](https://developer.mozilla.org/en-US/docs/Web/CSS/color_value/color_keywords#list_of_all_color_keywords).

Pour que tous tes paragraphes aient un fond rouge par exemple :
```css
p {
    background-color: red;
}
```

{{% box type="exercise" %}}

1. Change la couleur du fond de toute la page avec le selecteur `body`
2. Change la couleur du fond du titre principal

{{% /box %}}

Maintenant que tu as changé la couleur des fonds, les textes ne sont peut-être plus très lisibles. Pour changer la couleur des textes, tu vas utiliser la propriété `color`. Cette propriété prend les mêmes valeurs que `background-color`.

Pour changer la couleur du titre principal en bleu :
```css
h1 {
    color: blue;
}
```

{{% box type="exercise" %}}

1. Change la couleur des titres de tes articles
2. Change la couleur des mots en gras

{{% /box %}}

## Des bordures

En `HTML`, chaque balise représente une boîte contenant des éléments comme du texte, une image, etc.


On peut ajouter une bordure à la boîte et la personnaliser en utilisant les trois propriétés suivantes : `border-style`, `border-width` et `border-color`.

La propriété `border-style` permet de choisir son style : un trait, un double trait, etc... La liste complète des valeurs possibles est disponible [ici](https://developer.mozilla.org/en-US/docs/Web/CSS/border-style#values).

La propriété `border-width` permet de contrôler son épaisseur. Elle peut prendre trois valeurs différentes : `thin`, `medium`, `thick`, respectivement pour une épaisseur fine, moyenne, ou épaisse.

Enfin la propriété `border-color` permet de choisir sa couleur. Elle utilise les mêmes valeurs de couleurs vues précédemment. Tu peux retrouver la liste des valeurs possibles [ici](https://developer.mozilla.org/en-US/docs/Web/CSS/color_value/color_keywords#list_of_all_color_keywords).


Pour ajouter une bordure aux titres des articles (définis en `h2`) :

```css
h2 {
    border-style: solid;
    border-width: medium;
    border-color: green;
}
```

{{% box type="exercise" %}}

Ajoute une bordure à tes images

{{% /box %}}

{{<figure src="resources/images/border.png" width=250 >}}

## Padding

Pour éviter que les éléments soient trop proches les uns des autres, on peut ajouter de l'espace autour d'un élément. On peut ajouter un espace différent sur chacun des côtés de l'élément en utilisant la propriété correspondante :

- En haut : `padding-top`
- A droite : `padding-right`
- En bas : `padding-bottom`
- A gauche : `padding-left`

Pour ajouter un espace autour des images :

```css
img {
  padding-top: 50px;
  padding-right: 30px;
  padding-bottom: 50px;
  padding-left: 80px;
}
```

{{% box type="exercise" %}}

Ajoute un padding à gauche de ton sommaire

{{% /box %}}

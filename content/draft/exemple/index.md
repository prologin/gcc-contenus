---
title: "TP Exemple"
weight: 1
authors: ["GCC"]
subtitle: Voici un TP présentant toutes les actions possibles pour créer un TP. 
code_stub_url: FIXME (or not)
---

Avant tout, pense à remplir les différentes `meta-data` qui sont utiles pour 
que ton TP soit correctement répertorié et affiché sur le site. 

# Voilà le premier titre principal du TP

## Et un sous-titre...

### Et un sous-sous-titre...

Ici nous avons un simple paragraphe avec vraiment beaucoup de texte, encore et
encore du texte. Du texte à foison afin d'expliquer complètement aux filles les
différentes notions abordées... 

Nous avons ici du texte en **gras**, _italique_, ~~barré~~, `inline codeblock`,
**_gras et italique_**, [un lien vers google](https://www.google.fr), etc...
Toutes les balises markdown sont prises en compte par Hugo (si ce n'est pas le
cas, vous pouvez ouvrir une issue sur [gitlab](https://www.gitlab.com/prologin/gcc/contenus)). 

```python
def function():
    """
    Nous avons ici un code block python que les participantes peuvent copier
    directement grâce au bouton prévu à cet effet.

    De très nombreux langages sont pris en compte dans cette coloration
    syntaxique.
    """
    print("Un TP d'exemple qui sert aussi de cheat-sheet")
```

La liste complète des langages ayant une coloration syntaxique est disponible 
[ici](https://gohugo.io/content-management/syntax-highlighting/#list-of-chroma-highlighting-languages). 

Il y a aussi un autre type de balise code. Ce sont des balises qui permettent
d'exécuter directement du code dans le navigateur. Elles sont disponibles en
python et en HTML. 

```codepython
print("Une balise pour exécuter du code en python")
```

```codehtml
<p class="test">Un paragraphe de <em>test</em></p>
<style>
.test {
    color: red;
}
</style>
```

[SECTION-BREAK]

# Une nouvelle section !

La balise ci-dessus permet de diviser les TPs en plusieurs sous-sections qui
marquent une séparation plus nette que de simples changements de titres. 
Cette balise peut, par exemple, séparer une partie assez théorique d'une partie au
contraire très pratique. 

{{% info %}}
Il est aussi possible de mettre en valeur certaines parties d'un
TP, pour que celui-ci soit plus lisible et agréable à lire. 
Ils sont appelés des `shortcodes`. 
{{% /info %}}

Voici la fin du shortcode _info_.

{{% cours %}}
Voici un shortcode _cours_.
Nous pouvons ajouter toutes sortes de balises Markdown dans des shortcodes.
# Comme des titres
## Des sous-titres, etc...
{{% /cours %}}

{{% exemple %}}
Voici un shortcode _exemple_.
{{% /exemple %}}

{{% exercice %}}
Voici un shortcode _exercice_.
{{% /exercice %}}

## Un block spoiler

La phrase suivante contient un spoiler. Il cache une zone de texte, qui est
révélée quand on appuie dessus.
Qu'est-ce qui est jaune et qui attend ? {{< spoiler >}}Un citron
dans un ascenseur{{</ spoiler >}}.
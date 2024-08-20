# Mettre en forme les chaînes de caractères

## Insérer des expressions dans une chaîne

En *Python*, il existe un moyen de **formater** une chaîne de caractères. Cela
permet d'insérer des expressions ou des variables à l'intérieur d'une chaîne de
caractères.

Pour créer un **f-string**, il suffit de mettre le caractère `f` avant le début
d'une chaîne de caractères, c'est-à-dire avant le premier guillemet (`"`).

```codepython
# Crée un f-string `mon_fstring`
mon_fstring = f"Hello World!"

# Affiche `mon_fstring`
print(mon_fstring)
```

Il est alors possible de donner une expression à l'intérieur d'accolades (`{}`)
dans un *f-string*.

```codepython
# Crée une variable `nombre`
nombre = 42

# Crée un f-string `mon_fstring`
mon_fstring = f"{nombre} est un nombre important en informatique !"

# Affiche `mon_fstring`
print(mon_fstring)
```

## Options de formattage

Une autre fonctionnalité des *f-string* est de pouvoir **donner des options** au
formattage des nombres donnés dans un *f-string*. On utilise alors la syntaxe
`{variable : options}` avec `variable` correspondant au nombre souhaité et
`options` des différentes options possibles.

{{< codestep steps=3 lang="py" run="true" >}}

{{< codestep-block desc="Crée une variable `pi`" >}}
pi = 3.14159265359
 
{{< /codestep-block >}}

{{< codestep-block desc="Affiche la variable `pi` avec 2 décimales" >}}
print(f"{pi : .2f}")
{{< /codestep-block >}}

{{< codestep-block desc="Affiche la variable `pi` avec 4 décimales" >}}
print(f"{pi : .4f}")
{{< /codestep-block >}}

{{< /codestep >}}

Les *f-string* s'avèrent très utiles lorsqu'on essaye d'afficher un tableau de
nombres dans une console *Python*.

```codepython
print(f'Nombre\t\tCarré\t\tCube')
for x in range(1, 11):
    print(f'{x : <2d}\t\t{x*x : ^4d}\t\t{x*x*x : >4d}')
```

{{% box type="warning" title="Beaucoup de détails..." %}}

Nous allons pas rentrer dans le détail sur les différentes options possibles,
mais si tu souhaites en savoir plus, n'hésite pas à contacter un organisateur !

<!-- Plus d'informations sur https://he-arc.github.io/livre-python/fstrings/index.html -->

{{% /box %}}

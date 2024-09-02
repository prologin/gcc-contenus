# Les fonctions

Les fonctions représentent une fonctionnalité clé de la programmation. Elles
permettent d'**affecter un bout de code** à un nom. C'est comme si on
représentait les fonctions comme étant des variables avec comme valeur tout un
bout de code ! Elle est donc réutilisable en fonction de certains paramètres.

Pour déclarer une fonction, il faut **5 éléments** :

- le mot-clé `def` ;
- le nom de la fonction ;
- des parenthèses ;
- deux points `:` ;
- un bout de code indenté.

{{< codestep steps=3 lang="py" run="true" >}}

{{< codestep-block desc="Définit la fonction qui se nomme `salutations`" >}}
def salutations():
{{< /codestep-block >}}

{{< codestep-block desc="Instructions qui représentent le corps de la fonction" >}}
    print("Bonjour chère aventurière !")
    print("Je suis Julie...")
    print("et voici ma fonction !")
{{< /codestep-block >}}

{{< codestep-block desc="Appelle la fonction `salutations`" >}}
 
salutations()
{{< /codestep-block >}}

{{< /codestep >}}

Une fonction peut aussi être utilisée pour **créer un résultat** à partir de
certains **paramètres**. Jouons à un jeu ! Voici une fonction qui permettra de 
lire dans les pensées (enfin presque).

```codepython
# Définit la fonction `tour_de_magie` qui
# prend un nombre `n` en paramètre
def tour_de_magie(n):
    # Crée la variable `resultat` en fonction
    # du paramètre `n`
    resultat = 2 * n
    resultat = resultat + 10
    resultat = resultat // 2
    resultat = resultat - n

    # Renvoie la valeur de `resultat`
    return resultat

# Appelle la fonction avec la valeur 42
# et garde en mémoire le résultat de la fonction
# dans la variable `valeur`
valeur = tour_de_magie(42)
print(valeur)
```

Essaye de changer le nombre dans l'appel à la fonction `tour_de_magie`, tu
verras ainsi la magie s'opérer !

{{% box type="info" title="Les paramètres d'une fonction" %}}

Comme tu as pu le remarquer, les paramètres de la fonction fonctionnent comme
des **variables dans la fonction**. Il peut en avoir 0, 1 ou plus ! On utilise
la fonction en l'**appelant avec des paramètres** :

```python {nocopy=true}
ma_fonction(parametre1, parametre2, ...)
```

{{% /box %}}

{{% box type="info" title="Le mot-clé `return`" %}}

On peut également demander à la fonction de **renvoyer un résultat** en utilisant le mot-clé `return`. Il est alors possible
de récupérer la valeur du résultat dans une variable.

```python {nocopy=true}
ma_variable = ma_fonction(parametre1, parametre2, ...)
```

{{% /box %}}

{{% box type="exercise" title="Mission 7 : Trésor caché !" %}}

Après ton long périple, tu te retrouves sur une grosse croix rouge sur le sol !
Curieuse, tu voudrais creuser pour retrouver le trésor enfoui.

Tu remarques sur le parchemin, qu'il est possible d'appeler des mineurs afin
qu'ils t'aident à creuser dans le sol et révéler le secret !

> Afin d'accéder à mon précieux, utilise une fonction pour appeler les mineurs !
> Pour cela, crée une fonction qui se nomme `creuser` et qui prend en paramètre 
> une variable qui s'appelle `nom`. Dans cette fonction, affiche les phrases
> suivantes :

> Brothers of the mine rejoice!
> </br>
> Swing, swing, swing with me
> </br>
> Raise your pick and raise your voice!
> </br>
> Sing, sing, sing with me
> </br>
> I am a dwarf and I'm digging a hole
> </br>
> Diggy diggy hole, diggy diggy hole

> Après avoir affiché ces paroles, affiche la phrase suivante en utilisant la
> variable `nom` à la place de <font color=#F54110>**nom**</font> !
> 
> </br>
> "Come <font color=#F54110>nom</font> and sing with me!"

Appelle ta fonction avec ton prénom puis avec *"Julie"* et enfin avec *"Joseph"*
en paramètre et le secret se dévoilera !

<details>
<summary>Clique pour voir un rappel sur la fonction print</summary>

En *Python* pour intégrer une variable dans le texte affiché par `print` on peut utliser des virgules (`,`).

```codepython
nom = "Marchand"

# Affiche la variable avec `print`
print("Salut", nom , "! Comment vas-tu ?")
```

</details>

{{% /box %}}

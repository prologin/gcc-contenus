## Les fonctions

Rentrons dans une partie un peu complexe mais qui va nous servir tout au long du sujet.

Découvrons ensemble les **fonctions** ! Sache que si tu as la moindre question, tu peux lever la main et demander de l'aide à un organisateur !


{{% box type="info" title="Une fonction, qu'est-ce-que c'est ?" %}}

Une fonction est un bout de programme qui effectue une action, et que l'on va pouvoir utiliser plusieurs fois.   

```py
def hello_world():
    # Indentation
    # Code
```

Comme tu vois ci-dessus, il faut 5 éléments pour créer une fonction :

- le mot-clé `def`
- le nom de la fonction (ici `hello_world`)
- des parenthèses `()`
- deux points `:`
- une indentation à la suite


Prenons un exemple:
{{< codestep steps=4 lang="py" run=true >}}

{{< codestep-block desc="Créons une nouvelle fonction nommée `fonction_geniale`" >}}
def fonction_geniale():
{{< /codestep-block >}}

{{< codestep-block desc="On écrit tout ce que l'on veut que notre fonction fasse en dessous **et** indenté." >}}
    print("Bonjour !")
    print("Les fonctions c'est super utile !")
{{< /codestep-block >}}

{{< codestep-block desc="Il ne nous reste plus qu'à appeler notre fonction pour que nos 2 `print` soient exécutés." >}}

fonction_geniale()
{{< /codestep-block >}}

{{< codestep-block desc="Mais attend, tu peux le faire autant de fois que tu le veux maintenant, tu n'as plus qu'à appeler la fonction encore et encore" >}}

print("\nEt de deux")
fonction_geniale()
print("\nEt de trois")
fonction_geniale()
print("\nEt de quatre")
fonction_geniale()
{{< /codestep-block >}}

{{< /codestep >}}

</br>

Jusque-là, c'est bien, mais on peut faire mieux.

Les fonctions ont la spécificité de pouvoir **prendre des paramètres** et **renvoyer une ou plusieurs valeurs**.

</br>

**Les paramètres :** À l'intérieur des parenthèses qui suivent le nom de la fonction, on peut mettre un ou plusieurs paramètres qui seront utilisés comme des variables dans la fonction. Le résultat de la fonction peut dépendre ainsi des paramètres donnés.

**Le `return` :** Ce mot-clé se trouve à la fin d'une fonction et permet de renvoyer une ou plusieurs valeurs.

</br>

Analysons ensemble le code ci-dessus.

{{< codestep steps=6 lang="py" run=true >}}

{{< codestep-block desc="On définit notre fonction qui prend un paramètre `nombre`." >}}
def puissance_2(nombre):
{{< /codestep-block >}}

{{< codestep-block desc="On calcule le carré de `nombre`." >}}
    carre = nombre * nombre
{{< /codestep-block >}}

{{< codestep-block desc="On renvoie la valeur de `carre`." >}}
    return carre
{{< /codestep-block >}}


{{< codestep-block desc="`resultat` prend la valeur retournée par l'appel de `puissance_2` avec `5` comme paramètre." >}}

resultat = puissance_2(5)
{{< /codestep-block >}}

{{< codestep-block desc="On affiche la valeur renvoyée par la fonction." >}}
print(resultat)
{{< /codestep-block >}}

{{< codestep-block desc="On affiche directement ce que renvoie `puissance_2` de `4`." >}}

print(puissance_2(4))
{{< /codestep-block >}}

{{< /codestep >}}

Et voilà, tu sais tout ce qu'il y a à savoir sur les fonctions pour faire ton Flappy Bird!

{{% /box %}}

{{% box type="warning" title="Variables VS paramètres" %}}

Les variables créées dans une fonction sont **temporaires** et ne peuvent être utilisées que dans cette même fonction. Dès que le code sort de la fonction, les variables **ne peuvent plus être utilisées**, d'où l'utilité de renvoyer une valeur.

</br>

De même, les variables données en paramètre ne sont pas liées aux variables données dans l'appel de la fonction. Elles ne sont que des **"copies"**.

</br>

Cet aspect de valeur temporaire est très important à comprendre, donc n'hésite pas à appeler un organisateur si tu n'as pas tout compris.

```codepython
def exemple(x):
    tmp = 5 # Crée une variable à l'intérieur de la fonction
    x = x + 4 # Rajoute 4 au paramètre
    print("x =", x)
    print("tmp =", tmp)

valeur = 6
exemple(valeur)
print("valeur =", valeur)

# Enlève le `#` devant le `print` ci-dessous
# print(tmp)
```

{{% /box %}}

*Encore une fois, si tu n'as pas tout compris ou que tu as encore des questions sur les fonctions (ou autre), n'hésite pas à appeler un organisateur pour revoir ce dont tu as besoin.*

Si, au contraire, tu veux comprendre par toi-même, tu peux cliquer sur le menu déroulant ci-dessous pour plus d'exemples.

<details>
<summary> Quelques exemples supplémentaires </summary>

Voici un exemple de fonction qui prend un paramètre, mais qui ne renvoie rien.
{{< codestep steps=4 lang="py" run='true' >}}

{{< codestep-block desc="On définit notre fonction, nommée `comparer` qui prend un paramètre `x`" >}}
def comparer(x):
{{< /codestep-block >}}

{{< codestep-block desc="On vérifie que `x` est inférieur à 100." >}}
    if x < 100:
        print(x + " est inférieur à 100")
{{< /codestep-block >}}

{{< codestep-block desc="De même pour `x` supérieur à 100" >}}
    elif x > 100:
        print(x + " est supérieur à 100")
{{< /codestep-block >}}

{{< codestep-block desc="Et pour finir, si `x` est égal à 100" >}}
    else:
        print(x + " est égal à 100")
{{< /codestep-block >}}

{{< /codestep >}}

Pour l'instant on a juste défini la fonction. Ton ordinateur connaît désormais la fonction `comparer` que tu viens de créer. Elle n'a juste pas encore été appelée, c'est pour cela que rien ne s'affiche.

Découvrons comment appeler la fonction avec différents paramètres !

```codepython
def comparer(x):
    if x < 100:
        print(str(x) + " est inférieur à 100")
    elif x > 100:
        print(str(x) + " est supérieur à 100")
    else:
        print(str(x) + " est égal à 100")

# On appelle notre fonction avec `5` en paramètre
comparer(5)

# On crée une variable `valeur`.
valeur = 121
# On appelle notre fonction pour savoir si `valeur` est supérieur,
# inférieur ou égal à 100.
comparer(valeur)
```

</br>

Regardons une autre fonction.
La fonction ci-dessous prend 2 paramètres et renvoie le résultat de x puissance y.
{{< codestep steps=5 lang="py" run='true' >}}

{{< codestep-block desc="On définit notre fonction `puissance` qui prend deux paramètres `x` et `y`" >}}
def puissance(x, y):
{{< /codestep-block >}}

{{< codestep-block desc="On vérifie les cas particuliers : on renvoie `1` si `y == 0` et `0` si `x == 0`." >}}
    if y == 0:
        return 1
    if x == 0:
        return 0
{{< /codestep-block >}}

{{< codestep-block desc="On définit une variable `resultat = x` puis, avec une boucle `while`, on multiplie `resultat` par `x`, `y - 1` fois" >}}
    resultat = x
    while y > 1:
        resultat *= x
        y -= 1
{{< /codestep-block >}}

{{< codestep-block desc="On renvoie la valeur `resultat`" >}}
    return resultat
{{< /codestep-block >}}


{{< codestep-block desc="On appelle la fonction `puissance`" run=true >}}

# `resultat` prend la valeur que renvoie `puissance(2, 3)`
resultat = puissance(2, 3)
# Puis on affiche `resultat`
print(resultat)

# On peut aussi directement afficher la valeur retournée
# par la fonction `puissance`
print(puissance(5, 2))
{{< /codestep-block >}}
{{< /codestep >}}
</details>

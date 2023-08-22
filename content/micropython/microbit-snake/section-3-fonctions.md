# C'est parti !

## Les fonctions

Tu peux commencer à coder en téléchargeant le code à compléter (tout en haut de la page). Celui-ci est composé de plusieurs fonctions à compléter, ainsi que de la boucle principale de jeu (qui commence à la ligne `while longueur_serpent < 25:`).

On mettra dans la boucle du jeu les actions qu'il faudra effectuer tant que la partie n'est pas finie : déplacer le serpent, placer une pomme sur le terrain, etc.

{{% box type="warning" title=" " %}}

_Attention, les `pass` dans les fonctions sont à enlever une fois la fonction completée._
{{% /box %}}

{{% box type="info" title="Mais qu'est ce qu'une fonction ?" %}}

Une fonction est un bout de programme qui effectue une action, et que l'on va pouvoir utiliser plusieurs fois.   

Pour créer une fonction, il faut 5 éléments :
- le mot-clé `def`
- le nom de la fonction
- des parenthèses
- deux points (`:`)
- une indentation à la suite

Voici un exemple de déclaration de fonction : `def hello_world():`.

*L'indentation est l'espace que l'on mets devant une parti de code pour le considérer dans un bloc.*
*N'hésite pas à appeler un organisateur si tu n'est plus sûre de ce que c'est.*


Prenons un exemple:

```codepython
# Le mot-clé 'def' informe la création d'une fonction avec
# 'trop_bas' qui sera le nom de la fonction
def trop_bas():
    # Indentation pour montrer le début de la fonction
    print("La valeur est trop basse")

x = 0

while x < 5:
    # Ici on appelle la fonction 'trop_bas()' que l'on a définie ci-dessus
    trop_bas()
    x += 1

print("x est égal à 5")
```

Les fonctions sont très utiles et utilisées car elles peuvent aussi prendre des _paramètres_ et _renvoyer une valeur_.

Les paramètres : à l'intérieur des parenthèses qui suivent le nom de la fonction, on peut mettre un ou plusieurs paramètres qui seront utilisés comme des variables dans la fonction. Le résultat de la fonction peut dépendre ainsi des paramètres donnés.

Le `return`: ce mot-clé se trouve à la fin d'une fonction et permet de renvoyer une valeur.

```codepython
# La fonction prend une valeur et renvoie sa valeur au carré
# Ici on va utiliser le paramètre 'nombre' pour faire nos opérations
def puissance_2(nombre):
    carre = nombre * nombre
    # Ici le mot 'return' marque la fin de la fonction et renvoie la valeur 'carre'
    return carre
    # Tout ce qui est écrit après le 'return' ne sera pas lu


# Attention : on entre la valeur 5 en paramètre et on
# récupère la valeur retournée par la fonction dans la variable 'resultat'
resultat = puissance_2(5)
print(resultat)
```


Analysons ensemble le code ci-dessus (n'hésite pas à l'exécuter avant pour bien comprendre) : 
{{< codestep steps=5 lang="py" >}}

{{< codestep-block desc="On définit notre fonction qui prend un paramètre `nombre`" >}}
def puissance_2(nombre):
{{< /codestep-block >}}

{{< codestep-block desc="On utilise `nombre` pour effectuer un calcul" >}}
    carre = nombre * nombre
{{< /codestep-block >}}

{{< codestep-block desc="On renvoie la valeur de `carre`" >}}
    return carre
{{< /codestep-block >}}


{{< codestep-block desc="On appelle `puissance_2` avec `5` comme paramètre" >}}
resultat = puissance_2(5)
{{< /codestep-block >}}

{{< codestep-block desc="On affiche la valeur renvoyée par la fonction" >}}
print(resultat)
{{< /codestep-block >}}

{{< /codestep >}}
Et voilà, tu sais tout ce qu'il a à savoir sur les fonctions pour faire ton Snake ! Si tu n'as pas compris quelque chose ou que tu n'es pas sûre d'avoir tout compris, n'hésite pas à appeler un organisateur.

{{% /box %}}

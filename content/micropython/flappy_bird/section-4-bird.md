## Le jeu

Fin des explications barbantes, il est temps de rentrer dans le coeur du sujet.

Codons notre Flappy bird !

Tu peux **télécharger le code à compléter** (tout en haut de la page) pour commencer le projet. Celui-ci est composé de plusieurs fonctions à compléter, ainsi que de la boucle `while` qui correspond à la boucle principale du jeu.

{{% box type="warning" title="`pass`" %}}

Attention, les mots-clés `pass` dans les fonctions sont à enlever une fois la fonction complétée.

{{% /box %}}

Ne te laisse pas impressionner par toutes ces fonctions, allons-y étape par étape ! N'hésite pas à demander à un organisateur si tu as besoin d'une quelconque aide !

### Un oiseau, ça vole...

Commençons avec notre oiseau.

{{<figure src="resources/images/position_oiseau.png" caption="Position flappy">}}

{{% box type="exercise" title="Mission : je vole ! " %}}

```py
def deplace_oiseau(ois_x, ois_y, ois_int)
```
Cette fonction permet de déplacer notre oiseau. Pour cela, voici les différentes étapes que tu dois coder :

- Éteindre le pixel représentant l'emplacement actuel de l'oiseau ;
- Augmenter `ois_y` si `button_a` a été appuyé ;
- Diminuer `ois_y` si `button_b` a été appuyé ;
- Allumer le nouvel emplacement de l'oiseau ;
- Renvoyer la nouvelle position de l'oiseau.

{{% box type="warning" title="Tu dépasses ! " %}}

Attention à ne pas dépasser les côtés de l'écran quand tu déplaces ton oiseau.

Combien de lignes et de colonnes sur le micro:bit ?

{{% /box %}}
{{% /box %}}

{{% box type="exercise" title="Mission : Déplacement dans la boucle du jeu" %}}

Dans la boucle `while` du jeu, modifie la ligne `# TODO 1` pour appeler la fonction `deplace_oiseau`.

N'oublie pas de récupérer et d'utiliser la valeur que ta fonction renvoie.

<details>
<summary> Tu bloques ? </summary>

Notre fonction va modifier l'emplacement de notre oiseau. Cependant, elle ne modifie que les valeurs locales à la fonction, pas la valeur de `oiseau_y` utilisée dans la boucle de jeu. Il faut donc que `oiseau_y` récupère la valeur que retourne la fonction.
</details>

{{% /box %}}

Tu devrais pouvoir bouger librement ton oiseau de haut en bas sans avoir d'erreur.

Si tu n'y arrives pas, n'hésite pas à appeler un organisateur, on est là pour vous aider.

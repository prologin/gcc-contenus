# Introduction aux chaînes de caractères

On va aborder ici un type de variables en programmation très important, les chaînes de caractères.

Un caractère c'est une lettre, un chiffre, un signe de ponctuation, etc.
Une chaîne de caractères est simplement une suite de caractères, donc un mot, une phrase, ou autres.
Vous les avez déjà manipulées dans les TP précédents, notamment à l'aide de la fonction `print`.

En anglais, on appelle les chaînes de caractères des "*string*", et un caractère
devient "*character*" abrégé "*char*".

Les string s'écrivent entre guillemets `"` mais peuvent aussi s'écrire entre apostrophes `'`.

```codepython
chaine = "Bonjour !"
print(chaine)

stage = 'GCC'
print(stage)
```

Les string peuvent contenir des *caractères spéciaux*.
Ces caractères sont similaires aux caractères normaux, mais ne peuvent pas s'écrire directement.

Le caractère *sauter une ligne* ne peut, notamment pas vraiment s'écrire dans le code avec juste un appui sur la touche entrée.

Ceci provoque une erreur :

```codepython
print("Ceci est une
nouvelle ligne")
```

Pour pallier ce problème il existe une façon d'écrire les **caractères spéciaux**.
Cette façon consiste à écrire le caractère `\` suivi d'un autre caractère.

```codepython
print("Ceci est une\n nouvelle ligne")
# \n permet de sauter une ligne
```

Les caractères spéciaux communs sont les suivants :
- `\t` pour les tabulations
- `\n` pour les retours à la ligne
- `\"` pour insérer un `"` dans une chaine de caractères, sans entrer en conflit avec les guillemets de début de chaîne
- `\'` pour insérer une apostrophe dans une chaîne de caractères
- `\\` pour insérer un `\`


```codepython
print("Le canard m'a dit \"Bonjour !\"")
print("Code:")
print("\tprint()")
print("\tprint(\'Bonjour\\n\')")
```


Il existe d'autres caractères spéciaux comme les emojis :

```codepython
print("Yes ! \u26F5")
print("Yes ! \u265E")
```

{{% box type="exercise" title="Exercice 1" %}}

Affiche cette chaîne de caractères :
> 
> "Nuit et jour à tout venant  
> Je chantais, ne vous déplaise.  
> \- Vous chantiez ? J'en suis forte aise ;  
> Eh bien dansez maintenant." 🐜🍂

Combien de caractères doivent être utilisés pour l'écrire avec un seul appel à la fonction `print()` ?

{{% /box %}}

Bravo ! Passe à la section suivant pour en apprendre plus sur les string.
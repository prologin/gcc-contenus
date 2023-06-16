# Ça fait beaucoup de lignes

Tu sais maintenant comment créer des programmes assez complexes. Mais imaginons
que tu veuilles effectuer plusieurs fois la même action. Tu pourrais écrire un
bout de code et le copier/coller le nombre de fois que tu veux le répéter, mais
c'est assez long et peu efficace. Eh bien ça tombe bien, il existe en Python ce
que l'on appelle des `boucles`, c'est-à-dire des petits bouts de codes qui
peuvent se répéter. Il en existe deux : les boucles `for` et les boucles
`while`. Nous allons commencer par la première.

## Pour un certain nombre de fois

Nous allons donc ici traiter la boucle `for`. Ce type de boucle sert à répéter
un certain nombre de fois un bloc de code. Ce nombre de répétitions **doit être
connu** d'une manière ou d'une autre. Le cas où ce nombre n'est pas connu est
traité dans la boucle `while` un peu plus bas. 

Voyons le fonctionnement de ce type de boucles à travers un exemple simple : 

```python
for i in range(5):
    # Ce qui suit va être répété 5 fois, une variable `i` est créée,
    # et va prendre successivement les valeurs 0, 1, 2, 3 puis 4.
    display.scroll("Coucou numéro " + str(i))
    sleep(500)

display.show(Image.HAPPY) # Cette ligne de code n'est pas répétée
```

- _Ligne 1_ : Ici, c'est la déclaration de la boucle. C'est la partie la plus complexe.
              Le mot clé `for` indique que la déclaration commence.
              Ensuite, il y a une variable `i`. Elle peut prendre n'importe quel nom,
              ça n'a pas d'importance. Il y a enfin le `range(5)` qui nous indique que
              la boucle sera répétée `5` fois. Comme indiqué en commentaire, la variable
              `i` prendra successivement les valeurs de 0 à 5 exclu. Le `5` peut être
              remplacé par n'importe quelle valeur numérique entière. 
- _Ligne 4_ : Affiche la phrase `"Coucou numéro "` suivie de la valeur de `i`. La fonction
              `str()` permet de transformer un entier en une chaîne de caractères. 
- _Ligne 5_ : Met en pause le programme pendant _500_ millisecondes
- _Ligne 7_ : Affiche un smiley souriant

Voici un petit schéma pour bien différencier les différents blocs de code : 

{{<figure src="resources/images/for_loop.png" width=400 >}}


Bien sûr, il est possible d'"emboîter" des boucles les unes dans les
autres :

```python
# La prochaine ligne ne sera exécutée qu'une seule fois:
display.scroll("start")

for i in range(5):  # Début du bloc `for` n°1
    # La prochaine ligne sera exécutée 5 fois:
    display.scroll("i=" + str(i))

    for j in range(5):  # Début du bloc `for` n°2
        # La prochaine ligne sera exécutée 5*5 = 25 fois:
        display.scroll("j=" + str(j))
    # Fin du bloc `for` n°2

    # La prochaine ligne sera aussi exécutée 5 fois:
    display.scroll("i=" + str(i))
# Fin du bloc `for` n°1

# La prochaine ligne ne sera aussi exécutée qu'une seule fois:
display.scroll("end")
```

### Mini-exercice
**But :** Comme pour l'exercice 2, Joseph voudrait connaître le résultat de la
multiplication de différents nombres. Sauf que cette fois-ci, il ne veut pas se
limiter à deux nombres. Écris un programme qui multiplie 3 nombres entre eux. Tu
peux récupérer les nombres en comptant le nombre d'appuis sur le bouton A, en
laissant quelques secondes à chaque fois. 

_Aide :_ Pour savoir quand tu passes au nombre suivant, tu peux allumer la LED
de coordonnée `(0, i)` à chaque début de boucle. 



## Tant que 

La boucle **while** est une boucle dont le bloc de code est répété tant qu'une
condition est vérifiée (d'où son nom :D). Illustrons cette boucle à travers un
exemple de code : 

```python
while button_a.get_presses() == 0:
    display.scroll("Appuie sur le bouton A pour sortir")
    sleep(500)

display.scroll("Tu es sorti !")
```

Nous avons sur la première ligne la déclaration de la boucle avec le mot-clé
`while` suivi de la condition d'arrêt. Ici, la boucle s'arrêtera lorsque tu 
appuieras sur le bouton A. 
Pour ce qui concerne les lignes suivantes, tu connais déjà leur comportement. 

### Mini-exercice
**But :** Écris un programme qui compte et affiche le nombre d'appuis sur les
boutons A et B avant que le bouton tactile ne soit touché. 

_Aide :_ Tu peux utiliser `display.show(Image.ALL_CLOCKS)` pour afficher une
horloge d'attente. 


# Partie IV : Améliorations

Une fois le jeu fini, tu peux ajouter plusieurs améliorations. Note que chaque amélioration est réalisable indépendamment des autres.  
Avant de commencer cette partie, vérifie que ton jeu fonctionne correctement. Si ce n'est pas le cas, n'hésite pas à demander de l'aide aux organisateurs !

---
## Accélération de la chute des pommes !

Pour rendre la partie plus difficile et amusante, tu peux augmenter la vitesse de chute des pommes au fur et à mesure de l'avancement de la partie.  
*Il faut tout de même s'assurer que le jeu reste faisable, en posant par exemple une limite de vitesse de chute.*

## Rajout d'un son !

À chaque fois que tu collectes une pomme, tu peux rajouter un petit son. Pour ce faire, tu peux utiliser la fonction `music.play()` comme dans l'exemple ci-dessous !

```python
# Importe la librairie music
import music

# Joue une note
music.play("F:2")
```

N'hésite pas à demander à un organisateur de l'aide si tu souhaites changer de note ou même faire une mélodie !

## Jouons pour la fin des temps

Cette amélioration va surement pas mal changer ton code, donc n'hésite pas à faire une sauvegarde de ce qui marche avant de modifier quoi que ce soit.

Ton but sera d'ajouter la possibilité qu'à la fin de la partie tu puisses, soit en relancer une autre en appuyant sur le bouton A, soit tout arrêter en appuyant sur le bouton B. Avec cet ajout, tu peux t'amuser à créer une nouvelle variable `best_score` pour que tu puisses avoir le meilleur score que tu as atteint depuis que tu as lancé ton programme.

Pour finir, avec ce meilleur score tu peux même ajouter la possibilité de l'afficher en appuyant sur le logo.

N'hésite pas à afficher un petit message quand tu bats le précédent `best_score`. Un peu de challenge voyons !

{{% box type="info" title="Un peu d'aide ?" %}}

Ce qui serait amusant c'est que tu essayes de le faire toute seul. Avec tes idées, ta façon de penser et ta manière de faire. Tu peux bien évidemment appeler un organisateur si quelque chose te bloque.

Si tu ne sais vraiment pas par où commencer ou que tu veux juste continuer à être quelque peu guidé, voici quelques petites pistes :

- Tu vas avoir besoin d'une autre boucle qui englobe tout, et donc une autre variable qui permettra de déterminer si le jeu s'arrête ou pas.
- Il te faudra trois conditions qui vérifient si tu appuis sur les différents boutons. Cela te permettra d'effectuer les actions voulues.
- Pour finir, à la fin d'une partie, n'oublie pas de mettre à jour le `best_score` si nécessaire et d'afficher un message selon si tu l'as battu ou pas.

{{% /box %}}

---

Bravo, te voilà arrivée à la fin de ce projet !  
Tu as maintenant un code qui fonctionne. Si tu as des idées d’amélioration, essaye de les mettre en place par toi-même !
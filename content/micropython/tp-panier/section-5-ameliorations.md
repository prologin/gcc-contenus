# Partie IV : Améliorations

Une fois le jeu fini, tu peux ajouter plusieurs améliorations. Note que chaque amélioration est réalisable indépendamment des autres.  

{{% box type="warning" title="Tout fonctionne ?" %}}

Avant d'intégrer des améliorations à ton jeu du panier, assure-toi qu'il fonctionne déjà parfaitement. Si ce n'est pas le cas, n'hésite pas à demander de l'aide aux organisateurs !

{{% /box %}}

---

## Bonus 1 : Accélérer la chute des pommes

Pour rendre la partie plus difficile et amusante, tu peux augmenter la vitesse de chute des pommes au fur et à mesure de l'avancement de la partie.  

{{% box type="warning" title="Pas trop vite non plus !" %}}

Il faut tout de même s'assurer que le jeu reste faisable, en posant par exemple une limite de vitesse de chute maximum.

{{% /box %}}


## Bonus 2 : Rajouter un son

À chaque fois que tu collectes une pomme, tu peux rajouter un petit son. Tu peux utiliser la fonction `music.play` comme dans l'exemple ci-dessous !

```python
# Importer la bibliothèque `music`.
import music

# Jouer une note.
music.play("F:2")
```

N'hésite pas à demander à un organisateur de l'aide si tu souhaites changer de note ou même faire une mélodie !


## Bonus 3 : Pour la fin des temps !

{{% box type="warning" title="Mieux vaut être prudent" %}}

Cette amélioration va modifier une grande partie de ton code. Avant de commencer, pense à sauvegarder une version de ton programme qui fonctionne, afin de pouvoir y revenir en cas de problème.

{{% /box %}}

### Bonus 3.1 : Choix de fin de partie

Ton objectif est d'ajouter un choix à la fin de la partie :
* appuyer sur le bouton A pour relancer une nouvelle partie ;
* appuyer sur le bouton B pour arrêter complètement le jeu.

### Bonus 3.2 : Meilleur score

Pour aller plus loin, tu peux créer une variable `best_score`. Elle servira à mémoriser le meilleur score obtenu depuis le lancement du programme.

Tu peux aussi ajouter la possibilité d'afficher ce meilleur score en appuyant sur le logo du micro:bit.

Enfin, n'hésite pas à afficher un petit message lorsque tu bats ton précédent `best_score`.


{{% box type="info" title="Un peu d'aide ?" %}}

Ce qui serait amusant, c'est que tu essayes de le faire toute seule : avec tes idées, ta façon de penser, et ta manière de faire. Bien-sûr, tu peux appeler un organisateur si quelque chose te bloque.

Si tu ne sais vraiment pas par où commencer ou que tu veux juste continuer à être un peu guidé, voici quelques petites pistes :
* prévoir une boucle supplémentaire qui englobe l'ensemble du jeu, ainsi qu'une variable permettant de décider si le programme continue ou s'arrête ;
* utiliser plusieurs conditions pour détecter les appuis sur les boutons et déclencher les actions correspondantes ;
* à la fin de chaque partie, mettre à jour la variable `best_score` si nécessaire et afficher un message indiquant si le record a été battu.

{{% /box %}}

---

Bravo, te voilà arrivée à la fin de ce projet !  

Tu as maintenant un code qui fonctionne. Si tu as encore d'autres idées d'améliorations, essaye de les mettre en place par toi-même ! Peut-être que les organisateurs les rajouterons à ce sujet. 😉

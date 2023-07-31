# Écriture de messages

Maintenant que nous pouvons traduire du morse en lettres de l'alphabet normal,
Joseph va pouvoir écrire le message qu'il voit sur le mur et l'envoyer à sa
soeur ! 

Enfin il nous reste quand même un petit problème : comment fait-il pour faire ça ?

{{% box type="exercise" title="Mission 5 : Envoi de messages" %}}

Grâce à un système de télépathie que seul Joseph et les organisateurs maîtrisent,
Joseph nous a transmis ce dont il avait besoin pour communiquer avec sa soeur.
Il nous a dit qu'il voudrait une fonction qui, lorsqu'il appuie sur le logo :

- Affiche une image de son choix
- Lui permet d'entrer ce qu'il voit sur le mur (c'est la fonction
  `creer_message()` de ton fichier de code). Cela permettra d'utiliser la
  fonction `morse_vers_lettre()`.

Il nous a aussi dit qu'il voudrait pouvoir :

- Écrire un point (`'.'`) en appuyant sur le bouton `A`
- Écrire un trait (`'-'`) en appuyant sur le bouton `B`
- Valider l'encodage en appuyant à nouveau sur le logo
- Valider son message en appuyant sur les boutons `A` et `B` en même temps. Cela
  devra afficher sur le `micro:bit` le message validé.

<details>
<summary>Besoin d'aide ? Clique ici !</summary>

Si tu ne vois pas comment faire, tu peux commencer par répondre à ces questions :

- Comment je récupère et stocke les appuis de Joseph sur les boutons ?
- Comment je détecte si le logo est appuyé ?
- Comment je peux traduire chaque lettre en morse ?
- Comment je peux concaténer des lettres ?

</details>

{{% /box %}}

Si jamais tu as besoin d'aide, n'hésite surtout pas à appeler un organisateur
pour t'aider (ils maîtrisent tous la télépathie et peuvent communiquer avec
Joseph pour savoir ce qu'il veut faire).
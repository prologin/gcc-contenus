# Écriture de messages

Maintenant que nous pouvons traduire du morse en lettres de l'alphabet normal,
Joseph va pouvoir écrire le message qu'il voit sur le mur et l'envoyer à sa
soeur ! 

Enfin il nous reste quand même un petit problème : comment fait-il pour faire ça ?

{{% box type="exercise" title="Mission 5 : Envoi de messages" %}}

Grâce à un système de télépathie que seul Joseph et les organisateurs maîtrisent,
Joseph nous a transmis ce dont il avait besoin pour communiquer avec sa soeur.
Il nous a dit qu'il voudrait que la fonction `creer_message()` réponde aux
critères suivants :

- Avec le bouton `A`, on pourra écrire un point ('`.`').
- Avec le bouton `B`, on pourra écrire un tiret ('`-`').
- En appuyant sur le logo, on validera le code morse actuel pour le convertir
  en lettre et l'ajouter au message.
- Pour terminer notre message, on devra secouer le micro:bit.

Si notre lettre déchiffrée est invalide (est égale à `None`), il faudra afficher
un smiley `ANGRY`. Dans le cas contraire, si elle est valide, il faudra
afficher un smiley `HAPPY` et rajouter notre lettre au message.

<details>
<summary>Besoin d'aide ? Clique ici !</summary>

Si tu ne vois pas comment faire, tu peux commencer par répondre à ces questions :

- Comment je vérifie si le micro:bit est secoué ou non ?
- Comment je détecte si le logo est appuyé ?
- Comment je peux traduire chaque lettre en morse ?
- Comment je peux concaténer des lettres ?
- Comment je peux sortir d'une boucle avec un seul mot-clé ?

</details>

{{% /box %}}

Si jamais tu as besoin d'aide, n'hésite surtout pas à appeler un organisateur
pour t'aider (ils maîtrisent tous la télépathie et peuvent communiquer avec
Joseph pour savoir ce qu'il veut faire).
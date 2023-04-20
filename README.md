# GCC resources
Ce dépôt contient tous les travaux pratiques [des stages Girls Can 
Code!](https://girlscancode.fr/). Les stages se concentrent autour de 
l'apprentissage du Python mais couvrent de nombreux sujets comme le réseau,
la programmation web (HTML, CSS), Unix ou encore la programmation orientée
objet.

Nous encourageons vivement la réutilisation, modification et amélioration de
ce contenu pédagogique. En particulier si vous souhaitez vous servir de ces
sujets pour des cours ou pour monter un club d'informatique, faites-le sans
scrupules !

# Fonctionnement de Hugo
Pour lancer le site en local, il suffit de taper ces commandes dans un
terminal : 

```bash
git submodule update --init themes/gcc
./build.sh
hugo server
```
Il est alors marqué sur quel port trouver le site en local (souvent le port `1313`).

# Ajouter le support d'un langage pour les codeblocks intéractifs.

Pour l'instant, les langages suivants sont supportés:

- Python (module Turtle inclus)
- HTML

Dans le cas où en ajouter un nouveau serait intéressant, voici les étapes à suivre:

1. Ajouter le langage dans LANGS dans `themes/gcc/static/js/codemirror_global.js`.
2. Ajouter le script du mode _CodeMirror_ correspondant dans `themes/gcc/layouts/_default/single.html`
3. Ajouter un fichier `themes/gcc/layouts/_default/_markup/render-codeblock-code<langage>.html`. S'inspirer de ceux existant.
4. Nommer le placeholder du code `code-<lang>-input-{{.Ordinal}}`. `{{.Ordinal}}` est une macro de Hugo qui est remplacée par son numéro de codeblock. C'est très important, car c'est ce qui permet au code de savoir le code de quel codeblock exécuter, et sur quel codeblock afficher la sortie.
5. Dans la partie JS, récupérer les textAreas et output dont on a besoin, créer un objet CodeMirror (se référer au code existant), et ensuite enregistrer le block en suivant le nom `<lang>{{.Ordinal}}`.
6. Dans `.../codemirror_global.js`, ajouter un commentaire `// === <lang> related ===` et créer la fonction `runItLang(content)`, où `content` est le deuxième argument passé à `addBlock()`.
7. Toujours dans `.../codemirror_global.js`, ajouter un appel à la fonction `runItLang()` dans `runIt()`.
8. Enfin, débugger pour fix les étapes que j'ai oubliées de citer.

# Matériel utilisé
Accessoirement, pendant nos stages nous utilisons l'éditeur
[Mu](https://codewith.mu/) que nous recommandons vivement. Pour l'utilisation
des microbits une version en ligne est également disponible
[ici](https://python.microbit.org/v/2.0).


# License
<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">
<img alt="Creative Commons License" style="border-width:0"
src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a>

This work is licensed under a [Creative Commons
Attribution-NonCommercial-ShareAlike 4.0 International
License](http://creativecommons.org/licenses/by-nc-sa/4.0/).

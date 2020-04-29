# GCC resources

[![Build Status](https://travis-ci.com/prologin/gcc-resources.svg?branch=master)](https://travis-ci.com/prologin/gcc-resources)

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">
<img alt="Creative Commons License" style="border-width:0"
src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a>

This work is licensed under a [Creative Commons
Attribution-NonCommercial-ShareAlike 4.0 International
License](http://creativecommons.org/licenses/by-nc-sa/4.0/).

Ce dépôt contient tous les travaux pratiques [des stages Girls Can 
Code!](https://gcc.prologin.org/). Les stages se concentrent autour de 
l'apprentissage du Python mais couvrent de nombreux sujets comme le réseau,
la programmation web (html, css), unix ou encore la programmation orientée
objet.

Nous encourageons vivement la réutilisation, modification et amélioration de
ce contenu pédagogique. En particulier si vous souhaitez vous servir de ces
sujets pour des cours ou pour monter un club d'informatique, faites-le sans
scrupules !

Chaque dossier correspond à un sujet et contient au minimum :

- `nom_de_sujet.md`: c'est ce qui contient le texte du sujet au format Markdown, 
  Vous pouvez le visualiser directement depuis Github mais il se peut qu'il manque des 
  images (ou qu'elles s'affichent en trop grand). Cela peut être un bon moyen 
  pour regarder rapidement ce contenu mais nous ne donnons pas les sujets sous 
  cette forme.
  Nous générons un fichier latex à partir du Markdown et il est ensuite
  compilé pour donner un pdf. Vous pouvez trouver les pdf générés [ici](https://github.com/prologin/gcc-resources/tree/gh-pages).
- `Makefile` c'est ce qui permet de compiler le sujet en utilisant simplement
  la commande `make` dans le dossier du TP que l'on souhaite compiler. Il
  génère à la fois le fichier latex et le pdf.
- `README.md` C'est un fichier qui décrit le principe du TP et les éventuelles
  mises en place nécessaires.
- (optionnel) `notes_orga.md` il s'agit de conseils pour les encadrants qui
  dirigent le sujet. On y précise les points délicats du TP et des conseils
  pédagogiques.

Accessoirement, pendant nos stages nous utilisons l'éditeur
[Mu](https://codewith.mu/) que nous recommandons vivement. Pour l'utilisation
des microbits une version en ligne est également disponible
[ici](https://python.microbit.org/v/2.0).

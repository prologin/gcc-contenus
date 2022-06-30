# GCC resources
Ce dépôt contient tous les travaux pratiques [des stages Girls Can 
Code!](https://girlscancode.fr/). Les stages se concentrent autour de 
l'apprentissage du Python mais couvrent de nombreux sujets comme le réseau,
la programmation web (html, css), unix ou encore la programmation orientée
objet. 

Nous encourageons vivement la réutilisation, modification et amélioration de
ce contenu pédagogique. En particulier si vous souhaitez vous servir de ces
sujets pour des cours ou pour monter un club d'informatique, faites-le sans
scrupules !

# Création d'un sujet
Avant de commencer l'écriture d'un nouveau sujet, il faut d'abord construire son
architecture. Pour ce faire, une simple commande suffit à créer un dossier avec
la bonne architecture : 
```bash
hugo new -k subject [type_de_TP]/[nom_du_tp]
```
Il ne reste plus qu'a écrire le sujet dans le fichier `index.md`, ainsi
que d'écrire un `README.md` décrivant rapidement le sujet. Ce fichier sera
essentiellement destiné aux organisateurs et permet d'éclaicir certaines
particularité du TP. 



# Fonctionnement de Hugo
Pour lancer le site en local, il suffit de faire 
```bash
hugo server --renderToDisk --noHTTPCache
```
Il est alors marqué sur quel port trouver le site en local (souvent le port `1313`).


# Matériel utilié
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

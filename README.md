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

## Avant de commencer

Avant de commencer l'écriture d'un nouveau sujet, il faut d'abord construire son
architecture. Pour ce faire, une simple commande suffit à créer un dossier avec
la bonne architecture : 
```bash
hugo new -k subject [type_de_TP]/[nom_du_tp]
```

Par exemple, pour créer un nouveau sujet micropython s'appelant _"Usine"_, il
faut faire 
```bash
hugo new -k subject micropython/usine
```

## Remplir les meta-data

### `code_stub_url`

Toutes les meta-data du squelette sont nécessaires, sauf le champs
`code_stub_url`, qui n'est utile que s'il y a un skeleton à transmettre aux
participantes. Le cas échéant, ce champs doit contenir un lien vers un fichier
(`zip` s'il y a plus d'un fichier à transmettre). 

### `weight`
Cet attribut est important car il permet de définir l'ordre d'apparition de
votre sujet sur la page. 
Voici une petite convention à suivre pour le nombre à entrer dans ce champs afin 
de maintenir une organisation claire pour les participantes : 
- `1` si c'est un tutoriel de base
- `5` si c'est un TP simple utilisant des notions basiques
- `10` si c'est un TP normal
- `15` si c'est un TP complexe ou un cours à propos d'une notion complexe
- `20` si c'est quelque chose de vraiment très complexe


## Quelques précisions supplémentaires

### Insérer une image

Vous pouvez insérer une image dans votre sujet grâce à cette ligne, que vous
devez placer à l'endroit où l'image doit se situer : 
```go
{{< figure src="la_source" >}}
```

Pour connaître toutes les options possibles de cette commande, vous pouvez
trouver la documentation [ici](https://gohugo.io/content-management/shortcodes/#use-hugos-built-in-shortcodes)


## À vous de jouer !

Il ne reste plus qu'à écrire le sujet dans le fichier `index.md`. Vous pouvez
aussi écrire un `README.md` additionnel si jamais certaines informations doivent
être transmises aux organisateurs mais pas aux participantes. 
Ce fichier sera essentiellement destiné aux organisateurs et permet d'éclaicir certaines
particularités du TP. 



# Fonctionnement de Hugo
Pour lancer le site en local, il suffit de taper cette commande dans un
terminal : 
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

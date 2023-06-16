# Comment créer un sujet de TP ?

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

### D'autres ressources ?

Dans l'architecture de votre projet, le dossier `resources/images` est là pour
stocker les images de votre sujet. 
Vous pouvez aussi avoir d'autres types de ressources, comme une référence (`ref`), que vous
pouvez placer dans le dossier `resources/ref`, ou des ressources que les filles peuvent
télécharger, que vous pouvez placer dans le dossier `resources/given_resources`. 

Pour les autres types de resources, vous êtes libres de les placer où vous
voulez dans le dossier `resources`. 


## Cheat-sheet

Une cheat-sheet existe aussi pour présenter toutes les possibilités qui existent
pour créer un nouveau TP. 
Le code source de cette cheat-sheet se situe dans
`content/draft/exemple/index.md`. Vous pouvez visualiser le rendu, vous
pouvez lancer `hugo` avec les commandes :


```bash
git submodule update --init themes/gcc
./build.sh
hugo server --buildDrafts
```

Il vous suffit alors de chercher la cheat-sheet dans `Draft folders/TP Exemple`

N'hésitez pas à aller faire un tour sur : https://gitlab.com/prologin/tech/packages/hugo-base-theme/ pour améliorer le thème, ou voir ce qu'il est possible de faire.

## Remplir les meta-data

### `code_stub_url`

Toutes les meta-data du squelette sont nécessaires, sauf le champs
`code_stub_url`, qui n'est utile que s'il y a un `skeleton` à transmettre aux
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


## À vous de jouer !

Il ne reste plus qu'à écrire le sujet. Pour connaître le format d'un TP plus en détails, consultez (ce fichier)[https://gitlab.com/prologin/tech/packages/hugo-base-theme/-/blob/main/README.md?plain=1&ref_type=heads]. Vous pouvez

aussi écrire un fichier `README.md` additionnel si jamais certaines informations doivent
être transmises aux organisateurs mais pas aux participantes. 
Ce fichier sera essentiellement destiné aux organisateurs et permet d'éclaicir certaines
particularités du TP. 


# Quelques conventions

Dans le but de maintenir une harmonie et que la forme des TPs soit cohérente entre tous les sujets, il est nécessaire de respecter ces quelques conventions : 
- Utiliser le tutoiement
- S'adresser aux participantes comme si on leur parlait directement
- chaîne et non chaine 👀

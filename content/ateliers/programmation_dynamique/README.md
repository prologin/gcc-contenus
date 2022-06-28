# Atelier programmation dynamique

Atelier réalisé durant GCC! 2018 à Paris en Août, car plusieurs participantes
intéressées par l'algorithmique voulaient savoir ce qu'était la programmation
dynamique. Groupe de 5-6 filles.

L'article utilisé comme support :
https://haltode.fr/algo/general/approche/dynamique.html (cf le pdf
`programmation_dynamique.pdf` de l'article)

Dans un premier temps on pose un problème aux filles avec des vraies données
(dans l'article c'est de remplir un cargo pour l'ISS). Le but est de les faire
chercher chacune une solution optimale au problème. Rapidement, certaines vont
vouloir utiliser des approches gloutonnes et l'important dans ce début d'atelier
est de se rendre compte qu'on trouve tout le temps des contre-exemples aux
solutions gloutonnes ! L'exemple de l'article est notamment fait pour exposer
facilement quelques idées classiques : trier par importance et trier par poids.
Une fois que les filles ont résolu le problème on essaie justement de penser à
**comment** elles ont trouvé la solution. À nouveau, des idées de gloutons qui
passent, mais elles se rendent compte assez vite qu'il n'y a pas de principe
général à appliquer. Il faut donc savoir prendre du recul, et se dire que nous
ne sommes pas capables de coder quelque chose d'efficace tout de suite, on
essaie alors de coder un programme qui résout le problème de manière naïve.
Ensuite en analysant l'algorithme naïf on trouvera quoi améliorer.

On se lance donc dans la rédaction de la solution naïve qui teste toutes les
combinaisons, là il faut que les filles soient un minimum à l'aise avec la
récursivité (ce qui n'est pas évident au début). Bien expliquer les appels
récursifs, avec un appel représentant le choix « On prend l'objet » et un autre
appel pour « On ne prend pas l'objet ». Représenter cela sous la forme d'arbres
des appels peut aider. La rédaction du pseudo-code peut se faire tous ensemble
ou individuellement.

Bien, nous avons désormais une solution qui marche, maintenant jugeons son
efficacité. Introduire le tableau de benchmark, on se rend compte rapidement que
notre programme est assez vite inutilisable ! Mais pourquoi ? Dessiner l'arbre
des appels avec les paramètres, faire le lien entre le fait que notre fonction
appelée deux fois avec les mêmes paramètres renvoient deux fois le même
résultat. Montrer les pourcentages de répétition. La solution semble donc assez
simple : on évite de recalculer deux fois les mêmes résultats. Pour celles
intéressées pourquoi pas parler de complexité algorithmique (ou alors en faire
un autre atelier !).

Demander aux filles des idées de comment retenir l'information, il faut bien
qu'elles comprennent que les arguments de notre fonction représentent le
contexte et la valeur de retour le résultat qu'on aimerait stocker. Ici
plusieurs solutions possibles, un tableau ou une table de hachage. Ajouter les
quelques lignes de code pour dynamiser notre algorithme (l'écrire dans une
**autre** couleur sur le tableau blanc). Maintenant, discuter des benchmarks de
notre nouvelle version.

Résumer ce qui a été abordé :

1. Les tentatives d'approche gloutonnes qui ne fonctionnent pas.
2. L'algorithme naïf qui constitue une solution qui fonctionne bien que non
   efficace.
3. L'identification et la raison de la lenteur de l'algorithme naïf.
4. Dynamisation de l'algorithme (très rapide !)

Évoquer le trade-off entre mémoire et temps, car les algorithmes dynamiques ne
sont généralement pas « gratuits ». Rappeler que la programmation dynamique
n'est efficace que si on a des sous-problèmes **communs**. Donner d'autres
exercices classiques.

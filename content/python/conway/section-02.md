---
show_toc: false
---


# Comment ça fonctionne ?

Dans ce jeu, chaque case représente une cellule qui peut avoir deux états : mort ou vivant.

On appelle chaque tour du jeu une *génération*, c'est-à-dire lorsque le plateau est mis-à-jour.

Le *Jeu de la Vie* suit trois règles importantes qui permettent au jeu de :
- Faire naître une cellule
- Garder une cellule en vie
- Faire mourir une cellule



## La naissance d'une cellule

Si une cellule morte a exactement trois voisines vivantes, elle fera alors naître une cellule à la prochaine génération.

<!-- Exemple -->
{{< gallery steps=2 >}}

{{< gallery-img src="./resources/images/section02/ConwayBorn.png" desc="La cellule en rouge a trois voisines vivantes, elle fait alors naître une cellule à sa place à la prochaine génération." >}}
{{< gallery-img src="./resources/images/section02/ConwayBorn2.png" desc="Une cellule vient de naître au niveau de la case rouge !" >}}

{{< /gallery >}}

## La survie d'une cellule

Si une cellule déjà vivante a deux ou trois voisines vivantes, alors elle reste en vie.
<!-- Exemple -->

<table>
    <tr>
      <td style="width: 2000px;height: 400px">
        <img style="width:1200px;" src="./resources/images/section02/ConwayKeep2.png">
      </td>
      <td style="width:2000px">
        <img style="width:1200px;" src="./resources/images/section02/ConwayKeep.png">
      </td>
    </tr>
    <tr>
      <td>
        La cellule en rouge a trois voisines vivantes, elle reste donc en vie !
      </td>
      <td>
        La cellule en rouge a deux voisines vivantes, elle reste donc en vie !
      </td>
    </tr>
</table>


## La mort d'une cellule 

Si une cellule ne naît pas ou ne survit pas, elle meurt.
<!-- Exemple -->

{{< gallery steps=2 >}}

{{< gallery-img src="./resources/images/section02/ConwayUnder1.png" desc="La cellule en rouge n'a pas de voisines vivantes, il y a donc sous-population" >}}
{{< gallery-img src="./resources/images/section02/ConwayUnder2.png" desc="La cellule en rouge meurt donc !" >}}

{{< /gallery >}}

{{< gallery steps=2 >}}

{{< gallery-img src="./resources/images/section02/ConwayOver1.png" desc="La cellule en rouge a quatre voisines vivantes, il y a donc surpopulation" >}}
{{< gallery-img src="./resources/images/section02/ConwayOver2.png" desc="La cellule en rouge meurt donc !" >}}

{{< /gallery >}}
# 
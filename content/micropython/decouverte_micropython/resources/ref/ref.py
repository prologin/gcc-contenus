from microbit import *

#*** LES FONCTIONS MICROBIT ***

"""
Mini-exercice 1 :
But : Affiche un coeur sur l'écran.
"""
display.set_pixel(0, 1, 9)
display.set_pixel(0, 2, 9)
display.set_pixel(1, 0, 9)
display.set_pixel(1, 3, 9)
display.set_pixel(2, 1, 9)
display.set_pixel(2, 4, 9)
display.set_pixel(3, 0, 9)
display.set_pixel(3, 3, 9)
display.set_pixel(4, 1, 9)
display.set_pixel(4, 2, 9)

#----------

"""
Mini-exercice 2 :
But : Affiche un smiley content sur l'écran du `micro:bit`.
"""
display.show(Image.HAPPY)

#----------

"""
Mini-exercice 3 :
But : Affiche le texte de ton choix sur l'écran du `micro:bit`.
"""
display.scroll("Un message")

#----------

"""
Exercice 1 :
But : Max, qui est un ami de Joseph, te demande de créer un programme
pour que son `micro:bit` affiche une barre de chargement sur la ligne du milieu, 
puis affiche le message `"Salut Joseph !"` suivi d'un smiley qui sourit. 
"""
# Barre de chargement
display.set_pixel(0, 2, 9)
sleep(500)
display.set_pixel(1, 2, 9)
sleep(500)
display.set_pixel(2, 2, 9)
sleep(500)
display.set_pixel(3, 2, 9)
sleep(500)
display.set_pixel(4, 2, 9)
sleep(500)

# Affiche le message "Salut Joseph !"
display.scroll("Salut Joseph !")

# Affiche un smiley qui sourit
display.show(Image.HAPPY)

#*** LES VARIABLES ***

"""
Mini-exercice 4 :
But : crée une variable avec la valeur 42, puis ajoutes-y 2 et affiche-la 
sur l'écran.
"""
a = 42
a = a + 2
display.scroll(a)

#----------

"""
Mini-exercice 5 :
But : Joseph a envie de bananes. Le marchand lui propose de les acheter pour
2€ l'unité. Combien 10 bananes vont-elles lui coûter ? Affiche le résultat sur 
le `micro:bit`.
"""
prix = 2
total = 2 * prix
display.scroll(total)

#----------

"""
Mini-exercice 6 :
But : Comme dans l'exercice précédent, Joseph a besoin de savoir combien 
vont lui coûter ses bananes. Mais le marchand a augmenté le prix et les bananes 
coûtent désormais 3€ chacune. Après avoir calculé, affiche `"Payer (le prix) 
pour 10 bananes ? Mais c'est beaucoup trop cher !"` en remplaçant `le prix` par 
sa valeur.
"""
prix = 3
total = 10 * prix
display.scroll("Payer " + str(prix) + " pour 10 bananes ? Mais c'est beaucoup trop cher !")

#----------

"""
Mini-exercice 7 :
But : Après une discussion intense avec le marchand, Joseph n'est plus sûr
de ses calculs. Les bananes coûtant 3€, il pense que pour 7 bananes il en aura
pour 22€. Calcule le vrai prix et affiche si celui de Joseph est le bon.
"""
display.scroll(3 * 7 == 22)

#*** LES BOUTONS ***

"""
Mini-exercice 8 :
But : Crée un programme qui affiche la somme du nombre d'appuis sur les
boutons A et B au cours des 3 dernières secondes. 
"""
sleep(3000)
a = button_a.get_presses()
b = button_b.get_presses()
display.scroll(a + b)

#----------

"""
Exercice 2 :
But : Joseph voudrait connaître le résultat de la multiplication de deux
nombres. Pour récupérer la valeur des deux nombres tu peux donner quelques secondes
à l'utilisateur pour appuyer le bon nombre de fois sur chaque bouton. Par exemple,
si pendant ce temps, tu appuies 3 fois sur le bouton de gauche et 7 fois sur celui 
de droite, le programme affichera `3 * 7 = 21` sur l'écran.
"""
sleep(2000)
a = button_a.get_presses()

sleep(2000)
b = button_b.get_presses()

display.scroll(a * b)

#----------

"""
Mini-exercice 9 :
But : Essaye de trouver ce que va afficher le programme ci-dessus pour `x =
0`, `x = 42` et `x = 238`. 


from random import randint
from microbit import *

x = randint(0, 100)  # assigne un nombre aléatoire à x compris entre 0 et 100

if x < 30:
    display.scroll('x est inférieur à 30')
elif x < 50:
    display.scroll('x est supérieur ou égal à 30 et inférieur à 50')
elif x < 80:
    display.scroll('x est supérieur ou égal à 50 et inférieur à 80')
else:
    display.scroll('x est supérieur ou égal à 80')
"""
# Résultat : 
#    - x = 0   -> 'x est inférieur à 30'
#    - x = 42  -> 'x est supérieur ou égal à 30 et inférieur à 50'
#    - x = 238 -> 'x est supérieur ou égal à 80'

#*** LES BOUTONS ***

"""
Mini-exercice 10 :
But : Comme pour l'exercice 2, Joseph voudrait connaître le résultat de la
multiplication de différents nombres. Sauf que cette fois-ci, il ne veut pas se
limiter à deux nombres. Écris un programme qui multiplie 3 nombres entre eux. Tu
peux récupérer les nombres en comptant le nombre d'appuis sur le bouton A, en
laissant quelques secondes à chaque fois. 
"""
resultat = 1
for i in range(3):
    display.set_pixel(0, i, 9)
    sleep(2000)
    tmp = button_a.get_presses()
    resultat = resultat * tmp

display.scroll(resultat)

#----------

"""
Mini-exercice 11 :
But : Écris un programme qui compte et affiche le nombre d'appuis sur les
boutons A et B avant que le bouton tactile ne soit touché. 
"""
while not pin_logo.is_touched():
    display.show(Image.CLOCKS)

display.show("A :" + str(button_a.get_presses()))
display.show("B :" + str(button_b.get_presses()))

#*** PROJET ***

"""
But : 
Joseph est dans la panade... Il aurait besoin de deux dés à 6 faces pour jouer
au Monopoly avec ses amis, mais il les a oubliés, et tout ce qu'il a à sa
disposition est un `micro:bit`... 
Joseph te demande alors de lui faire un programme qui simule un lancé de deux 
dés et affiche le résultat (le résultat est donc entre 2 et 12) lorsque le
bouton A ou le bouton B est appuyé. 
Mais comme Joseph ne veut pas que ses amis pensent qu'il a simplement
oublié les vrais dés, il voudrait donc y ajouter quelques fonctionnalités : 
- Il voudrait que si le lancé est un double, un smiley content s'affiche
juste après le chiffre
- Par contre, il voudrait que si trois doubles sont faits d'affilée, un smiley pas
content s'affiche à la place du smiley content
- Il voudrait enfin que le smiley disparaisse 2 secondes après être apparu
"""

from random import randint

nb_double = 0
while True:
    if button_a.was_pressed() or button_b.was_pressed():
        de_1 = randint(1, 6)
        de_2 = randint(1, 6)
        
        display.scroll(de_1 + de_2)
        
        if de_1 == de_2:
            nb_double += 1
            if nb_double < 3:
                display.show(Image.HAPPY)
            else: 
                display.show(Image.SAD)

        else:
            nb_double = 0
        
        sleep(2000)
        display.clear()

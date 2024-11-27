from microbit import *

#*** LES FONCTIONS MICRO:BIT ***

"""
Mini-mission 1 : Dessiner un coeur
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
Mini-mission 2 : Afficher une image
"""

display.show(Image.PACMAN)

#----------

"""
Mini-exercice 3 : Afficher du texte
"""

display.scroll("Prologin for the win!")

#----------

"""
Mission 1 : Salut Joseph !
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

display.scroll("Salut Joseph !")
display.show(Image.HAPPY)

#*** LES VARIABLES ***

"""
Mini-mission 4 : Joseph au marché
"""

prix = 2
nombre_de_bananes = 10
total = nombre_de_bananes * prix
display.scroll(total)

#----------

"""
Mini-mission 5 : Augmentation de prix !
"""

prix = 3
nombre_de_bananes = 10
total = nombre_de_bananes * prix
texte = "Payer " + str(prix) + " pour 10 bananes ? Mais c'est beaucoup trop cher !"
display.scroll(texte)

#----------

"""
Mini-exercice 6 : Les calculs ne sont pas bons !
"""

display.scroll(3 * 7 == 22)

#*** LES BOUTONS ***

"""
Mission 2 : Addition
"""

sleep(3000)
a = button_a.get_presses()
b = button_b.get_presses()
display.scroll(a + b)

#----------

"""
Mission 3 : Calculatrice compacte
"""

display.show(Image.PACMAN)
sleep(2000)
a = button_a.get_presses()

display.show(Image.SKULL)
sleep(2000)
b = button_b.get_presses()

display.scroll(a * b)

#----------

#*** LES BOUTONS ***

"""
Mini-mission 7 : Multiplication 3 fois !
"""

resultat = 1
for i in range(3):
    display.set_pixel(0, i, 9)
    sleep(2000)

    a = button_a.get_presses()
    resultat = resultat * a

display.scroll(resultat)

#----------

"""
Mini-mission 8 : Nombre d'appuis
"""

while not pin_logo.is_touched():
    display.show(Image.CLOCKS)

display.scroll("A :" + str(button_a.get_presses()))
display.scroll("B :" + str(button_b.get_presses()))

#*** PROJET ***

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

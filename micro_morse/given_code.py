#from microbit import *
#import radio

class Noeud:
    def __init__(self, key, left, right):
        """
        Cree le noeud
        """
        self.key = key # La valeur du noeud
        self.left = left # Le noeud gauche
        self.right = right # Le noeud droit

# Arbre permettant de traduire du morse
NEUF = Noeud('9', None, None)
ZERO = Noeud('0', None, None)
HUIT = Noeud('8', None, None)
SEPT = Noeud('7', None, None)
SIX = Noeud('6', None, None)
DEUX = Noeud('2', None, None)
UN = Noeud('1', None, None)
TROIS = Noeud('3', None, None)
QUATRE = Noeud('4', None, None)
CINQ = Noeud('5', None, None)
C = Noeud('C', None, None)
Q = Noeud('Q', None, None)
Z = Noeud('Z', SEPT, None)
X = Noeud('X', None, None)
B = Noeud('B', SIX, None)
Y = Noeud('Y', None, None)
F = Noeud('F', None, None)
V = Noeud('V', None, TROIS)
H = Noeud('H', CINQ, QUATRE)
J = Noeud('J', None, UN)
P = Noeud('P', None, None)
L = Noeud('L', None, None)
O = Noeud('O', Noeud(None, HUIT, None), Noeud(None, NEUF, ZERO))
G = Noeud('G', Z, Q)
D = Noeud('D', B, X)
K = Noeud('K', C, Y)
U = Noeud('U', F, Noeud(None, None, DEUX))
S = Noeud('S', H, V)
W = Noeud('W', P, J)
R = Noeud('R', L, None)
M = Noeud('M', G, O)
N = Noeud('N', D, K)
I = Noeud('I', S, U)
A = Noeud('A', R, W)
E = Noeud('E', I, A)
T = Noeud('T', N, M)

MORSE = Noeud(None, E, T)



# Ecris tes fonctions ici !


radio.on() # Allumer la radio
radio.config(channel=42) # Configure le canal utilise (doit etre compris entre 0 et 83)

while False:
    message_recu = radio.receive() # Essaye de recevoir un message
    if message_recu != None:
        display.scroll(received_message) # Affiche le message recu s'il existe

    # Continue le code ici !




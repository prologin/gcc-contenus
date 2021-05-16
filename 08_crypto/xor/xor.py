#xor

import random

def stringToHexa(s):
    """
    Function that transforms a string
    into hexadecimal
    """
    res = ""
    l = len(s)
    for i in range(l):
        res += hex(ord(s[i]))[2:].zfill(2)
    return res

def msgXor(s, key, isEnc):
    """
    Function that applies the xor 
    operation of the message with a
    given key.
    """
    if isEnc:
        h = stringToHexa(s)
    else:
        h = s

    l = len(h)
    res = ""
    i = 0
    
    while i < l:
        tmp1 = h[i] + h[i+1]
        tmp2 = key[i] + key[i+1]
        i+=2
        res += hex(int(tmp1, 16)^int(tmp2, 16))[2:].zfill(2)
    return res

def hexaToString(hexa):
    l = len(hexa)
    i = 0
    res = ""
    while i < l :
        tmp = hexa[i] + hexa[i+1]
        i += 2
        res += chr(int(tmp, 16))
    return res

#test function
def randomHexa(lenstr):
    string = ""
    for i in range(lenstr):
        rdm_int = random.randint(0, 255)
        string += chr(rdm_int)
    res = stringToHexa(string)
    return res

#tests
s = "Hello World!"
h = randomHexa(len(s))
print("s = ",stringToHexa(s))
print("h = ", h)

tmp = msgXor(s, h, True)

print("t = ", tmp)

dec = msgXor(tmp, h, False)
print(dec)

clear = hexaToString(dec)
print(clear)
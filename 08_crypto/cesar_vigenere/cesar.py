#Caesar cipher
def letterCaesar(l, nb):
    """
    letterCaesar: function that applies Caesar's cipher
    on only one letter.
    """
    if l == " ":
        return l

    asc = ord(l)
    asc += nb
    if l <= 'Z' and l >= 'A':
        if asc > ord('Z'):
            asc = ord('A') + asc - ord('Z')-1
        if asc < ord('A'):
            asc = ord('Z') - (ord('A') - asc)+1
        return chr(asc)

    if l <= 'z' and l >= 'a':
        if asc > ord('z'):
            asc = ord('a') + asc - ord('z') -1
        if asc < ord('a'):
            asc = ord('z') - (ord('a') - asc) +1
        return chr(asc)
    
    raise ValueError("Error: value is not a letter")

def letterCaesarMod(l, nb):
    """
    letterCaesar: function that applies Caesar's cipher
    on only one letter.
    """
    if l == " ":
        return l

    asc = ord(l)
    asc += nb

    if l <= 'Z' and l >= 'A':
        if asc > ord('Z'):
            asc = ord('A') + asc % ord('Z')-1
        if asc < ord('A'):
            asc = ord('Z') - (ord('A') - asc) +1
        return chr(asc)

    if l <= 'z' and l >= 'a':
        if asc > ord('z'):
            asc = ord('a') + asc % ord('z')-1
        if asc < ord('a'):
            asc = ord('z') - (ord('a') - asc) +1
        return chr(asc)
    
    raise ValueError("Error: value is not a letter")


def wordCaesar(w, nb):
    """
    wordCaesar: function that applies Caesar's cipher
    on a whole word.

    Uses letterCaesar cipher.
    """
    l = len(w)
    res = ""

    for i in range(l):
        res += letterCaesar(w[i], nb)
    return res

def wordCaesarMod(w, nb):
    """
    wordCaesar: function that applies Caesar's cipher
    on a whole word.

    Uses letterCaesar cipher.
    """
    l = len(w)
    res = ""

    for i in range(l):
        res += letterCaesarMod(w[i], nb)
    return res

def breakCaesar(msg):
    for i in range(1, 27, 1):
        print(wordCaesar(msg, i))

#tests
breakCaesar("Rovvy Gybvn")


print(letterCaesar('a', 10))
print(wordCaesar("test", 1))
print(wordCaesar("Girls can code", 3))
print()
res = wordCaesar("Hello World", 10)
print(res)
res2 = wordCaesar(res, -10)
print(res2)
print()
print(wordCaesarMod("Girls can code", 3))
print()
res =wordCaesarMod("Hello World", 10)
print(res)
res2 = wordCaesarMod(res, -10)
print(res2)

#Caesar cipher while taking into account only capital letters

def charCaesarCap(c, d):
    """
    Function that applies Caesar cipher on one letter.
    """
    if c == " ":
        return c
    letter = c.upper()

    l = ord(letter) + d

    if letter >= 'A' and letter <= 'Z':
        if l > ord('Z'):
            l = ord('A') + l % ord('Z') -1
        if l < ord('A'):
            l = ord('Z') - (ord('A') - l) +1

    return chr(l)

def wordCaesarCap(w, nb):
    """
    wordCaesarCap: function that applies Caesar's cipher
    on a whole word.

    Uses letterCaesar cipher.
    """
    l = len(w)
    res = ""

    for i in range(l):
        res += charCaesarCap(w[i], nb)
    return res

print(charCaesarCap('a', 5))
print(charCaesarCap('e', -5))

res = wordCaesarCap("Hello World", 10)
print(res)
res2 = wordCaesarCap(res, -10)
print(res2)



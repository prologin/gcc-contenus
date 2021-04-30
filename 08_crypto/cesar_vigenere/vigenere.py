#Vigenère


def letterSubst(c, l):
    """
    letterCaesar: function that applies Caesar's cipher
    on only one letter.
    """
    nb = ord(l.upper()) - ord('A')
    if c == " ":
        return c

    asc = ord(c)
    asc += nb
    if c <= 'Z' and c >= 'A':
        if asc > ord('Z'):
            asc = ord('A') + asc - ord('Z') - 1
        if asc < ord('A'):
            asc = ord('Z') - (ord('A') - asc) + 1
        return chr(asc)

    if c <= 'z' and c >= 'a':
        if asc > ord('z'):
            asc = ord('a') + asc - ord('z') - 1
        if asc < ord('a'):
            asc = ord('z') - (ord('a') - asc) + 1
        return chr(asc)

    raise ValueError("Error: value is not a letter")


def letterSubstDec(c, l):
    """
    letterCaesar: function that applies Caesar's cipher
    on only one letter.
    """
    nb = -(ord(l.upper()) - ord('A'))
    if l == " ":
        return l
    asc = ord(c)
    asc += nb
    if c <= 'Z' and c >= 'A':
        if asc > ord('Z'):
            asc = ord('A') + asc - ord('Z') - 1
        if asc < ord('A'):
            asc = ord('Z') - (ord('A') - asc) + 1
        return chr(asc)

    if c <= 'z' and c >= 'a':
        if asc > ord('z'):
            asc = ord('a') + asc - ord('z') - 1
        if asc < ord('a'):
            asc = ord('z') - (ord('a') - asc) + 1
        return chr(asc)

    raise ValueError("Error: value is not a letter")


def wordVigenere(w, key, isEnc):
    """
    """
    l = len(w)
    res = ""
    j = 0
    l2 = len(key)
    for i in range(l):
        if isEnc:
            res += letterSubst(w[i], key[j])
        else:
            res += letterSubstDec(w[i], key[j])
        j += 1
        if j == l2:
            j = 0
    return res


res = wordVigenere("Programmation", "Linux", True)
print(res)
print(wordVigenere(res, "Linux", False))
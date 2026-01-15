alfabet = ["a", "ą", "b", "c", "ć", "d", "e", "ę", "f", "g",
           "h", "i", "j", "k", "l", "ł", "m", "n", "ń", "o",
           "ó", "p", "r", "s", "ś", "t", "u", "w", "y", "z",
           "ź", "ż"]

def szyfr_cezara(text, shift):
    szyfr = ""
    for znak in text.lower():
        if znak in alfabet:
            index = (alfabet.index(znak) + shift) % len(alfabet)
            szyfr = szyfr + alfabet[index]
        else:
            szyfr = szyfr + znak
    return szyfr

tekst = "Ala ma perę kotów"
print(szyfr_cezara(tekst, 3))
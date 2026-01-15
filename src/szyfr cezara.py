alfabet = ["a", "ą", "b", "c", "ć", "d", "e", "ę", "f", "g", "h", "i", "j", "k", "l", "ł", "m", "n", "ń", "o", "ó", "p", "r",
           "s", "ś", "t", "u", "w", "y", "z", "ź", "ż"]

def szyfr_cezara(text, shift):
    szyfr = []
    for znak in text:
        if znak.lower() in alfabet:
            litera = alfabet.index(znak.lower())
            nowa_litera = alfabet[(litera + shift) % len(alfabet)]
            if znak != znak.lower():
                szyfr.append(nowa_litera.upper())
            else:
                szyfr.append(nowa_litera)
        else:
            szyfr.append(znak)
    return "".join(szyfr)

 print("Niezaszyfrowany tekst:")
    tekst = str(input())
    print("Przesunięcie:")
    przesuniecie = int(input())
    print("Zaszyfrowany tekst:")
    print(szyfr_cezara(tekst, przesuniecie))
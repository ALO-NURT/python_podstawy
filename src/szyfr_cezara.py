def szyfr_cezara(text, shift):def szyfr_cezara(text, shift):
    alfabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u", "w", "y", "z"]
    szyfr = []
    for znak in text:
        if znak.lower() in alfabet:
            litera = alfabet.index(znak.lower())
            nowa_litera = alfabet[(litera + shift) % len(alfabet)]
            szyfr.append(nowa_litera)
        else:
            szyfr.append(znak)
    return "".join(szyfr)

print("Podaj tekst do zaszyfrowania:")
text = str(input())
print("Podaj przesunięcie liter w szyfrze:")
shift = int(input())
print("Zaszyfrowany tekst:")
print(szyfr_cezara(text, shift))

def szyfr_cezara(text, shift)
    for znak in text:


print("Podaj tekst do zaszyfrowania:")
text = str(input())
print("Podaj przesunięcie liter w szyfrze:")
shift = int(input())
print("Zaszyfrowany tekst:")
print(szyfr_cezara(text, shift))
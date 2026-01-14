from szyfr_cezara import szyfr_cezara
from lamacz_szyfrow import lamacz_szyfrow

def test_wszytskich_mozliwosci(tekst):
    for przesuniecie in range(31):
        szyfr = szyfr_cezara(tekst, przesuniecie)
        wynik = lamacz_szyfrow(szyfr)
        print(tekst == wynik, wynik)
    return ""

print("Podaj tekst do sprawdzenia:")
tekst_wejscie = str(input())
print(test_wszytskich_mozliwosci(tekst_wejscie))
from szyfr_cezara import szyfr_cezara
from analiza_czestosci import analiza_czestosci
import random
alfabet = [
    "a", "ą", "b", "c", "ć", "d", "e", "ę", "f", "g",
    "h", "i", "j", "k", "l", "ł", "m", "n", "ń", "o",
    "ó", "p", "r", "s", "ś", "t", "u", "w", "y", "z",
    "ź", "ż"
]
czestosc = [
    8.965, 1.021, 1.482, 3.988, 0.448, 3.293, 7.921, 1.131, 0.312, 1.377,
    1.072, 8.286, 2.343, 3.411, 2.136, 1.746, 2.911, 5.600, 0.185, 7.590,
    0.823, 3.101, 4.571, 4.263, 0.683, 3.966, 2.347, 4.549, 3.857, 5.620,
    0.061, 0.885
]
alfabet_czestosc = dict(zip(alfabet, czestosc))

def najczestsza_litera(slownik):
    return max(slownik, key=slownik.get)

def licz_przesuniecie(litera_szyfr, litera_pl, alfabet):
    i1 = alfabet.index(litera_szyfr)
    i2 = alfabet.index(litera_pl)
    return (i1 - i2) % len(alfabet)

tekst_1 = open("test_data.txt", encoding="utf-8").read()
przesuniecie_szyfr = random.randint(1, 29)
szyfr = szyfr_cezara(tekst_1, przesuniecie_szyfr)

szyfr_czestosc = dict(zip(alfabet, analiza_czestosci(szyfr)))

litera_pl = najczestsza_litera(alfabet_czestosc)
litera_tekst = najczestsza_litera(szyfr_czestosc)
przesuniecie = int(licz_przesuniecie(litera_tekst,litera_pl, alfabet))
tekst_2 = szyfr_cezara(szyfr, -przesuniecie)

print(przesuniecie == przesuniecie_szyfr)
print(tekst_2)
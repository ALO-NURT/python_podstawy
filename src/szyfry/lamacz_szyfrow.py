alfabet = ["a", "ą", "b", "c", "ć", "d", "e", "ę", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ń", "o", "ó", "p", "r",
           "s", "ś", "t", "u", "w", "y", "z", "ź", "ż"]
from szyfr_cezara import szyfr_cezara
from analiza_czestosci import analiza_czestosci

tekst_1 = open("test_data.txt", encoding="utf-8").read()
analiza = analiza_czestosci(szyfr)
print(analiza)
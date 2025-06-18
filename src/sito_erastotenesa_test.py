from src.faktoryzacja import liczba_pierwsza
from src.sito_erastotenesa import sito_erastotenesa
assert sito_erastotenesa(20) == [2, 3, 5, 7, 11, 13, 17, 19]

assert liczba_pierwsza(12) == False
liczby_pierwsze = sito_erastotenesa(1000)
for i in liczby_pierwsze:
    assert liczba_pierwsza(1)

print(sito_erastotenesa(1000))

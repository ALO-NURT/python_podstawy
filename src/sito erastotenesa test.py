from src.faktoryzacja import sito_erastotenesa, liczba_pierwsza

assert sito_erastotenesa(10) == [2,3,5,7]
assert sito_erastotenesa(20) == [2,3,5,7,11,13,17,19]

assert liczba_pierwsza(12) == False

liczby_pierwsze = sito_erastotenesa(100)
for i in liczby_pierwsze:
    assert liczba_pierwsza(i)


print(sito_erastotenesa(100))
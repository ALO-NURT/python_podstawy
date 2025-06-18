def sito_erastotenesa(n):
    if n < 2:
        return ([])
    lista = [True] * (n + 1)
    lista[0] = False
    lista [1] = False

    for indeks in range (2, int(n**0.5)+1):
        if lista[indeks]:
            for i in range (2*indeks, n+1, indeks):
                lista[i] = False
    return(lista)

from src.sito_erastotenesa import sito_erastotenesaassert
sito_erastotenesa(20) == [2, 3, 5, 7, 11, 13, 17, 19]

assert liczba pierwsza(13)
liczby_pierwsze = sito_erastotenesa(1000)
for i in liczby_pierwsze:
    assert liczby_pierwsze(i)
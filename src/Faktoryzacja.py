
from math import sqrt
def liczba_pierwsza(n):
    if n < 2 :
        return False
    for i in range(2, int(sqrt(n))+1):
       if n % i == 0:
           return False
    return True
print(liczba_pierwsza(25))



# lekcja 11.06 sito erastotenesa

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

print(sito_erastotenesa(10))
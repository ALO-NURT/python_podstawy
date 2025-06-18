#lekcja 21/05/2025

from math import sqrt
def liczba_pierwsza(n):
    if n < 2 :
        return False
    for i in range(2 , int(sqrt(n))+1): #pierwiastek
        if n % i == 0:
            return False
    return True
print(liczba_pierwsza(25))

#lekcja 28/05/2025
#lecka 11/06/2025 sito-Erastotenesa
def sito_erastotenesa(n):
    lista = [True] * (n + 1)
    lista[0] = False
    lista[1] = False
    indeks = 2
    for indeks in range (2 ,int(n**0.5)+1):
        if lista [indeks]:
            for i in range(2*indeks , n+1 , indeks):
                lista [i] = False
    wynik= []
    for i in range (n+1):
        if lista[i]:
            wynik.append(i)
    return wynik

print(sito_erastotenesa(738))
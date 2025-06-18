## 21.05
from math import sqrt


def liczba_pierwsza (n):
    for i in range(2 , int(sqrt(n))+1):
        if n % i == 0:
            return False
        return True

liczba = 193
if liczba_pierwsza(liczba):
    print(f"{liczba} jest liczbą pierwszą")
else:
    print(f"{liczba} nie jest liczbą pierwszą")

#28.05
def sito_erastotenesa(n):
    lista = [True]*(n + 1)
    lista[0] = False
    lista [1] = False
    for indeks in range (2,int(n**0.5)+1):
        if lista [indeks]:
            for i in range (2*indeks , n+1 , indeks):
                lista [i] = False
    wynik= []
    for i in range (n+1):
        if lista[i]:
            wynik.append(i)
    return wynik

print(sito_erastotenesa(400))



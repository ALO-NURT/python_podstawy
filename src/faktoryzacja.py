from math import sqrt

n = 25
def liczba_pierwsza (n):
    if n<2:
        return False
    for i in range (2, int(sqrt(n)) + 1):
        if n%i == 0:
            return False
    return True
print(liczba_pierwsza(n))


wynik = 0
for liczba in range(10):
    if liczba % 2 == 0:
        wynik = wynik + liczba
    else:
        wynik = wynik - liczba
print(wynik)

# sito erastotenesa ---> zawsze zaczyna od dwójki i dodaje kolejne liczby

[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

def sito_erastotenesa(n):
    if n<2:
        return ([])
    lista = [True]*(n+1)
    lista[0] = False
    lista[1] = False
    for indeks in range (2,int(n**0.5)+1):
        if lista[indeks]:
            for i in range(2*indeks,n+1,indeks):
                lista[i]=False
    wynik=[]
    for i in range (n+1):
        if lista[i]:
            wynik.append(i)
    return(wynik)
print(sito_erastotenesa(20))

from src.sito_erastotenesa import sito_erastotenesaassert
sito_erastotenesa(20) == [2, 3, 5, 7, 11, 13, 17, 19]

#sprawdzamy czy nic nam nie podkreśla na czerwono


def liczba_pierwsza (n):
    if n<2:
        return False
    for i in range(2,int (sqrt(n))+1):
        if n % i == 0:
            return False
    return True

for liczba in range (0,1000):
    print(f"Liczba {liczba} jest pierwsza? -> {liczba_pierwsza(liczba)}")


def sito_erastotenesa (n):
    if n<2:
        return[ ]
    lista= [True]*n
    print(lista)
    sito_erastotenesa(2)
while indeks i range (2,int (n**0.5) + 1):
    if lista [indeks]:
        for i in (2* indeks, n+1, indeks):
            lista [i]= False
    return (lista):
    lista[i]=False
    wynik= [ ]


def liczba_pierwsza (n):
    if n < 2:
        return False
    for i in range (2,0):
        if n % i == 0:
            return False
    return True

# for liczba in range(0, 1000000):
#     print(f"Liczba {liczba} jest pierwsza? -> {liczba_pierwsza(liczba)}")




# sito erastotenesa --> zawsze zaczyna od dwójki i dodaje kolejne liczby

[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


def sito_erastotenesa(n):
    if n<2:
        return ([])
    lista = [True]*(n+1)
    lista[0]= False
    lista[1] = False
    indeks = 2
    for indeks in range (2, int(n**0.5)+1):
        if lista [indeks]:
            for i in range(2*indeks,n+1,indeks):
                lista[i]=False
    wynik = []
    for i in range (n+1):
        if lista[i]:
            wynik.append(i)
    return(wynik)

print(sito_erastotenesa(10))

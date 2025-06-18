def sito_erastotelesa(n):
    lista = [True]*(n + 1)
    lista[0] = False
    lista [1] = False    indeks = 2
    for indeks in range  (2,int(n**0.5)+1):
        if lista [indeks]:
            for i in range (2*indeks, n+1, indeks):
                lista [i] = False
            wynik = []
                for i in range (n+1):
                    if lista [i]:
                        wynik.append(i)
return wynikprint(sito_erastotelesa(10))
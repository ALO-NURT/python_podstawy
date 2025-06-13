def sito_erastotenesa (n)
    if n<2
        return()
    lista = [True]*(n+1)
    lista[0] = False
    lista[1] = False
    wynik = []
    for indeks in range (2, int(n**0.5)+1)
        if lista[indeks]
            wynik.append(indeks)
            for i in range(indeks, n+1, indeks)
                lista[i] = False
    return wynik
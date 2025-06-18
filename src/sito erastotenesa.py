def sito_erastotenesa(n):
    lista = [True] * (n + 1)
    lista[0] = False
    lista[1] = False
    for indeks in range(2, int(n ** 0.5) + 1):
        if lista[indeks]:
            for i in range(2 * indeks, n + 1, indeks):
                lista[i] = False
    return(lista)
    wynik = []
    for i in range(n + 1):
        if lista[1]:
            wynik.append(i)
    return wynik
print(sito_erastotenesa(10))
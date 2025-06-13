def sito_erastotenesa(n):
    if n<2:
        return []
    lista = [True]*(n+1)
    lista[0] = False
    lista[1] = False
    wynik = []
    for indeks in range(2, n+1):
        if lista[indeks]:
            wynik.append(indeks)
            for i in range(indeks, n+1, indeks):
                lista[i] = False
    return wynik

print("Podaj liczbę:")
n = int(input())
print(sito_erastotenesa(n))
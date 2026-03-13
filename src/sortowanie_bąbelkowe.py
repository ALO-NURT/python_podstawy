def sortowanie_babelkowe(lista):
    n = len(lista)
    sorted = False
    while not sorted:
        sorted = True
        for j in range(n - 1):
            if lista[j] > lista[j + 1]:
                pamiec_podreczna = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = pamiec_podreczna
                sorted = False
    return lista

if __name__ == "__main__":
    print("Liczby do posortowania (odzdzielone przecinkiem):")
    dane = str(input())
    print("Posortowane liczby:")
    print(sortowanie_babelkowe(utworz_liste_wejsciowa(dane)))
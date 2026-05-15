def zadanie_1(lista):
    liczby_ujemne = 0
    najmniejsza_liczba_nieparzysta = None
    liczby_nieparzyste = 0
    najmniejsza = lista[0]
    najwieksza = lista[0]

    wynik = []

    for i in range(len(lista)):
        if lista[i] < 0:
            liczby_ujemne += 1

    # Ten element zadania 1 v2 musiałem dokończyć w domu, bo nie zdążyłem pod koniec lekcji
        if lista[i] % 2 == 1:
            liczby_nieparzyste += 1
            if najmniejsza_liczba_nieparzysta is None or lista[i] < najmniejsza_liczba_nieparzysta:
                najmniejsza_liczba_nieparzysta = lista[i]

    # Ten też
        if lista[i] < najmniejsza:
            najmniejsza = lista[i]
        if lista[i] > najwieksza:
            najwieksza = lista[i]

    wynik.append(liczby_ujemne)
    if liczby_nieparzyste != 0:
        wynik.append(najmniejsza_liczba_nieparzysta)
    elif liczby_nieparzyste == 0:
        wynik.append("Nie ma liczb nieparzystych")
    suma_skrajnych = najmniejsza + najwieksza
    wynik.append(suma_skrajnych)

    return wynik


if __name__ == "__main__":
    print("Podaj liczby całkowite oddzielone przecinkiem i spacją:")
    wejscie = (str(input())).split(", ")
    for j in range(len(wejscie)):
        wejscie[j] = int(wejscie[j])

    rezultat = zadanie_1(wejscie)
    print("Ilość liczb ujemnych:")
    print(rezultat[0])
    print("Najmniejsza liczba nieparzysta:")
    print(rezultat[1])
    print("Suma najmniejszej i największej liczby:")
    print(rezultat[2])



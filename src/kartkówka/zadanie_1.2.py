def zadanie_1(lista):
    liczby_ujemne = 0
    najmniejsza_liczba_nieparzysta = lista[0]
    liczby_nieparzyste = 0
    wynik = []
    for i in range(len(lista)):
        if lista[i] < 0:
            liczby_ujemne += 1
        if lista[i] < najmniejsza_liczba_nieparzysta and lista[i] % 2 == 1:
            najmniejsza_liczba_nieparzysta = lista[i]
        if lista[i] % 2 == 1:
            liczby_nieparzyste += 1

    wynik.append(liczby_ujemne)
    if liczby_nieparzyste != 0:
        wynik.append(najmniejsza_liczba_nieparzysta)
    if liczby_nieparzyste == 0:
        wynik.append("Nie ma liczb nieparzystych")
    return wynik


if __name__ == "__main__":
    print("Podaj liczby całkowite oddzielone przecinkiem i spacją:")
    wejscie = (str(input())).split(", ")
    for j in range(len(wejscie)):
        wejscie[j] = int(wejscie[j])

    print("Ilość liczb ujemnych:")
    print(zadanie_1(wejscie)[0])

    print("Najmniejsza liczba nieparzysta:")
    print(zadanie_1(wejscie)[1])
    print(zadanie_1(wejscie)[2])


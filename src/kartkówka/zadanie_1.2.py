def zadanie_1(lista):
    liczby_ujemne = 0
    najmniejsza_liczba_nieparzysta = lista[0]
    wynik = []
    for i in range(len(lista)):
        if lista[i] < 0:
            liczby_ujemne += 1
        if lista[i] < najmniejsza_liczba_nieparzysta and lista[i] % 2 == 1:
            najmniejsza_liczba_nieparzysta = lista[i]

    wynik.append(liczby_ujemne)
    wynik.append(najmniejsza_liczba_nieparzysta)
    return wynik

def liczby_nieparzyste(lista):
    liczby_nieparzyste = 0
    for m in range(len(lista)):
        if lista[m] % 2 == 1:
            liczby_nieparzyste =+ 1
    if liczby_nieparzyste == 0:
        return "Nie ma liczb nieparzystych"
    else:
        return

if __name__ == "__main__":
    print("Podaj liczby całkowite oddzielone przecinkiem i spacją:")
    wejscie = (str(input())).split(", ")
    for j in range(len(wejscie)):
        wejscie[j] = int(wejscie[j])

    print("Ilość liczb ujemnych:")
    print(zadanie_1(wejscie)[0])

    print("Najmniejsza liczba nieparzysta:")
    print(zadanie_1(wejscie)[1])
    print(liczby_nieparzyste(wejscie))


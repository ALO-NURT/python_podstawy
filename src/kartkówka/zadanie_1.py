def liczby_ujemne(lista):
    liczby_ujemne = 0
    for i in range(len(lista)):
        if lista[i] < 0:
            liczby_ujemne += 1
    return liczby_ujemne

def najmniejsza_liczba_nieparzysta(lista):
    liczba = lista[0]
    for i in range(len(lista)):
        if lista[i] < liczba and lista[i] % 2 == 1:
            liczba = lista[i]
    return liczba

def liczby_nieparzyste(lista):
    liczby_nieparzyste = 0
    for m in range(len(lista)):
        if lista[m] % 2 == 1:
            liczby_nieparzyste =+ 1
    if liczby_nieparzyste == 0:
        return "Nie ma liczb nieparzystych"

if __name__ == "__main__":
    print("Podaj liczby całkowite oddzielone przecinkiem i spacją:")
    wejscie = (str(input())).split(", ")
    for j in range(len(wejscie)):
        wejscie[j] = int(wejscie[j])

    print("Ilość liczb ujemnych:")
    print(liczby_ujemne(wejscie))

    print("Najmniejsza liczba nieparzysta:")
    print(najmniejsza_liczba_nieparzysta(wejscie))
    print(liczby_nieparzyste(wejscie))


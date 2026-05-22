def analiza_czestosci(tekst, dlugosc):
    lista_wejsciowa = tekst.split(" ")
    nowa_lista = []
    czestosc = []

    for slowo in lista_wejsciowa:
        if len(slowo) == dlugosc:
            nowa_lista.append(slowo)

    for i in nowa_lista:
        czestosc.append([i, nowa_lista.count(i)])

    for j in czestosc:
        #i tak dalej

    return czestosc

if __name__ == "__main__":
    print("Podaj tekst:")
    wejscie_1 = str(input())
    print("Długość słowa:")
    wejscie_2 = int(input())

    print(f"Wynik{analiza_czestosci(wejscie_1, wejscie_2)}")
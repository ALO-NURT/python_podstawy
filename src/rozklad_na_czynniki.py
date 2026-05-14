def faktoryzacja(liczba_do_rozkladu):
    rozklad = []
    czynnik = 2
    while liczba_do_rozkladu != 1:
        if liczba_do_rozkladu % czynnik == 0:
            liczba_do_rozkladu = liczba_do_rozkladu // czynnik
            rozklad.append(czynnik)
        else:
            czynnik += 1

    return rozklad

if __name__ == "__main__":
    print("Podaj liczbę do rozkładu na czynniki pierwsze:")
    liczba = int(input())
    print("Rozkład na czynniki pierwsze:")
    wynik = faktoryzacja(liczba)
    print(*wynik, sep=", ")

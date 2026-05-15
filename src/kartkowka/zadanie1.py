def liczenie_dodatnich():
    liczby = [int(x) for x in input("Podaj liczby oddzielone spacją: ").split()]
    ile_dodatnich = 0

    for liczba in liczby:
        if liczba > 0:
            ile_dodatnich += 1

    print("Liczb dodatnich:", ile_dodatnich)


liczenie_dodatnich()


def najwieksza_parzysta():
    liczby = [int(x) for x in input("Podaj liczby oddzielone spacją: ").split()]

    max_parzysta = None

    for liczba in liczby:
        if liczba % 2 == 0:
            if max_parzysta is None or liczba > max_parzysta:
                max_parzysta = liczba

    if max_parzysta is not None:
        print("Największa liczba parzysta:", max_parzysta)
    else:
        print("Brak liczb parzystych")


najwieksza_parzysta()

def najmniejsza_parzysta():
    liczby = [int(x) for x in input("Podaj liczby oddzielone spacją: ").split()]

    min_parzysta = None

    for liczba in liczby:
        if liczba % 2 == 0:
            if min_parzysta is None or liczba < min_parzysta:
                min_parzysta = liczba

    if min_parzysta is not None:
        print("Najmniejsza liczba parzysta:", min_parzysta)
    else:
        print("Brak liczb parzystych")


najmniejsza_parzysta()

def różnica_parzystych():
    najmniejsza = najmniejsza_parzysta()
    największa = najwieksza_parzysta()

    if najmniejsza is not None and największa is not None:
        wynik = największa - najmniejsza
        print("Różnica jest równa", wynik)
    else:
        print("Brak liczb parzystych")

różnica_parzystych()
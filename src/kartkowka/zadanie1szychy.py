def analiza_liczb(analiza_liczb) -> None:
    if len(analiza_liczb) == 0:
        print("Brak danych")
        return

    ilość_dodatnich = 0
    największa_parzysta = None
    największa_liczba = lista_liczb[0]
    najmniejsza_liczba = lista_liczb[0]

    for liczba in lista_liczb:
        if liczba > 0:
            ilość_dodatnich += 1
        if liczba % 2 == 0:
            if największa_parzysta is None or liczba > największa_parzysta:
                największa_parzysta = liczba
            if liczba > największa_liczba:
                największa_liczba = liczba
            if liczba < najmniejsza_liczba:
                najmniejsza_liczba = liczba

    print(f"ilość liczb dodatnich: {ilość_dodatnich}")
    print(f"Największa parzysta: {największa_liczba if not największa_liczba is None else'brak'}")
    print(f"Różnica między największą a najmniejszą liczbą: {największa_liczba - najmniejsza_liczba}")


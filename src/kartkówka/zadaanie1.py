def zadanie1(lista_liczb):
    dodatnie = 0
    ujemne = 0
    najmniejsze_nieparzyste = None
    najwieksza_parzysta = None
    najmniejsza = lista_liczb[0]
    najwieksza = lista_liczb[0]
    for liczba in lista_liczb:
        if liczba < najmniejsza:
            najmniejsza = liczba
        if liczba > najwieksza:
            najwieksza = liczba
        if liczba < 0:
            ujemne += 1
        if liczba % 2 == 1:
            if najmniejsze_nieparzyste is None or liczba < najmniejsze_nieparzyste:
                najmniejsze_nieparzyste = liczba
        if liczba > 0:
            dodatnie += 1
        if liczba % 2 == 0:
            if najwieksza_parzysta is None or liczba > najwieksza_parzysta:
                najwieksza_parzysta = liczba
    roznica = najwieksza - najmniejsza

    print(f"Dodatnich: {dodatnie}")
    print(f"Największa parzysta: {najwieksza_parzysta}")
    print(f"Różnica: {roznica}")
    print(f"Ujemnych: {ujemne}")
    print(f"Najmniejsza nieparzysta: {najmniejsze_nieparzyste}")
lista = [-8, 7, 3, -3, 2, 16, 9, -10, 5, 7, 17]
zadanie1(lista)

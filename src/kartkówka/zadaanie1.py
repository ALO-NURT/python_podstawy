def zadanie1(lista_liczb):
    dodatnie = 0
    najwieksza_parzysta = None
    najmniejsza = lista_liczb[0]
    najwieksza = lista_liczb[0]
    for liczba in lista_liczb:
        if liczba < najmniejsza:
            najmniejsza = liczba
        if liczba > najwieksza:
            najwieksza = liczba
        if liczba > 0:
            dodatnie += 1
            if najwieksza_parzysta is None or liczba > najwieksza_parzysta:
                najwieksza_parzysta = liczba
    roznica = najwieksza - najmniejsza

    print(f"Liczba parzystych: {dodatnie}")
    print(f"Największa parzysta: {najwieksza_parzysta}")
    print(f"Różnica między największą a najmniejszą: {roznica}")

lista = [2, 7, -3, 10, 5, 8, 1, -6]
zadanie1(lista)

def analiza_liczb(lista_liczb):
    ilosc_liczb_dodatnich = 0
    najwieksza_parzysta = None
    najwieksza_liczba = lista_liczb[0]
    najmniejsza_liczba = lista_liczb[0]
    for i in lista_liczb:
        if i > 0:
            ilosc_liczb_dodatnich += 1
        if i % 2 == 0:
            if najwieksza_parzysta is None or i > najwieksza_parzysta:
                najwieksza_parzysta = i
        if i > najwieksza_liczba:
            najwieksza_liczba = i
        if i < najmniejsza_liczba:
            najmniejsza_liczba = i
    print(f"Ilość liczb dodatnich:{ilosc_liczb_dodatnich}")
    print(f"Największa parzysta:{najwieksza_parzysta}")
    print(f"Różnica między największą a najmniejszą liczbą:{najwieksza_liczba - najmniejsza_liczba}")
print (analiza_liczb([1,2,3,5,6,7,8,9]))
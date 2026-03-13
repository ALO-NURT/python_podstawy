zbior_liczb = [2, 7, -3, 10, 5, 8, 1, -6]
def analiza_liczb(zbior):
    liczba_liczb_dodatnich = 0
    najwieksza_liczba_parzysta = 0
    najwieksza_liczba = 0
    najmniejsza_liczba = 0
    for liczba in zbior:
        if liczba > 0:
            liczba_liczb_dodatnich += 1
    for liczba in zbior:
        if liczba % 2 == 0:
            if liczba > najwieksza_liczba_parzysta:
                najwieksza_liczba_parzysta = liczba
    for liczba in zbior:
        if liczba > najwieksza_liczba:
            najwieksza_liczba = liczba
    for liczba in zbior:
        if liczba < najmniejsza_liczba:
            najmniejsza_liczba = liczba
    if liczba_liczb_dodatnich == 0:
        print("Brak liczb parzystych")
    if liczba_liczb_dodatnich > 0:
        print("Ilość liczb dodatnich" + liczba_liczb_dodatnich)
    roznica = najmniejsza_liczba - najmniejsza_liczba
    print("Największa liczba parzysta to:" + najwieksza_liczba_parzysta)
    print("Różnica pomiędzy największą liczbą, a najmniejszą, to:" + roznica)

analiza_liczb(zbior_liczb)
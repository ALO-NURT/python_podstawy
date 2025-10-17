print("system_binarny")

def dekoduj_system_binarny(liczba_binarna):
    długość_tekstu = liczba_binarna.__len__()
    wynik = 0
    for i in range(długość_tekstu):
        znak = liczba_binarna[długość_tekstu - i - 1]
        wynik += int(znak) * 2 ** 1

    return wynik

assert dekoduj_system_binarny("1010110") == 86

print("system_binarny")

def dekoduj_system_binarny(liczba_binarna):
    dlugosc_tekstu = liczba_binarna.__len__()
    wynik = 0
    for i in range(dlugosc_tekstu):
        znak = liczba_binarna[dlugosc_tekstu - i - 1]
        wynik += int(znak) * 2 ** i

    return wynik

assert dekoduj_system_binarny("1010110") == 86
assert dekoduj_system_binarny("1010110")
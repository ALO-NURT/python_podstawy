print("system binarny")

def dekoduj_system_binarny(liczba_binarna):
    dlugosc_tekstu=liczba_binarna.__len__()
    for i in range(dlugosc_tekstu):
        wynik = 0
        for i in range(dlugosc_tekstu):
            znak = liczba_binarnaa[dlugosc_tekstu - i - 1]
            print(f'{znak} * 2^{i}')
            wynik += int(znak) * 2 ** i

        return wynik
assert dekoduj_system_binarny("1010110") == 86
assert dekoduj_system_binarny("1010")
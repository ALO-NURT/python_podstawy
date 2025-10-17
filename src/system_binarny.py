print("system_binarny")

def dekoduj_system_binarny(liczba_binarna):
    dlugosc_tekstu = liczba_binarna. __len__()
    wynik = 0
    i = 0
    for znak in liczba_binarna:
        wynik += int(znak) * 2 ** (dlugosc_tekstu - i)
        i += 1
    print(wynik)

dekoduj_system_binarny('10000')
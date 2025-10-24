print("system binarny")
def dekoduj_system_binarny(liczba_binarna):
    dlugosc_tekstu = liczba_binarna.__len__()
    wynik = 0
    for i in range(dlugosc_tekstu):
        znak = liczba_binarna[dlugosc_tekstu - i - 1]
        wynik += int(znak) * 2 ** i

    return wynik


def zamien_na_system_binarny(liczba):
    temp = int(liczba)
    liczba_binarna = ""
    while temp > 0:
        remainder = temp % 2
        temp //= 2
        liczba_binarna = str(remainder) + liczba_binarna

    return liczba_binarna

    #print(dekoduj_system_binarny("1010110"))
    #print(dekoduj_system_binarny("111001"))

    print(zamien_na_system_binarny(92))

    liczba_testowa = 1345673224589

    binarna = zamien_na_system_binarny(liczba_testowa)
    dziesietna = dekoduj_system_binarny(binarna)

    print(f'liczba_binarna: {binarna}, dziesietna: {dziesietna}')
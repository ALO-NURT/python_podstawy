print("system_binarny")

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


print(zamien_na_system_binarny(73))
liczba_testowa = 121

binarna = zamien_na_system_binarny(liczba_testowa)
dziesietna = dekoduj_system_binarny(binarna)

print(f'liczba binarna: {binarna}, liczba dziesietna: {dziesietna}')

def zamien_na_system_binarny(liczba , podstawa = 2):
    temp = int(liczba)
    wynik = ""
    while temp > 0:
        remainder = temp % podstawa
        temp = temp // podstawa
        wynik =str = str(remainder) + wynik
    return wynik





#print(dekoduj_system_binarny("111001"))
#print(dekoduj_system_binarny("1010"))



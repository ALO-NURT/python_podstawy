print("Liczba w systemie binarnym (a):")
a = str(input())

def dekoduj_system_binarny(liczba_binarna):
    dlugosc_tekstu = liczba_binarna.__len__()
    wynik = 0
    for i in range(dlugosc_tekstu):
        znak = liczba_binarna[dlugosc_tekstu - i - 1]
        wynik += int(znak) * 2 ** i

    return wynik

print("Liczba w systemie dziesiętnym:")
print(dekoduj_system_binarny(a))
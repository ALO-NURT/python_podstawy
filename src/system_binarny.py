def dekoduj_system_binarny(liczba_binarna):
    dlugosc_tekstu = liczba_binarna.__len__()
    wynik = 0
    for i in range(dlugosc_tekstu):
        znak = liczba_binarna[dlugosc_tekstu - i - 1]
        wynik += int(znak) * 2 ** i

    return wynik

def zamień_na_system_binarny(liczba):
    temp = int(liczba)
    liczba_binarna = ""
    while temp > 0:
        reminder = temp % 2
        temp //= 2
        liczba_binarna = str(reminder) + liczba_binarna

    return liczba_binarna

print("Liczba w systemie binarnym (a):")
a = str(input())
print("Liczba w systemie dziesiętnym:")
print(dekoduj_system_binarny(a))

print("Liczba w systemie dziesiętnym: (b):")
b = str(input())
print("Liczba w systemie binarny")
print(zamień_na_system_binarny(b))

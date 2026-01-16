print("system_binarny")

def dekoduj_system_binarny(liczba_binarna):
    dlugosc_tekstu = liczba_binarna.__len__()
    wynik = 0
    for i in range(dlugosc_tekstu):
        znak = liczba_binarna[dlugosc_tekstu - i - 1]
        wynik +=int(znak) *  2 ** i

    return wynik

assert dekoduj_system_binarny("1010110") == 86
assert dekoduj_system_binarny("1010") == 10

print(dekoduj_system_binarny("1010110"))
print(dekoduj_system_binarny("111001"))

#temp - zmienna

def zamień_na_system_binarny(liczba):
    temp = int(liczba)
    liczba_binarna = ""
    while temp > 0:  #<- pętla
        reminder = temp % 2 #<- % modulo, dla zmiennej zapisujemy reszta dzielenia przez 2
        temp //= 2
        liczba_binarna = str(reminder) + liczba_binarna

    return liczba_binarna

print(zamień_na_system_binarny(92))
liczba_tekstowa = 9239588

binarna = zamień_na_system_binarny(liczba_tekstowa)
dziesietna = dekoduj_system_binarny(binarna)

print(f'liczba binarna: {binarna}, liczba dziesietna{dziesietna}')

#lekcja 31.10.2025 - zamiana z systemu binarnego na system ósemkowy
def zamien_na_system(liczba , podstawa = 2):
    temp = int(liczba)
    wynik = ""
    while temp > 0:
        reminder = temp % podstawa
        temp = temp // podstawa
        wynik = str = str(reminer) + wynik
    return wynik
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


#zadanie domowe

def dziesietny_na_binarny(liczba):
    return bin(liczba)[2:]  # usuwa "0b" z przodu

def binarny_na_dziesietny(liczba_binarna):
    return int(liczba_binarna, 2)

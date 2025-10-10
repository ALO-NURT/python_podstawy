print("system binarny")
def dekoduj_system_binarny(liczba):
    wynik=0
    for i in range(liczba.__len__()):
        if liczba[-i-1] == "1":
            wynik += 1 * (2 ** (liczba.__len__() - i))
    return wynik

print(dekoduj_system_binarny("1010"))

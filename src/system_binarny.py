print("system_binarny")

def dekoduj_system_binarny(liczba):
    wynik = 0
    print(liczba.__len__())
    for i in range(liczba.__len__()):
        if liczba(liczba.__len__() - i - 1) == "1":
            wynik += 2 * (2 ** liczba.__len__() - i)
    

print(dekoduj_system_binarny("1010"))

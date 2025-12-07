import math

def natezenie_dzwieku(poziom_natezenia):
    B = 10 ** (0.1 * poziom_natezenia - 12)
    return B

def dzialanie(znak_dzialania, poziom_natezenia_1, poziom_natezenia_2):
    if znak_dzialania == "+":
        wynik_posredni = natezenie_dzwieku(poziom_natezenia_1) + natezenie_dzwieku(poziom_natezenia_2)
    elif znak_dzialania == "-":
        wynik_posredni = natezenie_dzwieku(poziom_natezenia_1) - natezenie_dzwieku(poziom_natezenia_2)
    wynik = 10 * math.log10(wynik_posredni / (10 ** (-12)))
    return round(wynik, 5)

def program():
    print("KALKULATOR POZIOMU NATĘŻENIA DŹWIĘKU")
    znak_dzialania = str(input("Podaj operator działania (+/-): "))
    poziom_natezenia_1 = int(input("Podaj wartość poziomu natężenia pierwszego dźwięku: "))
    poziom_natezenia_2 = int(input("Podaj wartość poziomu natężenia drugiego dźwięku: "))
    print("Wynik: ", dzialanie(znak_dzialania, poziom_natezenia_1, poziom_natezenia_2))

while True:
    program()
    uruchamianie = input("Czy chcesz uruchomić program ponownie? (tak/nie):").lower()

    if uruchamianie != "tak":
        print("Zamykanie programu...")
        break
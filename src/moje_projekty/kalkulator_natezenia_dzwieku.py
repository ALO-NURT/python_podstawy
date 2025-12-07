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
    return wynik


print("KALKULATOR POZIOMU NATĘŻENIA DŹWIĘKU")
print("Podaj operator działania (+/-):")
znak_dzialania = str(input())
print("Podaj wartość poziomu natężenia pierwszego dźwięku:")
poziom_natezenia_1 = int(input())
print("Podaj wartość poziomu natężenia drugiego dźwięku:")
poziom_natezenia_2 = int(input())
print("Wynik:")
print(dzialanie(znak_dzialania, poziom_natezenia_1, poziom_natezenia_2))
def nwd(a, b):
    while b != 0:
        reszta = a % b
        a = b
        b = reszta
    return a
def nww(a, b):
    iloczyn = a * b
    dzielnik = nwd(a, b)
    wynik = abs(iloczyn) // dzielnik
    return wynik

print("Podaj dwie liczby całkowite:")

pierwsza_liczba = int(input("Pierwsza liczba: "))
druga_liczba = int(input("Druga liczba: "))

wynik_nwd = nwd(pierwsza_liczba, druga_liczba)
wynik_nww = nww(pierwsza_liczba, druga_liczba)

print("Największy wspólny dzielnik (NWD) to:", wynik_nwd)
print("Najmniejsza wspólna wielokrotność (NWW) to:", wynik_nww)
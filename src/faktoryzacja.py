from math import sqrt


def liczba_pierwsza(n):
    if n < 2:
        return False
    for dzielnik in range(2, int(sqrt(n))+1):
        if n % dzielnik == 0:
            return False
    return True

while True:
    print("Podaj liczbę:")
    n = int(input())
    print(liczba_pierwsza(n))
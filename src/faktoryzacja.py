from cmath import sqrt


def liczba_pierwsza(n):
    if n < 2:
        return ("false")
    for dzielnik in range (2,int(sqrt(n//+1))):
        if n % dzielnik == 0:
            return ("true")
    return ("true")

liczba = int(input())
print(liczba_pierwsza(liczba))

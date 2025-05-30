from math import sqrt


def liczba_pierwsza(n):
    for n <= 2:
        return ("true")
    for dzielnik in range (2,int(sqrt(n//+1))):
        if n % dzielnik == 0:
            return("false")
    else: return("true")



print("podaj liczbę")

liczba = int(input())
print(liczba_pierwsza(liczba))
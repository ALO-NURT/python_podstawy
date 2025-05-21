## 21.05
from math import sqrt


def liczba_pierwsza (n):
    for i in range(2 , int(sqrt(n))):
        if n % i == 0:
            return False
        return True

liczba = 193
if liczba_pierwsza(liczba):
    print(f"{liczba} jest liczbą pierwszą")
else:
    print(f"{liczba} nie jest liczbą pierwszą")

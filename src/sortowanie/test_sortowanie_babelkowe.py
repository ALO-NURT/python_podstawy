import random
from sortowanie_babelkowe import sortowanie_babelkowe

losowe_liczby = []
for i in range(1000):
    nowa_liczba = random.randint(0, 1000)
    losowe_liczby.append(nowa_liczba)

liczby_posortowane = sortowanie_babelkowe(losowe_liczby)
liczby_posortowane_automatycznie = sorted(losowe_liczby)
print(liczby_posortowane)
print (liczby_posortowane == liczby_posortowane_automatycznie)
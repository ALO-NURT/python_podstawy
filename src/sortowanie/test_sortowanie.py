import random
from sortowanie import sortowanie

losowe_liczby = []
for i in range(10000):
    nowa_liczba = random.randint(0, 1000000)
    losowe_liczby.append(nowa_liczba)

liczby_posortowane = sortowanie(losowe_liczby)
liczby_posortowane_automatycznie = sorted(losowe_liczby)
print(liczby_posortowane)
print (liczby_posortowane == liczby_posortowane_automatycznie)
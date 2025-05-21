
from math import sqrt
def liczba_pierwsza(n):
    if n < 2 :
        return False
   for i in range(2, int(sqrt(n))):
       if n % i == 0:
           return False
   return True
print(liczba_pierwsza(15))

from math import sqrt

n = 25
def liczba_pierwsza (n):
    if n<2:
        return False
    for i in range (2, int(sqrt(n)) + 1):
        if n%i == 0:
            return False
    return True
print(liczba_pierwsza(n))


wynik = 0
for liczba in range(10):
    if liczba % 2 == 0:
        wynik = wynik + liczba
    else:
        wynik = wynik - liczba
print(wynik)

# sito erastotenesa ---> zawsze zaczyna od dwójki i dodsje kolejne liczby

[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

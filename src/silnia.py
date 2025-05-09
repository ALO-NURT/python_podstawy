def silnia(n):
    wynik = 1
    i = 1

    while i <= n:
        wynik = wynik * i
        i = i + 1
    return wynik

print(silnia(10))

def silnia(n):
    if n == 1:
        return 1
    else:
        return n * silnia(n-1)
print(silnia(5))

def silnia_rekurencja(n):
    return 1 if n == 1 else n * silnia_rekurencja(n-1)
print(silnia_rekurencja(3))


def silnia_pętla(n):
    wynik=1
    for i in range(1, n+1):
        wynik *= i
    return wynik
print(silnia_pętla(4))

def silnia_rekurencja(n):
    return 1 if n == 1 else n * silnia_rekurencja(n - 1)

def silnia_petla(n):
    wynik = 1
    for i in range(1, n+1):
        wynik *= i
    return wynik

print(silnia_rekurencja(10))
print(silnia_petla(10))
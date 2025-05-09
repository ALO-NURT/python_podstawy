def silnia_pętla(n):
    x_p = 1
    wynik_p = 1
    while(x_p <= n):
        wynik_p = wynik_p * x_p
        x_p = x_p + 1

    return wynik_p

def silnia_rek(n):
    return 1 if n == 1 else n * silnia_rek(n - 1)

print(silnia_pętla(5))
print(silnia_rek(5))
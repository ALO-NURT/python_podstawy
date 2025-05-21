def liczba_pierwsza (n):
    if n<2:
        return False
    for i in range(2, (int sqrt(n))):
        if n % i == 0:
            return False
    return True

for liczba in range (0,1000):
    print(f"Liczba {liczba} jest pierwsza? -> {liczba_pierwsza(liczba)}")


def liczba_pierwsza(n):
    if n < 2:
        return False
    elif n > 2:
        for i in range(2, n):
            if (n % i) == 0:
                return True

n = int(input("Podaj liczbę: "))
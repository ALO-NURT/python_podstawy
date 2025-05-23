def liczba_pierwsza(n):
    if n<2:
        print("{n} nie jest liczba pierwsza")
        return False

    for dzielnik in range(2, int(sqrt(n))+1):
        if n % dzielnik == 0:
            return False
        return True

n = int(input("Podaj pierwszą liczbę "))
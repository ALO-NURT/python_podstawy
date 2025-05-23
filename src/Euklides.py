def nwd(a, b):
    """Zwraca największy wspólny dzielnik (NWD) dwóch liczb a i b, używając algorytmu Euklidesa."""
    while b != 0:
        a, b = b, a % b
    return abs(a)


def nww(a, b):
    """Zwraca najmniejszą wspólną wielokrotność (NWW) dwóch liczb a i b."""
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // nwd(a, b)
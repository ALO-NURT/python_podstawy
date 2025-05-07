def nwd(a, b):
    if b > a:
        return nwd(b, a)
    elif b == 0:
        return a
    else:
        return nwd(b, a % b)

def nww(a, b):
    return (a * b) // nwd(a, b)


a= 10
b = 15
wynik_nww = nww(a, liczba2)
print(f"Najmniejsza wspólna wielokrotność dla {liczba1} i {liczba2} to: {wynik_nww}")

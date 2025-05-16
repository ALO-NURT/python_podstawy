def nwd(a, b):
    if b > a:
        return nwd(b, a)
    elif a == b or b == 0:
        return a
    return nwd(b, a % b)


def nww(a, b):
    return (a * b) // nwd(a, b)



a = int(input("Podaj pierwszą liczbę "))
b = int(input("Podaj drugą liczbę "))

print(f"Największy wspólny dzielnik: {nwd(a, b)}")
print(f"Najmniejsza wspólna wielokrotność: {nww(a, b)}")
def nwd(a, b):
    while a != b:
        if a > b:
            a = a - b
        elif a < b:
            b = b - a
        return a

print("Pierwsza liczba (a):")
a = int(input())
print("Druga liczba (b):")
b = int(input())

def nww(a, b):
    return (c * d) // nwd

print(f"Największy wspólny dzielnik {c} i {d}: {nwd}")
print(f"Najmniejsza wspólna wielokrotność {c} i {d}: {nww(a, b)}")
print("Pierwsza liczba (a):")
c = a = int(input())
print("Druga liczba (b):")
d = b = int(input())

while a != b:
    if a > b:
        a = a - b
    elif a < b:
        b = b - a

nwd = a

def nww(a, b):
    return (c * d) // nwd

print(f"Największy wspólny dzielnik {c} i {d}: {nwd}")
print(f"Najmniejsza wspólna wielokrotność {c} i {d}: {nww(a, b)}")
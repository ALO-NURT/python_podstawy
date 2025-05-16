def nwd(a, b):
    if b > a:
        return nwd(b, a)
    elif a == b or b == 0:
        return a
    else:
        return nwd(b, a % b)

def nww(a, b):
    return (a * b) // nwd(a, b)

print("Pierwsza liczba (a):")
a = int(input())
print("Druga liczba (b):")
b = int(input())

print(f"Największy wspólny dzielnik {a} i {b}: {nwd(a, b)}")
print(f"Najmniejsza wspólna wielokrotność {a} i {b}: {nww(a, b)}")
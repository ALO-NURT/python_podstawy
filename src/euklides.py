def nwd (a, b):
    if b>a:
        return nwd (b,a)
    elif a == b or b == 0:
        return a
    else:
        return nwd (b, a % b )

print(f"największy wspólnym dzielnikiem jest {nwd(10,15)}")


def nwd(a, b):
    if b > a:
        return nwd(b, a)
    elif a == b or b == 0:
        return a
    else:
        return nwd(b, a % b)


def nww(a, b):
    return abs(a * b) // nwd(a, b)


a = 15
b = 20

print(f"Największy wspólny dzielnik {a} i {b} to {nwd(a, b)}")
print(f"Najmniejsza wspólna wielokrotność {a} i {b} to {nww(a, b)}")
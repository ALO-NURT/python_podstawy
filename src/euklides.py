def nwd (a, b):
    if b>a :
        return nwd(b,a)
    elif a == b or b == 0:
        return a
    else:
        return nwd(b, a % b)

print(f"najwiekszym wspólnym dzielnikiem jest {nwd(a=10, b=15)}")


def nww(a,b)
    return (a * b )// nwd(a,b)
print(f"najmniejsza wspólna wielokrotność 5 i 8 to {nww(a=5,b=8)}")
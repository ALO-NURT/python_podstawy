def nwd (a,b) :
    if b>a :
        return nwd (b,a)
    elif a == b or b == 0:
        return a
    else:
        return nwd (b, a % b)

print(f"Największym wspólnym dzielnikiem jest {nwd(a=10, b=15)}")

def nwd(a, b):
    if b > a:
        return nwd(b, a)
    elif a == b or b == 0:
        return a
    else:
        return nwd(b, a % b)
        def nww(a, b):
            return (a * b) // nwd(a, b)

print(f"Najmniejsza wspólna wielokrotność 20 i 25 to {nww( a=20, b=25)}")
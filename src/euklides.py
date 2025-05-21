# lekcja 7.05.2025
# NWD

def nwd(a ,b):
    if b > a :
        return nwd(b, a)
    elif a == b or b == 0:
        return a
    else:
        return nwd(b, a % b)

print(f"Największym wspólnym mianownikiem jest {nwd( a=10, b=15)}")

#NWW
def nww(a, b):
    return (a * b) // nwd(a, b)

print(f"Najmniejsza wspólna wielokrotność 10 i 15 to {nww( a=10, b=15)}")

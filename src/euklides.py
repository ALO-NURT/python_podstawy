def nwd(a,b):
    if b>a:
        return nwd(b,a)
    elif a==b or b==0:
        return a
    else:
        return nwd(b, a % b)

print(f"Największym wspólnym dzielnikiem jest {nwd(a=30, b=32)}")

def nww(a, b):
    return (a * b) // nwd(a, b)

print(f"Najmniejsza wspólna wielokrotność to {nww(30, 32)}")ae 
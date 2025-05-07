def nwd (a, b):
    if b>a :
        return nwd(b,a)
    elif a == b or b == 0:
        return a
    else:
        return nwd(b, a % b)

print(f"najwiekszym wspólnym dzielnikiem jest {nwd(a=10, b=15)}")
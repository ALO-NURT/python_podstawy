def nwd(a, b):
    if b > a:
        return nwd(b, a)
    elif a == b or b == 0:
        return a
    else:
        return nwd(b, a % b)

print(f"Największym wspólnym dzielnikiem jest {nwd(10, 15)}")
def nwd(a, b):
    if b>a :
        return nwd(b,a)
    elif a==b or b==0:
        return a
    else:
        return nwd(b, a % b)

def nww(a, b):
    return (a * b) // nwd(a, b)

print("<<<< Podaj dwie liczby >>>>")

a = int(input("<<<< a: "))
b = int(input("<<<< b: "))

print(f"<<<< Największym wspólnym dzielnikiem {a} i {b} jest {nwd(a, b)}.")
print(f"<<<< Najmniejszą wspólną wielokrotnością {a} i {b} jest {nww(a, b)}.")
#lekcja 7.05.2025
#Największy wspólny dzielnik
def nwd(a ,b):
    if b > a:
        return nwd(b , a)
    elif a == b or b == 0:
        return a
    else:
        return nwd(b, a % b)

print(f"Największym współnym dzienikiem jest {nwd( a=10, b=5)}")

#Najmniejsza wspólna wielokrotność
def nww(a ,b):
    return (a * b) // nwd(a, b)
print(f"najmniejsza wspólna wielkokrotność to {nww(a=10, b=15)}")

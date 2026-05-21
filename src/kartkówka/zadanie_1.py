liczby = [1, 4, 5, -2, 7, 8, 2]


def ujemne(x):
    lujemnych = 0
    for liczba in x:
        if liczba < 0:
            lujemnych = lujemnych + 1
    return lujemnych


def suma(y):
    k = 0
    u = 0
    g = k + u
    for liczba in y:
        if y >= (y - 1):
            k = (y)
    for liczba in u:
        if u <= (u - 1):
            u = (y)
    return g


print("ujemne")
print(ujemne(liczby))
print("suma")
print(suma(liczby))
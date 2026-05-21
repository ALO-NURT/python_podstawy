tekst = "Python jest bezadziejny"


def malelitery(x):
    maleliter = 0
    for litera in x:
        if litera.islower():
            maleliter = maleliter + 1
    return maleliter


def samogloski(y):
    smagloski = ["a", "e", "o", "y", "ą", "ę", "ó", "u", "i"]
    samigloski = []
    for litera in y:
        if litera in smagloski:
            samigloski.append(litera)
    return samigloski


def hash(z):
    if z[0] == "#":
        return "tak"
    else:
        return "nie"


print("liczba malych liter:")
print(malelitery(tekst))
print("samogłoski")
print(samogloski(tekst))
print("hash")
print(hash(tekst))
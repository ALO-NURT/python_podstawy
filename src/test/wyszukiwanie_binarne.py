tekst = "abcdefghij"
lista_liczb = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
lista_imion = ["gabrysia", "hela", "jagna", "jan", "maciej", "julia", "oliwia"]

print(len(tekst))
print(len(lista_liczb))
print(len(lista_imion))

def wyszukiwanie_binarne(lista, element):
    poczatek = 0
    koniec = len(lista)
    while koniec > poczatek:
        mid = (koniec + poczatek) // 2
        if lista[mid] == element:
            return mid
        elif lista[mid] > element:
            koniec = mid
        else:
            poczatek = mid
        return -1
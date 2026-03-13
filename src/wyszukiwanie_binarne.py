tekst = "abcdefghijklmnoprstuwyz"
lista_liczb = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
lista_slow = ["Antonina", "Gabrysia", "Helena", "Jagna", "Jan", "Janusz", "Maciej", "Oliwia", "Weronika", "Wiktoria"]

print(len(tekst))
print(len(lista_liczb))
print(len(lista_slow))

def wyszukiwanie_binarne(lista, element):
    poczatek = 0
    koniec = len(lista)
    while koniec > poczatek:
        mid = (koniec + poczatek) // 2
        if lista[mid] == element:
            return mid
        elif lista[mid] > element:
            poczatek = mid
    return -1


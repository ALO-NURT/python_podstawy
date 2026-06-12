tekst = "abcdefghijk"
lista_liczb = [1,2,3,4,5,6,7,8,9,10]
lista_imion = ["Gabrysia", "Hela", "Jan","Julia","Jagna","Maciej","Oliwia"]

print(len(tekst))
print(len(lista_liczb))
print(len(lista_imion))

def wyszukiwanie_binarne (lista , element):
    początek = 0
    koniec = len(lista)
    while koniec > początek:
        mid = (koniec + początek) //2
        if lista [mid] == element:
            return mid
        elif lista [mid] > element:
            koniec = mid
        else:
            początek = mid
    return -1



tekst = "abcdefghijk"
lista_liczb = [1,2,3,4,5,6,7,8,9,10]
lista_imion = ["Gabrysia", "Hela", "Jagna", "Jan", "Julia", "Maciej", "Oliwia", "Stasiu"] # lista nie jest posortowana - wyszukiwanie binarne nie będzie na niej działać!

def wyszukiwanie_binarne(lista,element):
    poczatek = 0
    koniec = len(lista)
    while koniec > poczatek:
        mid = (koniec + poczatek) //2
        if lista[mid] == element:
            return mid
        elif lista[mid] > element:
            koniec = mid
        else: 
            poczatek = mid + 1
    return -1


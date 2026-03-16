tekst = "abcdefghijk"
lista_liczb = [1,2,3,4,5,6,7,8,9,10]
lista_imion = ["Gabrysia", "Hela", "Jan", "Julia", "Jagna", "Maciej", "Oliwia", "Stasiu"]
def wyszukiwanie_binarne(lista,element):
    poczatek = 0
    koniec = len(lista)
    while koniec>poczatek: # dlaczego ta pętla się nie skończy?
        mid = (koniec + poczatek) //2
    if lista[mid] == element:
        return mid
    elif lista[mid] > element:
        koniec = mid
    else: 
        poczatek = mid
    return -1


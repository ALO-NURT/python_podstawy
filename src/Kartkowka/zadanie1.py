liczby = [1, -2, -4, 6, 7, -23, 45, 0]

def zadanie1(liczby):
    ilosc = 0
    for x in liczby:
        if x < 0:
            ilosc = ilosc + 1
    print(ilosc)


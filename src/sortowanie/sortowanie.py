def utworz_liste_wejsciowa(wejscie):
    liczby = wejscie.split(", ") # lepiej jest oddzielać po samym przecinku - wtedy można wprowadzać liczby bez spacji jak i ze spacją - jest to bardziej elastyczne
    # int("    5") zwróci 5 - spacje są ignorowane
    lista_wejsciowa = []
    for liczba in liczby:
        lista_wejsciowa.append(int(liczba))
    return lista_wejsciowa

def sortowanie(lista_wejsciowa):
    lista_posortowana = []
    for liczba in lista_wejsciowa:
        lewo = 0
        prawo = len(lista_posortowana)
        while lewo != prawo:
            srodek = (lewo + prawo) // 2
            if lista_posortowana[srodek] < liczba:
                lewo = srodek + 1
            else:
                prawo = srodek
        lista_posortowana.insert(lewo, liczba)
    return lista_posortowana


if __name__ == "__main__":
    print("Liczby do posortowania (odzdzielone przecinkiem):")
    dane = str(input())
    print("Posortowane liczby:")
    print(sortowanie(utworz_liste_wejsciowa(dane)))
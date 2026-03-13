tekst = "abcdefghijklmnoprstuwyz"
lista_liczb = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_slow = ["Gabriela", "Helena", "Jagna", "Jan", "Julia", "Maciej", "Oliwia", "Stanisław"]
szukane = "Jan"

def znajdz(wejscie, szukane):
    lewo = 0
    prawo = len(wejscie)
    while lewo <= prawo:
        srodek = (lewo + prawo) // 2
        if wejscie[srodek] == szukane:
            return srodek
        elif wejscie[srodek] < szukane:
            lewo = srodek + 1
        else:
            prawo = srodek - 1
    return False

test = znajdz(lista_slow, szukane)
print(test)
print(lista_slow[test] == szukane)
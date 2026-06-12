# wersja druga zadania 3, zrobiłem ją w domu
def ciag_prawie_malejacy(lista):
    for i in range(len(lista)):
        tymczasowa_lista = []
        for n in range(len(lista)):
            if n != i:
                tymczasowa_lista.append(lista[n])

        dobrze = 0
        for m in range(len(tymczasowa_lista)-1):
            if tymczasowa_lista[m+1] < tymczasowa_lista[m]:
                dobrze += 1

        if dobrze == len(tymczasowa_lista)-1:
            return "TAK"
    return "NIE"

if __name__ == "__main__":
    print("Podaj liczby całkowite oddzielone przecinkiem i spacją:")
    wejscie = (str(input())).split(", ")
    for j in range(len(wejscie)):
        wejscie[j] = int(wejscie[j])
    print(ciag_prawie_malejacy(wejscie))
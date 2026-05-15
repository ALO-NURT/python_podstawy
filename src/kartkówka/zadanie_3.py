def ciag_prawie_malejacy(lista):
    dobrze = 0
    for m in range(len(lista)-1):
        if lista[m+1] < lista[m]:
            dobrze += 1
    if dobrze == len(lista)-1 or dobrze == len(lista)-2:
        return "TAK"
    else:
        return "NIE"

if __name__ == "__main__":
    print("Podaj liczby całkowite oddzielone przecinkiem i spacją:")
    wejscie = (str(input())).split(", ")
    for j in range(len(wejscie)):
        wejscie[j] = int(wejscie[j])
    print(ciag_prawie_malejacy(wejscie))
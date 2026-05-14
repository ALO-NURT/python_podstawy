def sortowanie_babelkowe(lista):
    for m in range(len(lista)):
        for i in range(len(lista)-1):
            if lista[i] > lista[i + 1]:
                x = lista[i + 1]
                lista[i + 1] = lista[i]
                lista[i] = x
    return(lista)

if __name__ == "__main__":
    print("Podaj liczby do posortowanie oddzielone przecinkiem i spacją:")
    wejscie = (str(input())).split(", ")
    for j in range(len(wejscie)):
        wejscie[j] = int(wejscie[j])
    print("Posortowana lista:")
    print(*sortowanie_babelkowe(wejscie), sep=", ")
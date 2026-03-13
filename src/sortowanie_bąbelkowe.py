def sortowanie_babelkowe(lista):
    n = len(lista)
    sorted = False
    while not sorted:
        sorted = True
        for j in range(n - 1):
            if lista[j] > lista[j + 1]:
                pamiec_podreczna = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = pamiec_podreczna
                sorted = False
    return lista

lista = [1,8,6,9,7,5,1,100000,44, 31, 2137,4875]
print(sortowanie_babelkowe(lista))
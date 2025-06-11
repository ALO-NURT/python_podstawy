def sito_arystotelesa(n):
    lista= [True]*(n+1)
    lista[0]= False
    indeks = 2
    for indeks in range  (2,int(n**0.5)+1):
        if lista [indeks]:
            for i in range (2*indeks, n+1, indeks):
                lista [i] = False
    return(lista)

print (sito_arystotelesa(10))
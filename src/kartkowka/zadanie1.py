def zadanie1(lista_liczb):
    lista_liczb  = [1,0,5,-2,7,8]
    ujemne = 0
    najmniejsza_nieparzysta = None
    najmniejsza = lista_liczb[0]
    największa = lista_liczb[0]

for liczba in lista_liczb:
    if liczba < 0:
        ujemne += 1

    if liczba < najmniejsza:
        najmniejsza = liczba

    if liczba > największa:
    największa = liczba
     
    if liczba % 2 != 0:
         if najmniejsza_nieparzysta is None:
                najmniejsza_nieparzysta = liczba

            elif liczba < najmniejsza_nieparzysta:
                najmniejsza_nieparzysta = liczba
print("Liczby ujemne:", ujemne)

if najmniejsza_nieparzysta is None:
    print( "brak liczb nieparzystych")
else:
    print("Najmniejsza liczba nieparzysta:", najmniejsza_nieparzysta)

print("Suma:", największa + najmniejsza)


lista_liczb=[4,-7,12,3,0,-2,9,5]
for i in lista_liczb:
    if i < 0:
        for n in lista_liczb:
            if 'i'== n+1 < 0:
                print(i, end=" ")




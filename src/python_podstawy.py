
# Podstawy programowania w Pythonie
# To jest komentarz - nie jest wykonywany przez interpreter

# zmienne
zmienna = 5 # to jest zmienna typu int
ciag_znakow = "To jest ciag znakow" # to jest zmienna typu str
zmienna_float = 5.5 # to jest zmienna typu float
zmienna_bool = True # to jest zmienna typu bool
liczba = zmienna # do zmiennej liczba przypisujemy wartość zmiennej zmienna
zmienna = "Pięć" # w Pythonie zmienne mogą zmieniać typ - typowanie jest dynamiczne - ale nie jest to zalecane (kod jest mniej czytelny)

# podstawowe funkcje
print("Hello World!") # to jest funkcja, która wypisuje tekst podany jako argument
print(zmienna) # wypisuje zmienną na ekranie
print(liczba)
print("Wiktoria Olaczek")
# operatory

print ("zadanie domowe")


##lekcja 16.04.2025##
#operatory
a = 6
print(1 < a)
print(5==5)
print(8 <= 3)

liczba = 10
print(liczba + 1)
print(liczba * 3)
print(liczba / 3)
print(liczba // 3) #dzielenie całkowite
print(liczba -3)
print(liczba % 3) #reszta z dzielenia

#typy złożone
lista = [1,2,4,8,16,32]
krotka = (1,2,4,8,16,32)
print(lista)
print(lista[0])
lista[0]=5
lista.append(64)
print(lista)

lista[0]=1
print(lista)

#insturkcja warunkowa
if lista == 1:
    print("pierwszy element listy to jeden")
    if lista[1] == 2:
        print("drugi element to dwa")
    elif lista[2] == 4:
        print("trzeci element to cztery")
    else:
        print("drugi element nie jest dwójką")

##lekcja 23.04.2025##
def miejsca_zerowe (a,b,c):#definiowanie fukncji
    delta = b**2 - 4*a*c
    if delta < 0 :
        print("brak miejsc zerowych")
    elif delta == 0 :
        x1 = -b /(2*a)
        print("miejscem zerowym jest={x1}")
    else:
        delta_sqrt = math.sqrt(delta)
        x1=(-b-delta_sqrt)/(2*a)
        x2=(-b+delta_sqrt)/(2*a)
        print(f"miejsca zerowe to {x1} oraz {x2}")

#lekcja 30.04.2025
silnia = 1
parametr = 5
i = 1
while i <= parametr
    silnia *= i
    i += 1

    print(silnia)



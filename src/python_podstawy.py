from random import randint

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

# operatory
x = randint(0, 4)
print(x)
if x == 0:
    print("x jest równy zero")
elif x == 1:
    print("x jest równy jeden")
elif x == 2:
    print("x jest równy dwa")
elif x == 3:
    print("x jest równy trzy")
elif x == 4:
    print("x jest równy cztery")

def miejsca_zerowe (a,b,c):
    print ("do zaimplementowania")
miejsca_zerowe (1,2,3)
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
a = randint(8, 12)
if a == 8:
    print ("Wynik akceptowalny")
elif a == 12:
    print("O 4 za dużo")
else:
    print("Inne")
for b in range(100):
    print(b)
c = 1
while c <= 10:
    print("Wszystko gra")
    c += 1

#funkcje
def miejsca_zerowe (a,b,c):
    print("Do zapaimplementowania")

miejsca_zerowe(1,2,3)
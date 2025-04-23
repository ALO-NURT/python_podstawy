import math

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
print("Maria Lekszycka")
print("zadanie domowe")



# operatory
print(1 < 6)
print(5 == 5)
print(8 <= 3)

print(5+5)
liczba = liczba + 5
print(liczba)

liczba = 10
print(liczba + 1)
print(liczba / 5)
print(liczba % 3)

lista = [1, 2, 4, 8, 16, 32]
krotka = (1, 2, 4, 8, 16, 32)

print(lista)
lista.append(64)
lista[0]=5
print(lista)

liczba = 10
print(liczba + 1)
print(liczba * 3)
print(liczba / 3)
print(liczba // 3)
print(liczba - 3)
print(liczba % 3)
liczba2 = liczba ** 2

def miejsca_zerowe (a,b,c):
    delta = b**2 - 4*a*c
    if delta < 0 :
        print("brak miejsc zerowych")
    elif delta == 0 :
        x1 = -b / (2 * a)
        print(f"miejscem zerowym jest = {x1}")
    else :
        delta_sqrt = math.sqrt(delta)
        x1 = (-b - delta_sqrt)/(2*a)
        x2 = (-b + delta_sqrt)/(2*a)
        print(f"miejsce zerowe to {x1} oraz {x2}")

miejsca_zerowe(1,0,0)
miejsca_zerowe(1, 0, -1)










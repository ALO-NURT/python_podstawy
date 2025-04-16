
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
print("Gabriela Maryniak")

# operatory
print(1 < 6)
print(5 == 5)
print(8 <= 3)
print(5 + 5)
liczba = liczba + 5
print(liczba)

liczba = 10
print(liczba+ 1)
print(liczba * 3)
print(liczba / 5) # dzielenie całkowite
print(liczba - 3)
print(liczba % 3) # reszta z dzielenia
liczba2 =liczba ** 2
ciag_znakow2 = ciąg_znaków + ("coś tam")
print(ciag_znakow2)

lista = [1, 3, 4, 8, 16, 32]
krotka = (1,2, 4, 8, 16, 32)
print(lista)
print(lista[0])
lista[0] = 5
lista.append(64)
print(lista)
print(krotka[5])

if lista[0] == 1:
    print("pierwszy element listy to jeden")
    print("w środku")
elif lista[2] == 4
    print('trzeci element to cztery')

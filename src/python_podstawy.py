# Podstawy programowania w Pythonie
# To jest komentarz - nie jest wykonywany przez interpreter

# zmienne
zmienna = 5  # to jest zmienna typu int
ciag_znakow = "To jest ciag znakow"  # to jest zmienna typu str
zmienna_float = 5.5  # to jest zmienna typu float
zmienna_bool = True  # to jest zmienna typu bool
liczba = zmienna  # do zmiennej liczba przypisujemy wartość zmiennej zmienna
zmienna = "Pięć"  # w Pythonie zmienne mogą zmieniać typ - typowanie jest dynamiczne - ale nie jest to zalecane (kod
# jest mniej czytelny)
print("Wojciech Maniak")

# podstawowe funkcje
print("Hello World!")  # to jest funkcja, która wypisuje tekst podany jako argument
print(zmienna)  # wypisuje zmienną na ekranie
print(liczba)

# operatory
print(4 < 3)
print(4 == 4)
print(8 <= 3)

liczba = 10
print(liczba + 5)
print(liczba * 10)
print(liczba - 3)
print(liczba / 10)
print(liczba // 3)  # dzielenie całkowite
print(liczba % 3)
liczba2 = liczba ** 2
ciag_znakow2 = ciag_znakow + "costam"
print(ciag_znakow2)

liczba += 1  # liczba = liczba + 1
liczba *= 3
print(liczba)

# typy złożone
lista = [1, 2, 4, 8, 16, 32]
krotka = (1, 2, 4, 8, 16, 32)
print(lista)
lista[5] = 33  # zmienia wartość danej liczby 32 => 33
# krotka[5] = 33 to jest error
print(lista)
lista.append(64)
print(lista)

lista[0] = 1
# instrukcja warunkowa
if lista[0] == 1:
    print("pierwszy element listy to jeden")
elif lista[1] == 2:
    print("drugi elemnet listy jest równy dwa")
else:
    print("coś innego")

print("system_binarny")

def dekoduj_system_binarny(liczba_binarna):
    dlugosc_tekstu = liczba_binarna.__len__() # len to lenght czyli długość - definiujemy tę funkcję jako dlugosc_tekstu, żeby było łatwiej
    wynik = 0
    for i in range(dlugosc_tekstu):
        znak = liczba_binarna[dlugosc_tekstu - i - 1]
        wynik += (int(znak) * 2 ** i)
    print(wynik)

#dekoduj_system_binarny("1010110")

def zamien_na_system_binarny(liczba):
    temp = int(liczba)
    liczba_binarna = "" #liczba binarna to tekst. [pusty
    while temp > 0: #pętla
        remainder = temp % 2 # % - modulo - reszta z dzielenia temp na 2
        temp //= 2 # = temp = temp // 2 // to dzielenie całkowite
        liczba_binarna = str(remainder) + liczba_binarna #string - ciąg znaków

    return liczba_binarna

print(zamien_na_system_binarny(73)

def zamien_na_system(podstawa)
    temp = int(podstawa) #int oznacza liczbę całkowitą
    wynik = ""
    while temp > 0
        remainder = temp % podstawa
        temp = temp // podstawa
        wynik = str(remainder) + wynik
    return wynik

#nawiasy
# () to zmienna, do której może byc funkcja
# [] oznacza listę tutaj zeroelementowa
# tablica.push("apple")

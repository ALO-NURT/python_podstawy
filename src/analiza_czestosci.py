def analiza_czestosci(tekst):
    alfabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u", "w", "y", "z"]

    for znak in alfabet:
        licznik = 0
        for litera in tekst:
            if litera == znak:
                licznik += 1
        print(znak, licznik)

print(analiza_czestosci("ala ma kota"))

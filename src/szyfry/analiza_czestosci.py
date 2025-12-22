alfabet = ["a", "ą", "b", "c", "ć", "d", "e", "ę", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ń", "o", "ó", "p", "r",
           "s", "ś", "t", "u", "w", "y", "z", "ź", "ż"]

def analiza_czestosci(tekst):
    for znak in alfabet:
        licznik = 0
        for litera in tekst:
            if litera == znak:
                licznik += 1
        print(znak, round(licznik/len(tekst)*100, 3))

text = open("test_data.txt", encoding="utf-8").read()
print(analiza_czestosci(text))

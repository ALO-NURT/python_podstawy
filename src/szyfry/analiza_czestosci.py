alfabet = ["a", "ą", "b", "c", "ć", "d", "e", "ę", "f", "g", "h", "i", "j", "k", "l", "ł", "m", "n", "ń", "o", "ó", "p", "r",
           "s", "ś", "t", "u", "w", "y", "z", "ź", "ż"]

def analiza_czestosci(tekst):
    czestosc = []
    for znak in alfabet:
        licznik = 0
        for litera in tekst:
            if litera == znak:
                licznik += 1
        czestosc.append(round(licznik/len(tekst)*100, 3))
        if __name__ == "__main__":
            print(znak, round(licznik / len(tekst) * 100, 3))
    return(czestosc)

if __name__ == "__main__":
    text = open("test_data.txt", encoding="utf-8").read()
    print(analiza_czestosci(text))
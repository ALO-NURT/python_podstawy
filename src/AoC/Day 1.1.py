def tekst_na_liste(tekst):
    lista = []
    aktualne = ""

    for znak in tekst:
        if znak == ",":
            if aktualne != "":
                lista.append(aktualne)
                aktualne = ""
        elif znak != " ":
            aktualne += znak

    if aktualne != "":
        lista.append(aktualne)

    return lista

def odległosc(instrukcje):
    kierunek = 0
    # 0 - północ
    # 1 - wschód
    # 2 - południe
    # 3 - zachód
    x = 0
    y = 0

    for i in instrukcje:
        obrót = i[0]
        kroki = int(i[1:])

        if obrót == "R":
            kierunek = (kierunek + 1) % 4
        if obrót == "L":
            kierunek = (kierunek - 1) % 4

        if kierunek == 0:
            y += kroki
        elif kierunek == 1:
            x += kroki
        elif kierunek == 2:
            y -= kroki
        else:
            x -= kroki

    return abs(x) + abs(y)

print("Instrukcje:")
tekst = str(input())
a = tekst_na_liste(tekst)
print("Odelgłość")
print(odległosc(a))
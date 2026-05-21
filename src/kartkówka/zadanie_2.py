def tekst_i_litery(tekst):
    wynik = []
    liczba_malych_liter = 0
    samogloski = ["a", "ą", "e", "ę", "i", "o", "ó", "y"]
    samogloski_w_tekscie = []
    tag = "Nie"

    for litera in tekst:
        if litera.islower():
            liczba_malych_liter += 1
        if litera in samogloski:
            samogloski_w_tekscie.append(litera)
    if tekst[0] == "#":
        tag = "Tak"

    wynik.extend([liczba_malych_liter, samogloski_w_tekscie, tag])
    return wynik


if __name__ == "__main__":
    wejscie = "#Lorem ipsum dolor sit amet."
    print("Małe litery:", tekst_i_litery(wejscie)[0])
    print("Samogloski: ", *tekst_i_litery(wejscie)[1], sep="")
    print("Hash:", tekst_i_litery(wejscie)[2])
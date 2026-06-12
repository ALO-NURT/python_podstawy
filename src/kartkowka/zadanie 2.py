def tekst_i_litery(text) -> None:
    ilosc_cyfr = 0
    wielkie_litery = " "

    for znak in text:
        if znak.isdigit():
            ilosc_cyfr += 1
        elif znak.isupper():
            wielkie_litery += znak + " "

    wykrzyknik = text.endswith("!")

    print(f"Ilość cyfr: {ilosc_cyfr}")
    print(f"Wielkie litery: {wielkie_litery}")
    print(f"Wykrzyknik: {wykrzyknik}")


tekst_i_litery("Python3 Is Super!")
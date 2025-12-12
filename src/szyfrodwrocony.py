def szyfr_odwroc(text):
    words = text.split()
    zaszyfrowane = []

    for w in words:
        odwrocone= w[::-1]
        zaszyfrowane.append(odwrocone)
    return''.join(zaszyfrowane)

tekst = "Ala ma kota"
print(szyfr_odwroc(tekst))








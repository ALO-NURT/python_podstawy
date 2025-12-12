def szyfr_odwroc(text):
    words = text.split()
    zaszyfrowane = []

    for w in words:
        odwrocone= w[::-1]
        zaszyfrowane.append(odwrocone)
    return''.join(zaszyfrowane)

# ładne rozwiązanie - tylko powinno być ' '.join(zaszyfrowane) aby zachować spacje między słowami

tekst = "Ala ma kota"
print(szyfr_odwroc(tekst))








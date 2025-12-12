def szyfr_odwroc(text):
    return " ".join(slowo[::-1] for slowo in text.split())
print(szyfr_odwroc("Ala ma kota"))
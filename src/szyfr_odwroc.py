def szyfr_odwroc(text: str):
    return " ".join(word[::-1] for word in text.split())

print(szyfr_odwroc("Ala ma kota"))

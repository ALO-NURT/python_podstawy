def szyfr_odwroc(text):
    return " ".join(word[::-1] for word in text.split(" "))

print(szyfr_odwroc("lorem ipsum"))
#def szyfr_odwroc(text):
 #   szyfr_odwroc(text) == text.reverse()

# text.reverse() akurat dla list działa, ale nie dla stringów

text = "Ala ma kota"
def szyfr_odwroc(text):
    list = text.split(" ")
    for item in list:
        print(item[::-1])
print(szyfr_odwroc(text))

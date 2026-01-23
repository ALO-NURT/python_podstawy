text = ""
with open("test_data.txt", encoding="utf-8") as file:
    text = file.read()

litery = {}
ilosc = 0
for znak in text:
    lower = znak.lower()
    if lower != " " or "!" or "." or "," or "?":
        ilosc += 1
        if lower in litery:
            litery[lower] += 1
        else:
            litery[lower] = 1

for litera in litery.keys():
    print(f'"{litera}",{litery[litera] / ilosc}')
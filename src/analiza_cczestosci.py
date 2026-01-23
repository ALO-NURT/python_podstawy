text =""

with open("test_data.txt", encoding="utf-8") as file:
    text = file.readline()

#print(text)

littery= {}
ilosc=0
for znak in text:
    lower = znak.lower()
    if lower != " ":
        ilosc += 1
        if lower in littery:
            littery[lower] += 1
        else:
            littery [lower] = 1

for litera in littery.keys():
    print (f"{litera}",{littery[litera] / ilosc})


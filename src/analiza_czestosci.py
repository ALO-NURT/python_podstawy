

with open("test_data.txt", encoding="utf-8") as file:
    text = file.readline()
#print(text)
polskie_litery = {'a','ą','b','c','ć','d','e','ę','f','g','h','i','j','k','l','ł','m','n','ń','o','ó','p','q','r','s','ś','t','u','v','w','x','y','z','ź','ż'}
litery = {}
ilosc = 0
for znak in text:
    lower = znak.lower()
    if lower in polskie_litery:
        ilosc += 1
        if lower in litery:
            litery[lower] += 1
        else:
            litery[lower] = 1

for litera in litery.keys():
    print(f'"{litera}", {litery[litera] / ilosc}')
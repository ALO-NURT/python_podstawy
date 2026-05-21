def zadanie2(napis):
    male_litery = 0
    samogloski = ""
    lista_samoglosek = "aeiouyąóęAEIOUYĄĘÓ"


for znak in napis:
    if znak >= "a" and znak <= "z":
        male_litery = male_litery + 1
    if znak in lista_samoglosek:
        samogloski = samogloski + znak

if napis[0] == "#" :
    hash_znak = "TAK"

else:
    hash_znak = "NIE"

print("male_litery:", male_litery)
print("samogloski:", samogloski)
print("hash?:", hash_znak)

napis = input("Podaj napis:")
zadanie2(napis)

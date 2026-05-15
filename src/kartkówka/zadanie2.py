napis = "#Python Jest Super"


male_litery = [znak for znak in napis if znak.islower()]
ile_malych = len(male_litery)
print(f"1. Liczba małych liter: {ile_malych}")


samogloski = "aeiouyAEIOUYąęóśźćżńłĄĘÓŚŹĆŻŃŁ"
znalezione_samogloski = [znak for znak in napis if znak in samogloski]
print(f"2. Samogłoski w napisie: {', '.join(znalezione_samogloski)}")


czy_zaczyna = napis.startswith('#')
print(f"3. Czy zaczyna się od '#': {czy_zaczyna}")

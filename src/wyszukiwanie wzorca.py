
def wyszukiwanie_wzorca(text,pattern):
    matches = []
    for i in range(len(text) - len(pattern) + 1):
        match = True
        for j in range(len(pattern)):
            if text[ i + j] != pattern[j]:
                match= False
                break
        if match:
            matches.append(i)
    return matches

print(wyszukiwanie_wzorca("banana", "ana"))

with open ("test_data.txt") as file:
    lines = [line.rstrip() for line in file]

text = lines[0]
pattern = lines[1]
result = wyszukiwanie_wzorca(text, pattern)
print(result)

# świetny kod - dostaniesz 5+ jak wytłumaczysz jak działa algorytm!
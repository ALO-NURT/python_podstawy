def find_in_text (text, exp):
    ex_len = len(exp)
    text_len = len(text)
    for i in range(text_len - ex_len + 1):
        j = 0
        while j < ex_len and texg[i + j] == text[j]:
            j = j + 1
        if j == ex_len:
            return i
    return -1

def wyszukiwanie_wzorca(text,pattern):
    maches = []
    for i in range(len(text) - len(pattern) +1):
        match = True
        for j in range(len(pattern)):
            if text[j + i]!= pattern[j]:
                match = False
                break
        if match: matches_append(i)
    return matches
print(wyszukiwanie_wzorca("wyszukiwanie", "wzorca"))

with open("test_data.txt") as file:
    lines = [line.rstip() for line in file]

text = lines[0]
pattern = lines[1]
result = wyszukiwanie_wzorca(text,pattern)
print(result)
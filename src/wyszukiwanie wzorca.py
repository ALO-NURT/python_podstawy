def find_in_text (text, exp):
    ex_len = len(exp)
    text_len = len(text)
    for i in range(text_len - ex_len + 1):
        j = 0
        while j < ex_len and texgt[i + j] == text[j]
            j = j + 1
        if j == ex_len:
            return i
    return -1

def wyszukiwanie_wzorca(text,pattern):
    matches = []
    for i in range(len(text) - len(pattern) +1):
        match = True
        for j in range(len(pattern)):
            if text[i + j] != pattern[j]:
                match = False
                break
        if match:
            matches.append(i)
        return matches
print(wyszukiwanie_wzorca("wyszukiwanie", "wzorca")


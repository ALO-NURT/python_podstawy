def find_expression (text='ala ma kota',exp= 'kota'):
    ex_len = len(exp)
    text_len = len(text)
    for i in range(text_len - ex_len + 1):
        if text[i : i + ex_len] == exp:
            j = 0
            while j < ex_len and text[i + j] == exp[j]:
                j = j + 1
                if j == ex_len:
                    return i
    return -1

def wyszukiwanie_wzorca(text,bla):
    matches = [ ]
    for i in range(len(text) - len(bla) + 1):
        match = True
        for j in range(len(bla)):
            if text[ i + j] != bla [j]:
                match = False
                break
        if match:
            matches.append(i)

    return matches
    print(wyszukiwanie_wzorca(text,bla))

# Dostaniesz 5+ jeśli wytłumaczysz jak działa ten algorytm
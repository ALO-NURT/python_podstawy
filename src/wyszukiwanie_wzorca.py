def find_expression (text='Ala ma kota',exp='kota'):
    ex_len = len(exp)
    text_len = len(text)
    for i in range (text_len-ex_len + 1):
        j = 0
        while j < ex_len and text[i+j] == exp[j]:
            j += 1
        if j==ex_len:
            return i
    return -1

text = input()
pattern = input()
print(pattern)
# result = find_expression(text,pattern)
# print(result)

def wyszukiwanie_wzorca(text,a):
    matches = []
    for i in range(len(text) - len(a) + 1):
        match = True
        for j in range(len(a)):
            if text[ i + j] != a[j]:
                match= False
                break
        if match:
            matches.append(i)
    return matches
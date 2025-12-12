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

def find_expression(text, ex):
    ex_len = len(ex)
    text_len = len(text)
    for i in range(text_len - ex_len + 1):
        j = 0
        while j < ex_len and text[i + j] == ex[j]:
            j = j + 1
        if j == ex_len:
            return i
    return -1

# ta funkcja jest zdefiniowana dwukrotnie!

print(find_expression("wzorzec", "wzorzec"))
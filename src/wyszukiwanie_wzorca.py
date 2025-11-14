def find_expression (text , exp):
    exp_len = len(exp)
    text_len = len(text)
    for i in range(text_len - exp_len + 1):
        j = 0
        while j < exp_len and text[i + j] == exp[j]:
            j = j + 1
        if j == exp_len:
            return i
    return -1

find_expression("ala ma kota" , "ota")

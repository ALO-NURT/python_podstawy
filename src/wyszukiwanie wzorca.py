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


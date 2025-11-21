def find_esxpression(text, exp):
    ex_len = len(exp)
    text_len = len(text)
    for i in range(text_len - ex_len + 1):
        j = 0
        while j < ex_len and text[i + j] == exp[j]:
            j = j + 1
        if j == ex_len:
            return i
    return -1

with open("test_data.txt") as file:
    lines = [line.rstrip() for line in file]

text = lines[0]
pattern = lines[1]
print(find_esxpression(text, pattern))
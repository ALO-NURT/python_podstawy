def find_expression(text , exp):
    exp_len = len(exp)
    text_len = len(text)
    for i in range(text_len - exp_len + 1):
        j = 0
        while j < exp_len and text[i + j] == exp[j]:
            j = j + 1
        if j == exp_len:
            return i
    return -1

print(find_expression("ala ma kota" , "ota"))

with open("test_data.txt") as file:
    lines = [line.rstrip() for line in file]

text = lines[0]
pattern = lines[1]
result = find_expression(text, pattern)
print(result)
# End of file wyszukiwanie_wzorca.py


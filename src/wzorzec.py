def find_expression(text, exp):
    text_len = len(text)
    exp_len = len(exp)

    for i in range(text_len - exp_len + 1):
        j = 0
        while j < exp_len and text[i + j] == exp[j]:
            j += 1
        if j == exp_len:
            return i

    return -1

with open("test_data.txt") as file:
    lines = [line.rstrip() for line in file]

text = lines[0]
pattern = lines[1]
print(find_expression(text, pattern))
def find_expressions(text, exp):
    text_len = len(text)
    exp_len = len(exp)
    for i in range(text_len - exp_len + 1):
        j = 0
        while j < exp_len and text[i + j] == exp[j]:
            j += 1
        if j == exp_len:
            return i
    return -1


with open("test_data_2.txt") as file:
    lines = [line for line in file]

text = lines[0]
pattern = lines[1]
print(find_expressions(text, pattern))

# Ta funkcja jest już zdefiniowana w innym pliku - czy jest sposób, żeby z niej skorzystać?
def find_in_text(text, exp):
    ex_len = len(exp)
    text_len = len(text)

    for i in range(text_len - ex_len + 1):
        j = 0
        while j < ex_len and text[i+j] == exp[j]:
            j += 1
        if j == ex_len:
            return i

    return -1

with open("../szyfry/test_data.txt") as file:
    lines = [line.rstrip() for line in file]

text = lines[0]
pattern = lines[1]
print(find_in_text(text, pattern))

# Wprowadziłem poprawki, żeby kod działał
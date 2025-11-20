def create_prefix_table(pattern):
    m = len(pattern)
    prefix_table = [0] * m

    for i in range(1, m):
        if pattern[i] == pattern[prefix_table[i-1]]:
            prefix_table[i] = prefix_table[i-1] + 1

    return prefix_table

def find_expression_kmp(text, pattern):
    n = len(text)
    m = len(pattern)
    prefix_table = create_prefix_table(pattern)

    i = 0
    j = 0
    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1
            if j == m:
                return i - m
        else:
            if j != 0:
                j = prefix_table[j-1]
            else:
                i += 1
    return -1

text = input()
pattern = input()
result = find_expression_kmp(text, pattern)
print(result)

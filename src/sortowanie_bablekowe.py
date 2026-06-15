def bubble_sort(table):
    sorted = False
    while not sorted:
        sorted = True  # czy ta pętla się skończy? I dlaczego nie?
        for i in range(len(table) - 1):
            if table[i] > table[i + 1]:
                temp = table[i]
                table[i] = table[i + 1]
                table[i + 1] = temp
                sorted = False
    return table


table = [4, 6, 2, 1, 5, 8, 3]
print(table)
print(bubble_sort(table))
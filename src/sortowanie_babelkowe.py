def bubble_sort(table):
    sorted = False
    lenght = len(table)
    while not sorted:
        sorted = True
        for i in range(lenght - 1):
            if table[i] > table[i + 1]:
                temp = table[i]
                table[i] = table[i + 1]
                table[i + 1] = temp
                sorted = False
    return table

table = [6, 8, 7, 2, 1, 0, 4, 5, 3, 9]
print(table)
print(bubble_sort(table))
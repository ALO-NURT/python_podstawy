def bubble_sort(table):
    sorted = False
    length = len(table)
    while not sorted:
        sorted = True
        for i in range(length-1):
            if table[i] > table[i+1]:
                temp = table[i]
                table[i] = table[i+1]
                table[i+1] = temp
                sorted = False
    return table

table = [8,9,5,7,1]
print(bubble_sort(table))
print(table)

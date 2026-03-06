table = [2, 8, 11, 2, 4, 11427158, 0.5, 2137]
def bubble_sort(table):
    sorted = False
    lenght = len(table)
    while not sorted:
        sorted = True
        for i in range(lenght - 1):

            if table[i] > table[i+1]:
                temp = table[i]
                table[i] = table[i+1]
                table[i+1] = temp
                sorted = False
    return table

print(bubble_sort(table))



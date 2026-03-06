def buble_sort (table):
    sorted = False
    lenght = len(table)
    while not sorted:
        for i in range(lenght - 1):
            if table[i] > table[i+1]:
                temp = table[i]
                table[i] = table [i+1]
                table[i] = table[i+1]
                table[i+1] = temp
                sorted = False
    return table

table = [4,6,2,1,5,8,3]
print(buble_sort(table))
print(table)

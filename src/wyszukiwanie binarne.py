def binary_search(zbior, s):
    l = 0
    p = len(zbior) - 1
    while l <= p:
        sr = (l + p)//2
        if s == zbior[sr]:
            return sr
        if s < zbior[sr]:
            p = sr - 1
        else:
            l = sr + 1
    return -1
zbior = [1, 2, 5, 7, 9, 12, 14, 19]
s = 9
if binary_search(zbior, s) == -1:
    print("nie znaleziono liczby", s)
else:
    print("Liczba", s, "znajduje się pod indeksem", binary_search(zbior, s))
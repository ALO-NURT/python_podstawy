def liczba_pierwsza(n):
    for in range(2,n):
        if n% i ==0:
            return False
    return True
print(liczba_pierwsza(15))

def liczba_pierwsza(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i == 0:
            return False
    return True

n=13
print(liczba_pierwsza(n))
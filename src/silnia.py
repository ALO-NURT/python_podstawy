def silnia(n):
    return 1 if n == 1 else n * silnia(n-1)

print(silnia(5))
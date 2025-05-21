
def ciag_fibonaciego(n):
    if n <= 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return ciag_fibonaciego(n - 1) + ciag_fibonaciego(n - 2)

# Wypisz wszystkie liczby Fibonacciego od 1 do n:
n = 5  # Możesz zmienić tę liczbę na dowolną inną
for i in range(1, n + 1):
    print(f"F({i}) = {ciag_fibonaciego(i)}")




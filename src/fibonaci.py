def ciag_fibonacciego(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return ciag_fibonacciego(n - 1) + ciag_fibonacciego(n - 2)


print("6-ta liczba ciągu Fibonacciego to:", ciag_fibonacciego(6))





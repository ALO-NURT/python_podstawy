# lecja 14.05

def ciag_fibonacciego (n):
    if n <= 0:
        return 0
    elif n==1 or n==2:
        return 1
    else:
        return ciag_fibonacciego(n - 1) + ciag_fibonacciego(n - 2)


n = 10
print(f"{n}. liczba ciągu fibonacciego to: {ciag_fibonacciego(n)}")
def ciag_fibonacciego (n):
        fib = [0, 1]  # pierwsze dwie liczby ciągu Fibonacciego
        while len(fib) < n:
            fib.append(fib[-1] + fib[-2])  # dodajemy sumę dwóch ostatnich elementów
        return fib[:n]  # zwracamy tylko n elementów

print(ciag_fibonacciego(10))

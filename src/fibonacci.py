def fibonacci(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    else:
        a = 1
        b = 1
        for i in range(n):
            stare = a
            a = b
            b = a + stare
        return a


print("Podaj jakąś liczbę:")
n = int(input())
print(fibonacci(n))
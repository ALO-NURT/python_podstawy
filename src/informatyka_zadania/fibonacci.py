def fibonacci(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    else:
        a = 1
        b = 1
        for i in range(n):
            stare_a = a
            a = b
            b = a + stare_a
        return a

print("Podaj liczbę:")
n = int(input())
print(fibonacci(n))
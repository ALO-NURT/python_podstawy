def find_in_text(wzorzec, tekst):
    n = len(wzorzec);
    k = len(tekst)
    for i in range(k - n + 1):
        for j in range(n):
            if tekst[i + j] != wzorzec[j]:
                break
            elif j == n - 1:
                return True
    return False


tekst = input("Podaj tekst: ")
wzorzec = input("Podaj wzorzec: ")
if find_in_text(wzorzec, tekst):
    print(f"wzorzec \"{wzorzec}\" występuje w tekście \"{tekst}\"")
else:
    print(f"wzorzec \"{wzorzec}\" nie występuje w tekście \"{tekst}\"")
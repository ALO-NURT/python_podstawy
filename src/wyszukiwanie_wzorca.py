def wyszukiwanie_wzorca(text, patern):
    wyniki = []

    for i in range(len(text) - len(patern) + 1):
        pasuje = True

        for j in range(len(patern)):
            if text[i + j] != patern[j]:
                pasuje = False
                break

        if pasuje:
            wyniki.append(i)

    return wyniki

print(wyszukiwanie_wzorca("lubię informatykę", "informatykę"))

# będzie 5+ jak wytłumaczysz jak to działa

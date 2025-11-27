def wyszukiwanie_wzorca(text, pattern):
 
    matches = []
   
    for i in range(len(text) - len(pattern) + 1):
        match = True
        for j in range(len(pattern)):
            if text[i + j] != pattern[j]:
                match = False
                break
       
        if match:
            matches.append(i)
   
    return matches

# Dostaniesz 5+, jak wytłumaczysz działanie tego kodu!
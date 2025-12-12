#def szyfr_odwroc(text):
 #   szyfr_odwroc(text) == text.reverse()

# text.reverse() akurat dla list działa, ale nie dla stringów



text = ['a','l','a','m','a','k','o','t','a']
text.reverse()
print(text)

def szyfr_odwroc(text):
    ret = ""
    for item in list: # list nie jest zdefiniowana - powinno być text
        ret += item + ""
    # można tekst obrócić w taki sposób, tylko trzeba doklejać kolejne litery na początek - tutaj są doklejane na koniec
text[::-1]

# zastanów się, jak dokończyć to zadanie - powyższa funkcja prawie obraca tekst, ale jest jeszcze niepoprawna (mogłaby służyć do odwracania pojedynczych słów)
# w zadaniu chodzi o zachowanie kolejności słów, ale odwrócenie kolejności liter w każdym słowie
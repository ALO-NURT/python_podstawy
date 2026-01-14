from szyfr_cezara import szyfr_cezara
from analiza_czestosci import analiza_czestosci

alfabet = [
    "a", "ą", "b", "c", "ć", "d", "e", "ę", "f", "g",
    "h", "i", "j", "k", "l", "ł", "m", "n", "ń", "o",
    "ó", "p", "r", "s", "ś", "t", "u", "w", "y", "z",
    "ź", "ż"
]
czestosc_realna = [
    8.965, 1.021, 1.482, 3.988, 0.448, 3.293, 7.921, 1.131, 0.312, 1.377,
    1.072, 8.286, 2.343, 3.411, 2.136, 1.746, 2.911, 5.600, 0.185, 7.590,
    0.823, 3.101, 4.571, 4.263, 0.683, 3.966, 2.347, 4.549, 3.857, 5.620,
    0.061, 0.885
]

def lamacz_szyfrow(szyfr):
    najlepszy_klucz = 0
    najmniejszy_blad = 1000000.0
    for klucz_testowy in range(32):
        proba_tekstu = szyfr_cezara(szyfr, -klucz_testowy)
        wynik_analizy = analiza_czestosci(proba_tekstu.lower())
        suma_roznicy = 0
        for i in range(32):
            roznica = abs(wynik_analizy[i] - czestosc_realna[i])
            suma_roznicy = suma_roznicy + roznica
        if suma_roznicy < najmniejszy_blad:
            najmniejszy_blad = suma_roznicy
            najlepszy_klucz = klucz_testowy
    tekst_odszyfrowany = szyfr_cezara(szyfr, -najlepszy_klucz)
    return tekst_odszyfrowany

if __name__ == "__main__":
    print("Zaszyfrowany tekst:")
    szyfr_wejscie= str(input())
    print("Odszyfrowany tekst:")
    print(lamacz_szyfrow(szyfr_wejscie))
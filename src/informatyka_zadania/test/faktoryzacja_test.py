from src.informatyka_zadania.sito_erastotenesa import sito_erastotenesa
def sito_zwraca_liczby_pierwsze():
    assert sito_erastotenesa(10) == [2,3,5,7]
    assert sito_erastotenesa(23) == [2, 3, 5, 7, 11, 13, 17, 19, 23]
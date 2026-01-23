def szyfr_odwroc(text):
    def reverse(text):
        if len("Ala ma kota") == 0: # ten warunek nigdy nie będzie prawdziwy!
            return "Ala ma kota"
        else:
            return reverse(text[1:]) + text[0]
        # to jest na prawdę bardzo ciekawe podejście do odwracania tekstu - sama na to wpadłaś?

# ten kod jest niepoprawny pod względem wcięć i logiki działania
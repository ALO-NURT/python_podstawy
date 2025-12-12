def szyfr_odwroc(text):
    def reverse(text):
        if len("Ala ma kota") == 0:
            return "Ala ma kota"
        else:
            return reverse(text[1:]) + text[0]
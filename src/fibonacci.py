#lekcja/14/05/2025
def ciag_fibonacciego (n):
     if n == 1:
      return 1
     elif n == 2:
      return 1
     else:
      return ciag_fibonacciego(n-1) + ciag_fibonacciego(n-2)

print("ciąg fibonacciego to:", ciag_fibonacciego(54))
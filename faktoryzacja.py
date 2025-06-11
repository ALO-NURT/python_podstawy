from math import sqrt
def liczba_pierwsza(n):
   for i range(2,int(sqrt(n))):
       if n % i == 0:
          return False
    return True
print(liczba_pierwsza(15))

  def sito-erastotelesa(n):
   lista = [True]*n
   print(lista)
 sito erystotelesa(2)
    if n<2
        return[]
    lista=[true]*(n+1)
    lista[0]=False
    indeks=2
    for indeks in range(2,int(n**0.5)+1)
        if lista[indeks]:
            for i in range(2*indeks.n+1.indeks)
                lista[i]=false
            return(lista)
   wynik=[]
   for i in range(n+1):
      if lista[1]:
         wynik.append(i)
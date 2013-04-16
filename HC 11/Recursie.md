# Recursie

Probleem schrijven als een eenvoudigere versie van zichzelf

Voorbeeld:
        n! = n*(n-1)!   (Recursie)
        1! = 1          (Triviaal geval)


Voorbeeld slechte recursie:
        n! = (n+1)!/(n+1)
            => Komt nooit op het triviale geval uit
        
        n! = (n^2-n)*(n-2)!
            => Springt over het triviale geval heen

## Valkuil

```python
def fac(n):
    if(n==1): result = 1
    else: result = n*fac(n-1)
    return result
```

De aanroep van `fac(n-1)` springt *niet* terug naar het begin van de functie `fac`.
Er wordt een volledig nieuwe versie van `fac` opgestart met eigen lokale variabelen en parameters.

        fac(4) --> 4*fac(3) --> 3*fac(2) --> 2*fac(1) --> 1
          24   <-- 4*  6    <-- 3*  2    <-- 2*  1

De functie vernietigt zichzelf nadat hij zijn waarde heeft teruggegeven.
Theoretisch gezien is er geen limiet op het aantal recursies.
In de praktijk heeft python een limiet van geneste functies.

## Binair zoeken

While-lus is impliciet gemaakt => verschillende recursieve oproepen na elkaar

**Examenvraag**: Van recursief naar while en omgekeerd

## Torens van Hanoi

### Tijdscomplexiteit

 * n = # schijven
 
        H(n) = H(n-1) + 1 + H(n-1)
             = 2*H(n-1)         + 1
             = 2*(2*H(n-2) + 1) + 1
             = 4*H(n-2)    + 2  + 1
             = 8*H(n-3)+ 4 + 2  + 1
             
        H(k) = 2^(k-1) + 2^(k-2) + .. + 2 + 1
             = 2^k - 1


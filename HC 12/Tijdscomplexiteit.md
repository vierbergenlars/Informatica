#Tijdscomplexiteit van een zoekalgoritme

Tijdscomplexiteit: Hoeveel tijd het algoritme vraagt in functie van een stijgende
probleemgrootte.

## Lineair zoekalgoritme

```python
def linearSearch(x, seq):
    found = False
    for i in range(0, len(seq)):
        if(x == seq[i]): found = True
    return found
```

 * Lijst wordt per element doorlopen
 * Ieder probleem wordt vergeleken met het gezochte element.
 
### Berekenen complexiteit

 1. Significante operatie: De operatie die het meeste rekentijd gebruikt. (vergelijking `x==seq[i]`)
 2. Hoeveel keer komt de significate operatie voor per element in de lijst? (1 keer)
 
 => Complexiteit: `O(n)` (lineair)
 
## Linear zoekalgoritme, versie 2

```python
def linearSearch2(x, seq):
    found = False
    for i in range(0, len(seq)):
        if(x == seq[i]):
            found = True
            break
    return found
```

### Complexiteit?

Hangt af van de kans dat x in de lijst zit

Als x in de lijst zit: Gemiddeld aantal iteraties is tot in het midden van de lijst.
Als x niet in de lijst zit: Algoritme loopt tot op het einde.

 
Voorbeeld:
  Lijst met x elementen, bereik 0-10000
  x=1000: 9/10 kans dat het element niet in de lijst zit.
  x>> 10000: Grote kans dat element in de lijst zit: Gemiddeld x/2 iteraties.
 
Voorbeeld:
  Lijst met x elementen, bereik 0-100
  
  De kans dat er binnen de 100 getallen een match is gevonden is zeer groot.


## Binair zoekalgoritme

Preconditie: Lijst is geordend.

Algoritme:
 1. Willekeurig element vergelijken met gezochte waarde x
 2. 
    * Als het element < x: x zit in 2de helft van de lijst of zit niet in de lijst
    * Als het element > x: x zit in 1ste helft van de lijst of zit niet in de lijst
 3. Herhaal met de juiste helft van de lijst.

De te zoeken lijst wordt steeds gehalveerd totdat er nog 1 element over is.

### Complexiteit

k = aantal # dat de lus wordt uitgevoerd
  = aantal # dat n door 2 gedeeld kan worden.
  
Grootte k bepalen: 
    Als n een macht van 2 is: n = 2^k => k = log2(n)
    Als n geen macht van 2 is: 2^k-1 < n <= 2^k => k = log(2n), naar boven afgerond.

==> Complexiteit: logaritmisch

### Theoretische afleiding

        T(n) = c*log2(n)
        T(2n) = c*log2(2n)
              = c*log2(n) + c*log2(2)
              = c*log2(n) + c
              = T(n)      + c




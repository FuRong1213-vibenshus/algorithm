# Algoritmer

## Faglige mål
- Forstå og anvende klassiske algoritmer til søgning og sortering
- Forstå rekursion som en styringskonstruktion
- Kende til og implementere enkel træstrukturer (binært søgetræ)
- (Supplerende) Analysere og sammenligne algoirthmers effektivitet. 
- (Supplerende) Arbejde med mere komplekse datastrukturer og bruge dem i problemløsning.

## Materialer
- [Turtle graphics](https://docs.python.org/3/library/turtle.html)
- [Introduction to algrithms, third edition](https://www.cs.mcgill.ca/~akroit/math/compsci/Cormen%20Introduction%20to%20Algorithms.pdf)
- [Introduction to tree data structure](https://www.geeksforgeeks.org/dsa/introduction-to-tree-data-structure/)
- [Tidskompleksitet](https://da.wikipedia.org/wiki/Tidskompleksitet)
- [Introduction to Recursion](https://www.geeksforgeeks.org/dsa/introduction-to-recursion-2)
- [Call Stack Recursion](https://dev.to/muirujackson/call-stack-recursion-40eh)

## Introduktion
### Hvad er en algoirtme?

*An **algorithm** is any well-defined computational procedure that takes some value, or set of values, 
as **input** and produce some value, or set of values, as **output**. An algorithm is thus a sequence of computational steps that transform the input into the output*

[Introduction to algrithms, third edition](https://www.cs.mcgill.ca/~akroit/math/compsci/Cormen%20Introduction%20to%20Algorithms.pdf)


## Sorteringsalgorithmer 1
### Insertion sort
ref: https://www.geeksforgeeks.org/dsa/insertion-sort-algorithm/

```
Insertion_sort(A)
    for j = 2 to A.length
        key = A[j]
        // Insert A[j] into the sorted sequence A[1..j-1]
        i = j-1
        while i>0 and A[i] > key   
            A[i+1] = A[i]
            i=i-1
        A[i+1]=key
```

## Sorteringsalgorithmer 2
### Selection sort
ref: https://www.geeksforgeeks.org/dsa/selection-sort-algorithm-2/

Man leder gentagne gange efter det mindste element i den del af listen, der endnu ikke er sorteret, 
og bytter det frem til den korrekte position.

1. Find det mindste element i hele listen, og byt det med elementet på første plads.
2. Find derefter det næstmindste element i resten af listen (fra position 2 til n), og byt det på plads.
3. Fortsæt sådan, indtil alle elementer står i rækkefølge.

## Sorteringsalgorithmer 3
### Bubble sort
ref: https://www.geeksforgeeks.org/dsa/bubble-sort-algorithm/

Man lader de største elementer “boble” op til toppen ved gentagne sammenligninger og bytninger af naboelementer.

1. Sammenlign to naboer. Hvis de står forkert, byt dem.
2. Gå gennem hele listen.
3. Gentag processen, indtil der ikke er flere bytninger.

## Sorteringsalgorithmer 4
### Merge sort (divide & conquer)


[s.30-37 Introduction to algrithms, third edition](https://www.cs.mcgill.ca/~akroit/math/compsci/Cormen%20Introduction%20to%20Algorithms.pdf)

En rekursiv ”divide and conquer”-algoritme: man deler listen i to halvdele, sorterer hver del, og fletter dem derefter sammen i én sorteret liste.

1. Del listen i to lige store dele.
2. Sortér hver del rekursivt (indtil kun ét element er tilbage).
3. Flet de to sorterede del-lister sammen.



## Hvad koster proceduren?

### The Hiring problem

Forestil dig, at en virksomhed skal ansætte en ny medarbejde ud fra n ansøgere. Kandidaterne ankommer én af gangen,
og virksomhed skal træffe en beslutning med det samme: enten ansætte kandidaten eller afvise dem for altid.

For hver kandidat skal virksomheden:

1. afholde en sametale, som altid koster en fast pris $c_i$.
2. Vurdere kandidaten - er de bedre end den nuværende medarbejder?
3. Hvis ja, fyre den gamle og ansætte den nye, hvilket medfører en ekstra omkostning $c_h$.

De samlede forventede omkostning afhænger af:
- Antal samtaler: $n$
- Antal ansættelse: afhænger af, hvor mange gange en ny "bedre kandidat" dukker op. 



## Rekursion
- n'th Fibonacci 
- n'th factorial 

## Binær søgning

- Gæt et tal mellem 1 og 100
- Algoritme

## Advancered konstruktioner

### Træ 
- node 
- addChild
- displayDescendants

## Øveopgaver
1. Koster af algoritmer
    - Skriv pseduocode til **selection sort**, **insertion sort** og **bubble sort**
    - Implementér dem,
    - Udvid koden, så algoritmen tæller:
        - antal sammenlinginger 
        - antal bytninger
    - Sammenlign resultater for forskellige input:
        - sorteret,
        - omvendt sorteret,
        - tilfældigt
    - Brug [timeit](https://docs.python.org/3/library/timeit.html) til at måle køretid for de tre algorimer.
        - plot køretider vs. længden (n) af input list  
    - Ekstra udfordringer: brug fx `matplotlib` til at animere sorteringsprocessen.
        - hver søjle repræsentere et tal -- vis hvordan elementer flytter sig.

2. Rekursion
    - Nedtælling
        - Skrive en rekursiv funktion `countdown(n)`, der printer tallene fra `n` ned til 0.
        - Hvad der sker i "base case" og "recursive case".
    - Faktorial 
        - lav en rekursiv funktion `factorial(n)` der beregner `n!`. 
        - Sammenlign derefter med en iterativ version (dem med for-løkke). Hvilken version er mest effektiv? Hvorfor?
    - Fibonacci
        - Lav en rekursiv funktion `fibonacci(n)`. 
        - Udvid funktionen til at tælle, hvor mange gange den bliver kaldt (f.eks. med en global counter eller en parameter)
        - Diskussion: hvorfor Fibonacci er et *ineffektivt* eksempel på rekursion, og hvordan man kunne forbedre det. (memoization)
        - Lav en plot, der viser hvor mange funktionkald `fibonacci(n)` laver som funktion af n.
    - Merge Sort
        - Forstå psedukoden
        - Implementere merge sort
        - Sammenlign køretiden mellem merge sort vs bubble sort. Hvem har kortere køretide? 
    - Binær søgning
        - Skriv pseudokode til binærsøgning
            - iterativ
            - rekursiv
        - Implementation
            - Hvorfor skal listen være sorteret?
            - Hvor mange trin bruger binær søgning i værste fald?
    - Diskussion:
        - Hvornår er rekursion en god ide?
        - Hvornår bør man vælge iterative i stedet?
        

3. [ibog](https://programmering.systime.dk/?id=240)
    - Øvelse 8.6, Øvelse 8.7, Øvelse 8.9
    - Øvelse 8.11, Øvelse 8.13, Øvelse 8.14

3. Mundtelig Oplæg for et emnet
    - Dijkstra's algoritme
    - Rod cutting problem
    - Activity-selection problem
    - Tower of Hanoi promblem

3. Generative art 


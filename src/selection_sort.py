

import random
n = 10
a = random.choices(range(1,100), k=n)
def selection_sort(A):

    """Man leder gentagne gange efter det mindste element i den del af listen, der endnu ikke er sorteret, 
    og bytter det frem til den korrekte position.

    1. Find det mindste element i hele listen, og byt det med elementet på første plads.
    2. Find derefter det næstmindste element i resten af listen (fra position 2 til n), og byt det på plads.
    3. Fortsæt sådan, indtil alle elementer står i rækkefølge.
    """

    #key = A[0]
    l = len(A)
    for i in range(0,l):
        min_index = i
        j = i
        for j in range(i, l+1):
            if A[j]< A[min_index]:
                min_index = j
            
        A[i], A[min_index] = A[min_index], A[i]
    return A 

print(selection_sort(a))
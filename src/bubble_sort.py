
import random
from matplotlib import pyplot as plt
import numpy as np
import time

def bubble_sort(A):
    """
    
    Man lader de største elementer “boble” op til toppen ved gentagne sammenligninger og bytninger af naboelementer.

    1. Sammenlign to naboer. Hvis de står forkert, byt dem.
    2. Gå gennem hele listen.
    3. Gentag processen, indtil der ikke er flere bytninger.
    """

    l= len(A)
    counter = 0
    for j in range(l-1,0, -1):
        i = 0
        for i in range(0,j):
            if A[i]>A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]
                counter +=1

    return counter


count_list = []
N = np.array(range(100, 10000, 1000))
for  n in N:
    
    a = random.choices(range(1,1000), k=n)
    count_list.append(bubble_sort(a))

#print(count_list) 
fig, ax = plt.subplots()
plt.plot(N, count_list, label = "acutal switch")
plt.plot(N, np.pow(N, 2), label = "worst case")
ax.legend()
plt.show()
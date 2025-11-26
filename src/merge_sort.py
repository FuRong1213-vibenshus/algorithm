import numpy as np
import math 

def merge(A, p, q, r):
    print(f'p: {p}, q: {q}, r: {r}')
    n1 = q-p+1
    n2 = r-q
    L = np.empty(n1)
    R = np.empty(n2)
    L = A[p:p+n1]
    np.append(L,math.inf)

    R = A[q+1:q+n2+1]
    np.append(R, math.inf)

    i = 0
    j = 0
    for k in range(p, r):
        if L[i]<=R[j]:
            A[k] = L[i]
            i +=1
        else:
            A[k]=R[j]
            j+=1

def merge_sort(A, p, r):
    if p<r:
        q = (p+r)//2
        merge_sort(A, p, q)
        merge_sort(A, q+1,r)
        merge(A, p, q, r)
    

rng = np.random.default_rng(seed = 42)
arr1= rng.integers(low=0, high=100, size=16)
print(arr1)
merge_sort(arr1, 0, 10)


import random
n = 10
a = random.choices(range(1,100), k=n)
print(a)

def insertion_sort(A):

    """Insertion_sort(A)
    for j = 2 to A.length
        key = A[j]
        // Insert A[j] into the sorted sequence A[1..j-1]
        i = j-1
        while i>0 and A[i] > key   
            A[i+1] = A[i]
            i=i-1
        A[i+1]=key
    """

    for j in range(1, len(A)):
        key = A[j]
        i = j -1
        while i>=0 and A[i] > key:
            A[i+1] = A[i]
            A[i] = key
            i = i-1
    return A

print(insertion_sort(a))
import math
import random

def binary_search(target, A):
    """
    1. Let min = 0 and max = n-1.
    2. If max < min, then stop: target is not present in array. Return -1.
    3. Compute guess as the average of max and min, rounded down (so that it is an integer).
    4. If array[guess] equals target, then stop. You found it! Return guess.
    5. If the guess was too low, that is, array[guess] < target, then set min = guess + 1.
    6. Otherwise, the guess was too high. Set max = guess - 1.
    Go back to step 2.
    
    """

    min = 0 
    max = len(A)
    found = -1
    while max>min:
        guess = min + math.floor((max-min)/2)
        print(min, max, guess)
        if A[guess]==target:
            found = guess
            break
        elif A[guess] < target:
            min = guess+1
        else:
            max = guess-1
    return found 


def binary_search_rec(target, A, min, max):
    
    guess = min + math.floor((max-min)/2)
    while  ((guess>0) and
           (guess <max) and 
           (not(A[guess] == target))) :
        if A[guess]< target:
            guess = binary_search_rec(target, 
                                      A, 
                                      guess+1, 
                                      max,
                                      )
        elif A[guess] > target:
            guess = binary_search_rec(target, 
                                      A, 
                                      min, 
                                      guess-1)
    
    if guess == max:
        guess = -1

    return guess

    
A = range(1,10)
#target = random.choice(A)

target = 0 
print(f'searching for {target} in A, index is {binary_search_rec(target, A, 0, len(A))}')
counter = 0

def fibonacci_mem(n):
    
    global counter
    counter +=1 
    if n == 0:
        return 0,0
    if n == 1:
        return 1,0
    else:
        b1, b2 = fibonacci_mem(n-1)
        return b1+b2, b1


print(fibonacci_mem(9))
print(counter)
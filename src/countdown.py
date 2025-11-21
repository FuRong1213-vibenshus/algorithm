def count_down(n,c):

    if c == n:
        return True
    else: 
        count_down(n, c+1)
        print(c)
        return True
    

count_down(5,0)
def rec(n):
    if n <= 0:
        return
    rec(n - 2)
    print(n)
    
    

rec(10)
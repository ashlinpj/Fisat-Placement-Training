def rec(n):
    if(n<=0):
        return 200
    else:
        print(n)
        t=rec(n-1)
        return t


print(rec(5))



def rec(n):
    if n <= 0:
        return

    print(n)
    rec(n - 2)
    

rec(10)
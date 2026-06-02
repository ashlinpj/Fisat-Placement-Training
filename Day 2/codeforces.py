#codeforces 1560A

t=int(input())
for i in range(t):
    n=int(input())
    i=0
    k=1
    while 1:
        if i%3!=0 and i%10!=3:
            if n==k:
                print(i)
                break
            k+=1
        i+=1

#i=1 2 3 4 5 6  7  8  9 10 11 12
#k=1 2 4 5 7 8 10 11 14 16 17 19 
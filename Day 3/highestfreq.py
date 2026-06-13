l=[1,1,1,3,1,2,1,4,2,2,2,2]
d={}
for i in l:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
print(d)
max=max(d.values())
print(d.keys())
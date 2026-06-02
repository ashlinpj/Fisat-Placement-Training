n=input("Enter number:")
num=0
sum=0
count=1
n=int(n)
while n:
    num=n%10
    sum+=num**count
    count+=1
    n=n//10




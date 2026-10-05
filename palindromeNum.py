n=int(input("enter number"))

def fun(n):
    sum=0
    og=n
    while n>0:
        l=n%10
        sum=sum*10+l
        n=n//10
    return sum==og

res=fun(n)
print(res)

n=int(input("enter number"))

def fun(n):
    a=1
    b=1
    for i in range(1,n):
        c=a+b
        a=b
        b=c
    return b

res=fun(n)
print(res)
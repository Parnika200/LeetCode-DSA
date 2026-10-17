n=int(input("enter number"))

def fun(n):
    if n<=0:
        return "not an ugly number"
    else:
        while n%2==0:
            n=n//2
        while n%3==0:
            n=n//3
        while n%5==0:
            n=n//5

    if n==1:
        return "number is an Ugly Number"
    else:
        return "number is not an Ugly Number"

res=fun(n)
print(res)

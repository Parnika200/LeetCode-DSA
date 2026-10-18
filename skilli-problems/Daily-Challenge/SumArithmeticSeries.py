def sum(a,d,n):
    k=a
    sum=0
    for i in range(1,n+1):
        sum=sum+k
        k+=d
    return sum

r=sum(1,3,5)
print(r)

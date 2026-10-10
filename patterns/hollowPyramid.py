n=int(input("enter number"))

for i in range(n):
    print(" "*(n-i),end="")
    for j in range(i*2+1):
        if i==0 or i==n-1 or j==0 or j==i*2:
            print("*",end="")
        else:
            print(" ",end="")
    print()
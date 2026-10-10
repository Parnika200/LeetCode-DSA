n=int(input("enter number"))

for i in range(n):
    print(" "*(n+i),end="")
    for j in range(n-i):
        print("*",end=" ")
    print()
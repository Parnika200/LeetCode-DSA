n=int(input("number"))

mid=(n+1)//2

for i in range(n):
    print(" "*(n-i),end="")
    for j in range((i*2)+1):
        print("*",end="")
    print()

for i in range(n):
    print(" "*(0+i),end="")
    for j in range(n-i):
        print("*",end=" ")
    print()
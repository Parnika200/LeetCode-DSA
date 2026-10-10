n=int(input("number"))
mid=(n+1)//2
for i in range(n):
    print(" "*(n-i),end="")
   
    for i in range((i*2)+1):
        print("*",end=" ")
    print()
for i in range(n):
    print(" "*(n+1))
    for j in range((i//2)-1):
        print("*",end=" ")
    print()

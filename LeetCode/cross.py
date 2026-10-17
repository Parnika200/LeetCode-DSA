n=int(input("enetr n"))

for i in range(n+1):
    for j in range(n+1):
        if n//2==i or n//2==j:
            print("*",end="")
        else:
            print(" ",end="")
    print()
       
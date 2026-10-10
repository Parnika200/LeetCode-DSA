n=int(input("enter number"))

k=0
for i in range(n):
    for j in range(i):
        print(chr(65+k),end="")
        k+=1
    print()
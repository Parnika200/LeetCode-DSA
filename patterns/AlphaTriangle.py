n=int(input("number"))

for i in range(n):
    for j in range(i):
        print(chr(65+j),end="")
    print()
"""
1
23
456
"""
n=int(input("enter num"))
k=1
for i in range(n):
    for j in range(i):
        print(k,end=" ")
        k+=1
    print()


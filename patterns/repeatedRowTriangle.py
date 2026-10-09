"""
1
22
333
"""

n=int(input("enter num"))
k=0
for i in range(n):
    for j in range(i):
        print(k,end=" ")
    print()
    k+=1

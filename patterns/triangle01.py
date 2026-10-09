"""
1
01
101
"""
n=int(input("enter num"))

for i in range(n):
    for j in range(i):
        if (i+j)%2==0:
            print(1,end=" ")
        else:
            print(0,end=" ")
       
    print()

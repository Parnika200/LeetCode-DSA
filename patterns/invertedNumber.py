"""
1234
123
12
1
"""

n=int(input("enter num"))
for i in range(n):
    for j in range(n-i):
        print(j+1,end=" ")
    print()

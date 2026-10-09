"""
1
12
123
1234
"""

n=int(input("enter num"))

for i in range(n):
    for j in range(i):
        print(j+1,end=" ")
    print()


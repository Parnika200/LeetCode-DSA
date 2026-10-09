"""
   *
  **
 ***
"""
n=int(input("enter num"))
for i in range(n):
    print(" "*(n-i),end="")
    for j in range(i):
        print("*",end="")
    print()

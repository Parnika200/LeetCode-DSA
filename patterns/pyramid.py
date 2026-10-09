"""
  *
 ***
*****
"""

n=int(input("number"))

for i in range(n):
    print(" "*(n-i),end="")
    for j in range((i*2)+1):
        print("*",end="")
    print()

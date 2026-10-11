"""
Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
"""

n=int(input("enter number"))

def fun(n):
    
    for i in range(1,n+1):
        s=i*i
        if s>n:
            return i-1
        elif s==n:
            return i
    return 0

res=fun(n)
print(res)
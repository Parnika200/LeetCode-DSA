"""
Input: candies = [2,3,5,1,3], extraCandies = 3
 Output: [true,true,true,false,true] Explanation: If you give all extraCandies to:
Kid 1, they will have 2 + 3 = 5 candies, which is the greatest among the kids.
Kid 2, they will have 3 + 3 = 6 candies, which is the greatest among the kids.
Kid 3, they will have 5 + 3 = 8 candies, which is the greatest among the kids.
Kid 4, they will have 1 + 3 = 4 candies, which is not the greatest among the kids.
Kid 5, they will have 3 + 3 = 6 candies, which is the greatest among the kids.
"""

candies = [2,3,5,1,3]
extraCandies = 3

def fun(candies,extraCandies):
    m=max(candies)
    res=[]
    for i in candies:
        if i+extraCandies>=m:
            res.append(True)
        else:
            res.append(False)
    return res

r=fun(candies,extraCandies)
print(r)

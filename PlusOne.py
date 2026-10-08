nums=[1,2,3]
#output=[1,2,4]

def fun(nums):
    s=""
    for i in nums:
        s+=str(i)

    num=int(s)
    sum=num+1

    res=[]
    for i in str(sum):
        res.append(int(i))
    return res


p=fun(nums)
print(p)
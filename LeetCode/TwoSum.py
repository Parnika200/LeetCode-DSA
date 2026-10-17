nums=[1,2,3,5,7]
target=3

def fun(nums,target):
    for i in nums:
        for j in range(i+1):
            if nums[i]+nums[j]==target:
                return [i,j]
                
print(fun(nums,target))    


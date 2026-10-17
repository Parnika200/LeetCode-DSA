nums=[1,2,3,5,6]
target=4

def fun(nums,target):

    for i in range(len(nums)):
        if nums[i]==target:
            return i
        else:
            if nums[i]>target:
                return i
        return len(nums)
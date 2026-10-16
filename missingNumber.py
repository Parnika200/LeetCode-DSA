
def missingNumber( nums: list[int]) -> int:
    n=len(nums)
    for i in range(1,n+1):
        if i not in nums:
            return i
    return 0



        
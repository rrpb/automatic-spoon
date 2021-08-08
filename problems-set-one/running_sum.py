"""Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
Return the running sum of nums.
"""

def get_running_sum(nums):
    result=[]
    result.append(nums[0])
    for i in range(1,len(nums)):
        result.append(nums[i]+result[i-1])
    return result

nums = [3,1,2,10,1]
print(get_running_sum(nums))
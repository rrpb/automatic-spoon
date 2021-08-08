"""Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it.
That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i]"""

def get_small_numbers(nums):
    counts,cv=[0]*101,[0]*101
    for num in nums:
        counts[num]+=1
    for i in range(1,101):
        cv[i]=cv[i-1]+counts[i-1]
    return [cv[num] for num in nums]

nums = [8,1,2,2,3]
print(get_small_numbers(nums))
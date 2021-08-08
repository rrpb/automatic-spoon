"""Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it.
That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i]"""

def get_small_numbers(nums):
    sorted_nums=sorted(nums)
    num_to_index={}

    for index in range(len(sorted_nums)):
        if sorted_nums[index] not in num_to_index:
            num_to_index[sorted_nums[index]]=index

    return [num_to_index[nums[i]] for i in range(len(nums))]


nums = [8,1,2,2,3]
print(get_small_numbers(nums))
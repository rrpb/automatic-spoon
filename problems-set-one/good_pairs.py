"""Given an array of integers nums.

A pair (i,j) is called good if nums[i] == nums[j] and i < j.

Return the number of good pairs."""

def get_num_good_pairs(nums):
    result=0
    count_map={}
    for num in nums:
        if num in count_map:
            count_map[num]+=1
        else:
            count_map[num]=1

    for value in count_map.values():
        result+=(value)*(value-1)//2

    return result

nums = [1,2,3,1,1,3]
print(get_num_good_pairs(nums))

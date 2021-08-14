"""
https://leetcode.com/problems/permutations/
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.



Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

"""


class Solution:

    def __init__(self):
        self.ans=[]

    def permute(self, nums):
        n = len(nums)
        empty_list = [None] * n
        self.recurse(nums, 0, empty_list)
        return self.ans

    def recurse(self, nums, ind, current_list):
        # Base case: Did we place every number? If yes then add a deep copy of the list to answer
        if ind == len(nums):
            self.ans.append(list(current_list))
            return
        current_number = nums[ind]
        # We want to place current_number at every available position
        # Trying to place current_number at every index
        for i in range(len(current_list)):
            if current_list[i] is None:
                # We can place current_number here
                current_list[i] = current_number
                # recurse to the next ind
                self.recurse(nums, ind + 1, current_list)
                # Undo placing current number here
                current_list[i] = None


sol = Solution()
print(sol.permute([1, 2, 3]))
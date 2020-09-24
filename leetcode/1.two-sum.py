#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        def solution_1():
            nums_dict = {}
            for idx, num in enumerate(nums):
                if target - num in nums_dict:
                    return [nums_dict[target - num], idx]
                nums_dict[num] = idx

        def solution_2():
            nums_dict = {}
            for i, num in enumerate(nums):
                nums_dict[num] = i
                
            for i, num in enumerate(nums):
                if target - num in nums_dict and i != nums_dict[target - num]:
                    return nums.index(num), nums_dict[target - num]
        
        return solution_1()
            
        
# @lc code=end


#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []

        # 왼쪽 곱셈
        point = 1
        for i in range(len(nums)):
            result.append(point)
            point *= nums[i]
        
        # 왼쪽 곱셈 결과에 오른쪽 값을 차례대로 곱셈
        point = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= point
            point *= nums[i]

        return result

        
# @lc code=end


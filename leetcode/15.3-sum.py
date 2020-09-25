#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()
        len_nums = len(nums)
        for i in range(len(nums)-2):
            # 중복 값 건너 뜀
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # 좌, 우측에서 간격 좁혀가며 sum 계산
            left, right = i + 1, len_nums - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    results.append((nums[i], nums[left], nums[right]))

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
                        
        return results
        
# @lc code=end


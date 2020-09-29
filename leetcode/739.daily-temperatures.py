#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#

# @lc code=start
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        a = [0] * len(T)
        stack = []
        for i, cur in enumerate(T):
            while stack and cur > T[stack[-1]]:
                last = stack.pop()
                a[last] = i - last
            stack.append(i)
        return a
        
# @lc code=end


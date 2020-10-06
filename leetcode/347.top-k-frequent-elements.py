#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums)
        counter = sorted(counter.items(), key=(lambda x: x[1]), reverse=True)
        return [counter[i][0] for i in range(k)]


# @lc code=end

#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(candidates_sum, idx, path):
            if candidates_sum == 0:
                result.append(path)
            elif candidates_sum < 0:
                return

            for i in range(idx, len(candidates)):
                dfs(candidates_sum - candidates[i], i, path + [candidates[i]])

        dfs(target, 0, [])
        return result
# @lc code=end

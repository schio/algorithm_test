#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = {}
        max_len = start = 0
        for idx, char in enumerate(s):
            # 이미 나온 chare이면 update start
            if char in used and start <= used[char]:
                start = used[char] + 1
            else:
                max_len = max(max_len, idx - start + 1)
            used[char] = idx

        return max_len

# @lc code=end

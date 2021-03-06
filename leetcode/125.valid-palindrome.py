#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        
        s = re.sub("[^a-z0-9]", "", s.lower())
        return s == s[::-1]

        
# @lc code=end


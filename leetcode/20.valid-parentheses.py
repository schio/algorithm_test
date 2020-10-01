#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping_table = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        for char in s:
            if char not in mapping_table:
                stack.append(char)
            elif not stack or mapping_table[char] != stack.pop():
                return False
        return len(stack) == 0
        
# @lc code=end


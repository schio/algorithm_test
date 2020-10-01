#
# @lc app=leetcode id=316 lang=python3
#
# [316] Remove Duplicate Letters
#

# @lc code=start
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter,seen, stack = collections.Counter(s), set(), []

        for char in s:
            # 해당 문자를 한번 확인했으니 -1
            counter[char] -= 1

            # seen에 있는 것은 stack에 들어갔다는 뜻이므로 char을 더 볼 필요 없음
            if char in seen:
                continue
            
            # char의 알파벳순이 더 빠르고, char의 카운터가 0 이상이면 init
            while stack and char < stack[-1] and counter[stack[-1]] > 0:
                seen.remove(stack.pop())
            stack.append(char)
            seen.add(char)
        
        return "".join(stack)
        
        
# @lc code=end


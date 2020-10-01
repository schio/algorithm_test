#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#

# @lc code=start
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        answer = [0] * len(T)
        stack = []
        for i, cur in enumerate(T):

            
            # 이전보다 상승하는 지점에서 현재 온도와 스택에 쌓아둔 온도차 비교
            while stack and cur > T[stack[-1]]:
                # 계속 온도가 떨어지며 처리되지 못한 것들을 pop
                last = stack.pop()
                answer[last] = i - last
            # 현재 인덱스를 스택에 쌓아 둠
            stack.append(i)
        return answer
        
# @lc code=end


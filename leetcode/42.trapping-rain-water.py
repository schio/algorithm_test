#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
         
        volume = 0

        # 투포인터 쓰기 위해 셋팅
        left, right = 0, len(height) - 1 
        left_max, right_max = height[left], height[right]

        # 왼쪽에서 오른쪽으로, 오른쪽에서 왼쪽으로 좁혀옴
        while left < right:
            left_max = max(height[left], left_max)
            right_max = max(height[right], right_max)

            # 좌우 어느 쪽이든 낮은 쪽은 높은 쪽을 향해 포인터가 가운데로 점점 이동함.
            # 가장 높이가 높은 곳ㅇ서 좌우 포인터가 서로 만나 O(n)에 풀이 가능
            if left_max <= right_max:
                # 최대 높이의 막대까지 각각 좌우 기둥 최대 높이가 현재 높이와의 차이만큼 voulme을 더함
                volume += left_max - height[left] 
                left += 1
            else:
                volume += right_max - height[right]
                right -= 1
        return volume
        
# @lc code=end


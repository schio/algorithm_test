#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        root = result = ListNode(None)
        heap = []

        # 각 연결리스트의 루트를 힙에 저장
        for i, row in enumerate(lists):
            if row:
                heapq.heappush(heap, (row.val, i, row))
            
        while heap:
            _, idx, result.next = heapq.heappop(heap)

            result = result.next
            if result.next:
                heapq.heappush(heap, (result.next.val, idx, result.next))
        return root.next
        
# @lc code=end


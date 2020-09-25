

#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # l1과 l2를 비교하여 l2가 더 작으면 서로 스왑
        if not l1 or (l2 and l1.val > l2.val):
            l1, l2 = l2, l1
        # 재귀
        if l1:
            l1.next = self.mergeTwoLists(l1.next, l2)
        
        return l1


# @lc code=end


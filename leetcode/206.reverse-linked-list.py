#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # use recursive
        def reverse(node:ListNode, prev: ListNode=None):
            if not node:
                return prev
            else:
                next, node.next = node.next, prev
                return reverse(next, node)

        # use iterative
        def iterative(head):
            node, prev = head, None
            next = None
            while node:
                next, node.next = node.next, prev
                prev, node = node, next
            return prev
        return iterative(head)


# @lc code=end


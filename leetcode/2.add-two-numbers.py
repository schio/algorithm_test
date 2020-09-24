#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_list, l2_list = [], []

        while l1 != None:
            l1_list.append(str(l1.val))
            l1 = l1.next
        
        while l2 != None:
            l2_list.append(str(l2.val))
            l2 = l2.next

        l1 = "".join(map(str, l1_list[::-1]))
        l2 = "".join(map(str, l2_list[::-1]))
        
        result = [str(num) for num in str(int(l1) + int(l2))[::-1]]
        del l1
        del l2
        
        # list to ListNode
        head = ListNode(result[0])
        tail = head
        e=1
        while e < len(result):
            tail.next = ListNode(result[e])
            tail = tail.next
            e+=1
        return head

        
# @lc code=end


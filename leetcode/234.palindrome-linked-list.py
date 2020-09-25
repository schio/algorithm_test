#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
                
        # # use_list
        # nums = []
        # while head is not None:
        #     nums.append(head.val)
        #     head = head.next
        
        # return True if nums == nums[::-1] else False

        # use runner    
        rev = None
        slow = fast = head

        # 런너를 이용한 역순 연결 리스트 구성
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        if fast:
            # 입력값이 홀수일 때 slow runner가 한칸 더 앞으로 이동
            # 중앙의 값을 빗겨나기 위함. 중앙은 팰린드롬 체크에서 배제되어야 하므로.
            slow = slow.next

        # 팰린드롬 여부 체크
        while rev and rev.val == slow.val:
            slow = slow.next
            rev = rev.next

        return not rev


    
        
        
# @lc code=end


#
# @lc app=leetcode id=706 lang=python3
#
# [706] Design HashMap
#

# @lc code=start
from typing import KeysView


class MyHashMap:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 1000  # 로드팩터에서 버킷 사이즈
        self.table = collections.defaultdict(ListNode)

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        # 이번 문제에서 키는 정수형이므로 아래와 같이 단순한 형태로 처리가능
        index = key % self.size
        if self.table[index].value is None:
            self.table[index] = ListNode(key, value)

        # index에 node가 존재하는 경우 연결리스트 처리
        p = self.table[index]
        # Hash collision 발생시 개별 체이닝으로 대응
        while p:
            if p.key == key:
                p.value = value
                return
            if p.next is None:
                break
            p = p.next

        p.next = ListNode(key, value)

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        index = key % self.size
        if self.table[index].value is None:
            return -1

        # 노드가 존재할 때 일치하는 키 탐색
        p = self.table[index]
        while p:
            if p.key == key:
                return p.value
            p = p.next
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        index = key % self.size
        if self.table[index].value is None:
            return

        # index의 first node일 때 delete
        p = self.table[index]
        if p.key == key:
            self.table[index] = ListNode() if p.next is None else p.next
            return

        # delete linked list node
        prev = p
        while p:
            if p.key == key:
                prev.next = p.next
                return
            prev, p = p, p.next


class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
# @lc code=end

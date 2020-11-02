#
# @lc app=leetcode id=687 lang=python3
#
# [687] Longest Univalue Path
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    result = 0

    def longestUnivaluePath(self, root: TreeNode) -> int:
        def dfs(node):
            if node is None:
                return 0

            # 노드 끝까지 dfs 재귀 탐색
            left = dfs(node.left)
            right = dfs(node.right)

            # 현재 노드가 자식 노드와 같은 값일 경우 거리 1 증가
            left = left + 1 if node.left and node.left.val == node.val else 0
            right = right + 1 if node.right and node.right.val == node.val else 0

            self.result = max(self.result, left + right)
            return max(left, right)
        dfs(root)
        return self.result

# @lc code=end

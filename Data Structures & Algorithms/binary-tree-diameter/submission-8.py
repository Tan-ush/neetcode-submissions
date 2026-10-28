# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    max_count = 0

    def ddfs(self, root):
        if not root:
            return 0
        left = self.ddfs(root.left)
        right = self.ddfs(root.right)
        diam = left + right
        self.max_count = max(self.max_count, diam)
        return 1 + max(left, right)

    def diameterOfBinaryTree(self, root):
        self.ddfs(root)
        return self.max_count

        






        
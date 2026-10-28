# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def max_depth(self, root):
        if not root:
            return 0
        return(1 + max(self.max_depth(root.left), self.max_depth(root.right)))

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        cur = self.max_depth(root)
        q = deque([root])
        while q:
            node = q.pop()
            if node:
                if node.right and node.left:
                    return max(cur, (self.max_depth(node.left) + self.max_depth(node.right) + 1)) - 1
                q.appendleft(node.left)
                q.appendleft(node.right)
        return cur - 1






        
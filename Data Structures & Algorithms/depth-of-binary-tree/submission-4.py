# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        n = 0
        m = 0
        if not root:
            return 0
        count = 0
        stack = [root]
        while stack:
            node = stack.pop()
            if node.left:
                n = self.maxDepth(node.left)
            if node.right:
                m = self.maxDepth(node.right)
            count += max(n, m)
        return count + 1

        
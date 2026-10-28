# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        q1 = deque([p])
        q2 = deque([q])
        while q1 and q2:
            node1 = q1.pop()
            node2 = q2.pop()
            if node1 and node2:
                if node1.val != node2.val:
                    return False
                q1.appendleft(node1.left)
                q1.appendleft(node1.right)
                q2.appendleft(node2.left)
                q2.appendleft(node2.right)
            else:
                if node1 != node2:
                    return False
        if q1 or q2:
            return False
        return True

        
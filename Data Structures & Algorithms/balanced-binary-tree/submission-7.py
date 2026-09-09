# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def height(self, root: Optional[TreeNode]) -> int:
        height = 0
        if not root:
            return 0
        height += 1
        int1 = self.height(root.left)
        int2 = self.height(root.right)
        height += max(int1, int2)
        return height


    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        leftheight = self.height(root.left)
        rightheight = self.height(root.right)
        if abs(leftheight - rightheight) > 1:
            return False
        bool1 = self.isBalanced(root.left)
        bool2 = self.isBalanced(root.right)
        if not bool1 or not bool2:
            return False
        return True
        
        
        
        







        
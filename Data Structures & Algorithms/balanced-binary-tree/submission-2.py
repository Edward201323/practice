# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        leftH = self.getHeight(root.left)
        rightH = self.getHeight(root.right)
        
        if abs(leftH - rightH) > 1:
            return False

        left = self.isBalanced(root.left)
        right = self.isBalanced(root.right)

        return left and right
    
    def getHeight(self, root):
        if not root:
            return 0

        left = self.getHeight(root.left)
        right = self.getHeight(root.right)

        return max(left, right) + 1
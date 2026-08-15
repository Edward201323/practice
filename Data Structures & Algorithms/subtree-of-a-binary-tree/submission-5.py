# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False

        if root.val == subRoot.val and self.subtree(root, subRoot):
            return True

        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)

        return left or right
        
    def subtree(self, root, subRoot):
        if not root and not subRoot:
            return True

        if not root or not subRoot:
            return False
        if root.val != subRoot.val:
            return False

        left = self.subtree(root.left, subRoot.left)
        right = self.subtree(root.right, subRoot.right)

        return left and right
        
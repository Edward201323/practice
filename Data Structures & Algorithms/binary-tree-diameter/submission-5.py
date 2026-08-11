# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    maxDiameter = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.findMaxDiameter(root)
        return self.maxDiameter

    def findMaxDiameter(self, root):
        if not root:
            return 0
        
        left = self.findMaxDiameter(root.left)
        right = self.findMaxDiameter(root.right)
        currDiameter = left + right

        if currDiameter > self.maxDiameter:
            self.maxDiameter = currDiameter
        
        return max(left, right) + 1



        
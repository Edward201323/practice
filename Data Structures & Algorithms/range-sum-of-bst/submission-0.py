# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        sum = 0
        for num in range(low, high + 1):
            if self.search(root, num):
                sum += num

        return sum

    def search(self, root, num):
        if not root:
            return False

        if num == root.val:
            return True
        elif num < root.val:
            return self.search(root.left, num)
        else:
            return self.search(root.right, num)
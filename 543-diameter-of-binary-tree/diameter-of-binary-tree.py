# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxDiameter = 0
        self.calcDiameter(root)

        return self.maxDiameter
    
    def calcDiameter(self, root):
        if not root:
            return 0
        
        left = self.calcDiameter(root.left)
        right = self.calcDiameter(root.right)

        currDiameter = left + right

        self.maxDiameter = max(self.maxDiameter, currDiameter)

        return 1 + max(left,right)
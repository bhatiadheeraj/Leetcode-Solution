# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxDiameter = 0
        self.explore(root)
        return self.maxDiameter
    
    def explore(self, root):
        if not root:
            return 0
        
        left = self.explore(root.left)
        right = self.explore(root.right)

        sum_diameter = left + right 
        self.maxDiameter = max(sum_diameter, self.maxDiameter)

        return 1 + max(left, right)
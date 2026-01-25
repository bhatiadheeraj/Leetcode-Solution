# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ans = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        self.dfs(root)
        return self.ans
        
    def dfs(self,root):
        if not root:
            return 0

        left = self.dfs(root.left)
        right = self.dfs(root.right)

        currentDiameter = left + right 

        self.ans = max(self.ans, currentDiameter)

        return 1 + max(left, right)
    
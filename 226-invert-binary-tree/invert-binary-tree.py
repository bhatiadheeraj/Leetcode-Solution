# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def invertNode(root):
            if not root:
                return
            #switch vals
            tempRight = root.right
            tempLeft = root.left

            root.right = tempLeft
            root.left = tempRight

            #invert their kids
            invertNode(root.right)
            invertNode(root.left)
        
        invertNode(root)
        return root
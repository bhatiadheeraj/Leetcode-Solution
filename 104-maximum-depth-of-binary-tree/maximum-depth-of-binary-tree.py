# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q= deque([root])
        level = 0
        res = []
        while q:
            for i in range(len(q)):
                item = q.popleft()
                if item and item.right:
                    q.append(item.right)
                if item and item.left:
                    q.append(item.left)
            level += 1
        return level
        
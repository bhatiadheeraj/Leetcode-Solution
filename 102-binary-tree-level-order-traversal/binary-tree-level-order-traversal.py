# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque([root])
        result = []

        if not root :
            return []
        while q:
            level = []
            for index in range(len(q)):
                item = q.popleft()
                if item:
                    level.append(item.val)
                if item and item.left:
                    q.append(item.left)
                if item and item.right:
                    q.append(item.right)
            result.append(level)

        return result
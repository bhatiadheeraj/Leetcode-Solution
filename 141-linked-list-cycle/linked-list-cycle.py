# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        ahead = head
        curr = head

        while ahead and ahead.next:
            curr = curr.next
            ahead = ahead.next.next
            if curr == ahead:
                return True
        
        return False 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        current = head
        runner = head

        while runner != None and runner.next != None:
            current = current.next
            runner = runner.next.next
            if runner == current:
                return True
        
        return False
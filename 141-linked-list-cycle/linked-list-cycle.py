# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head
        runner = head

        if not curr:
            return False
        if not curr.next:
            return False

        while runner and runner.next != None:
            curr = curr.next
            runner = runner.next.next
            if curr == runner:
                return True
        return False
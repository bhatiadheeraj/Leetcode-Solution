# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head 
        runner = head

        while runner != None and runner.next != None:
            current = current.next
            runner = runner.next.next
        return current
        
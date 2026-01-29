# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None

        dummy = prev

        while curr:
            temp = ListNode(curr.val, prev)
            prev = temp
            curr = curr.next
        return prev

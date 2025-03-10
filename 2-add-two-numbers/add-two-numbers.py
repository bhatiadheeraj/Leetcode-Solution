# from typing import Optional

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()  # Dummy node for easier handling
        sum_linked_list = dummy
        extra = 0  # Use an integer instead of a boolean

        while l1 or l2 or extra:
            sum_val = extra
            if l1:
                sum_val += l1.val
                l1 = l1.next
            if l2:
                sum_val += l2.val
                l2 = l2.next
            
            extra = sum_val // 10  # Compute carry
            sum_val = sum_val % 10  # Keep only the last digit
            
            sum_linked_list.next = ListNode(sum_val)
            sum_linked_list = sum_linked_list.next  # Move forward

        return dummy.next  # Return the head of the result

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        head = ListNode()
        tail = head
        while l1 is not None or l2 is not None:
            if l1 and l2:
                tail.val = l1.val + l2.val + carry
                l1 = l1.next
                l2 = l2.next
            elif l1:
                tail.val += l1.val + carry
                l1 = l1.next
            else:
                tail.val += l2.val + carry
                l2 = l2.next
            carry = 0
            if tail.val > 9:
                carry = 1
                tail.val %= 10
            if l1 is None and l2 is None and carry == 0:
                tail.next = None
            else:
                tail.next = ListNode()
                tail = tail.next
        if carry == 1:
            tail.val = 1
        return head

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode | None) -> ListNode | None:
        if head.next is None:
            return head
        dummy = ListNode(float('-inf'))
        dummy.next = head
        prev = head
        curr = head.next
        while curr:
            if prev.val <= curr.val:
                prev = curr
                curr = curr.next
                continue
            insert_pos = dummy
            while insert_pos.next.val < curr.val:
                insert_pos = insert_pos.next
            next_process = curr.next
            prev.next = next_process
            curr.next = insert_pos.next
            insert_pos.next = curr
            curr = next_process
        return dummy.next

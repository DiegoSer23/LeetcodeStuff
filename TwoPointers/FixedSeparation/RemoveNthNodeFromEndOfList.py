class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        dummy_node = ListNode(next=head)
        fast_ptr = dummy_node
        slow_ptr = dummy_node
        for _ in range(n):
            fast_ptr = fast_ptr.next
        while fast_ptr.next is not None:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next
        slow_ptr.next = slow_ptr.next.next
        return dummy_node.next

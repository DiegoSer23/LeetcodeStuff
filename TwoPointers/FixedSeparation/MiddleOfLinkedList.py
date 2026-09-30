class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        count = 0
        mid_ptr = head
        curr = head
        while curr:
            curr = curr.next
            count += 1
        mid = (count // 2) + 1
        count = 1
        while count < mid:
            mid_ptr = mid_ptr.next
            count += 1
        return mid_ptr

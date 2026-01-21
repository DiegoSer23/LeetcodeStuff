# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = {}
        tail = head
        while tail is not None:
            if tail.val not in seen:
                seen[tail.val] = tail.next
            else:
                if seen[tail.val] == tail.next:
                    return True
            tail = tail.next
        return False

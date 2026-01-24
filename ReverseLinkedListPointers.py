class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        prevNode = None
        nextNode = head.next
        currentNode = head
        while True:
            currentNode.next = prevNode
            prevNode = currentNode
            currentNode = nextNode
            if currentNode is None:
                return prevNode
            nextNode = currentNode.next

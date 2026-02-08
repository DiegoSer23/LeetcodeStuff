class ListNode:
    def __init__(self, val=None, next=None):
        self.value=val
        self.next=None

class MyHashSet:

    def __init__(self):
        self.keys = [ListNode(0) for i in range(1000)]

    def add(self, key: int) -> None:
        index = key % 1000
        current = self.keys[index]
        while current.next is not None:
            if current.next.value == key:
                return
            current = current.next
        current.next = ListNode(key)
        return

    def remove(self, key: int) -> None:
        index = key % 1000
        current = self.keys[index]
        while current.next is not None:
            if current.next.value == key:
                current.next = current.next.next
                return
            current = current.next
        return
        
    def contains(self, key: int) -> bool:
        index = key % 1000
        current = self.keys[index]
        while current.next is not None:
            if current.next.value == key:
                return True
            current = current.next
        return False

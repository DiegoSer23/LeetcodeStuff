class ListNode:
    def __init__(self, key, value, nextNode=None):
        self.key = key
        self.value = value
        self.next = nextNode

class MyHashMap:

    def __init__(self):
        self.maps = [ListNode(-1,-1) for i in range(1000)]

    def put(self, key: int, value: int) -> None:
        index = key % 1000
        cur = self.maps[index]
        while cur.next is not None:
            if cur.next.key == key:
                cur.next.value = value
                return
            cur = cur.next
        cur.next = ListNode(key, value)

    def get(self, key: int) -> int:
        index = key % 1000
        cur = self.maps[index]
        while cur.next is not None:
            if cur.next.key == key:
                return cur.next.value
            cur = cur.next
        return -1

    def remove(self, key: int) -> None:
        index = key % 1000
        cur = self.maps[index]
        while cur.next is not None:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next

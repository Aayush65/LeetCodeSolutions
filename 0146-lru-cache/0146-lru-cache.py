class ListNode:
    
    def __init__(self, val: list[int], prev = None, next = None):
        self.val = val
        self.prev = prev
        self.next = next
        

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.dummy = ListNode([None, None])
        self.last = self.dummy
        self.nodeMap = {}

    def get(self, key: int) -> int:
        if key not in self.nodeMap:
            return -1
        node = self.nodeMap[key]
        self.delete(node)
        self.put(key, node.val[1])
        return self.nodeMap[key].val[1]

    def delete(self, node: ListNode):
        node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        else:
            self.last = self.last.prev if self.last.prev else None
        del self.nodeMap[node.val[0]]
        self.size -= 1

    def put(self, key: int, value: int) -> None:
        if key in self.nodeMap:
            node = self.nodeMap[key]
            self.delete(node)
            self.put(key, value)
            return
        
        newNode = ListNode([key, value], self.dummy, self.dummy.next)
        self.dummy.next = newNode
        if newNode.next:
            newNode.next.prev = newNode
        if self.last == self.dummy:
            self.last = newNode
        self.nodeMap[key] = newNode
        self.size += 1

        if self.size > self.capacity:
            self.delete(self.last)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodeMap = {}
        curr = head
        headNew = currNew = Node(-1) if curr else None
        while curr:
            currNew.val = curr.val
            if curr.next:
                currNew.next = Node(-1)
            nodeMap[curr] = currNew
            currNew = currNew.next
            curr = curr.next
            
        curr = head
        currNew = headNew
        while curr:
            random = nodeMap[curr.random] if curr.random in nodeMap else None
            currNew.random = random
            curr = curr.next
            currNew = currNew.next
        return headNew
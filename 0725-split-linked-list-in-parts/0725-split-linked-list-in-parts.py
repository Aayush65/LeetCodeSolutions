# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
            
        parts = []
        curr = head
        while curr:
            parts.append(curr)
            prev = None
            for i in range(ceil(length / k)):
                print("Loop: " , curr.val, " ", ceil(length / k))
                prev = curr
                curr = curr.next
            if prev:
                prev.next = None
            length -= ceil(length / k)
            k -= 1
            
        for i in range(k):
            parts.append(None)
        return parts
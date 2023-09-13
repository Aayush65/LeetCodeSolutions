# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        crits = []
        
        prev = head
        curr = head.next
        index = 1
        while curr.next:
            if prev.val > curr.val and curr.next.val > curr.val:
                crits.append(index)
            if prev.val < curr.val and curr.next.val < curr.val:
                crits.append(index)
            index += 1
            prev = curr
            curr = curr.next
        
        if len(crits) < 2:
            return [-1, -1]
        
        minLen = float("inf")
        for i in range(1, len(crits)):
            minLen = min(minLen, crits[i] - crits[i - 1])
        return [minLen, crits[-1] - crits[0]]
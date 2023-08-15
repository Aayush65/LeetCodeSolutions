# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy = ListNode(None, head)
        small = big = dummy
        while True:
            while small.next and small.next.val < x:
                small = small.next
            if not small.next:
                break
            if big.val == None:
                big = small
            while big.next and big.next.val >= x:
                big = big.next
            if not big.next:
                break
            
            bigNext = big.next.next
            big.next.next = small.next
            small.next = big.next
            big.next = bigNext
        return dummy.next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        p1 = ListNode(None, head)
        p2 = fast = head
        for i in range(k):
            p1 = p1.next
            fast = fast.next
        while fast:
            p2 = p2.next
            fast = fast.next
        p1.val, p2.val = p2.val, p1.val
        return head
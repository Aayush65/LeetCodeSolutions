# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        dummy = ListNode(None, head)
        slow = fast = dummy
        while slow and fast:
            if slow != dummy and slow == fast:
                return True
            slow = slow.next
            fast = fast.next
            if fast:
                fast = fast.next
        return False
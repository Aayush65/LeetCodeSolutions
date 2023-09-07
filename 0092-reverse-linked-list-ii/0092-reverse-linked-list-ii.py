# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # unchanged head's tail
        dummy = newHead = ListNode(None, head)
        for _ in range(left-1):
            newHead = newHead.next

        # reversing the list between left and right node
        prev = None
        curr = newHead.next
        for i in range(right - left + 1):
            next = curr.next
            curr.next = prev
            prev, curr = curr, next

        # Pointing the unchanged tail of the head node to the reversed head of the list
        newHead.next.next = curr
        newHead.next = prev

        return dummy.next
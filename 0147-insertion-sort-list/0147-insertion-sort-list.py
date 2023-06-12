# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(None, head)
        
        it = head
        while it:
            curr = dummy
            while curr.next and curr.next.val < it.val:
                curr = curr.next
            right = it.next
            if it != curr.next:
                it.next = curr.next
                curr.next = it
            else:
                it.next = None
            it = right
        return dummy.next
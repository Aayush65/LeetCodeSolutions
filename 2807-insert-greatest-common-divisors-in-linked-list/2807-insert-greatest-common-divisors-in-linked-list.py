# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        div1, div2 = head, head.next
        while div2:
            hcf = gcd(div1.val, div2.val)
            newNode = ListNode(hcf, div2)
            div1.next = newNode
            div1 = div2
            div2 = div2.next
        return head
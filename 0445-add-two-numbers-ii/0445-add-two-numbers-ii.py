# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = 0
        while l1:
            num1 = num1 * 10 + l1.val
            l1 = l1.next
        num2 = 0
        while l2:
            num2 = num2 * 10 + l2.val
            l2 = l2.next

        l3head = l3 = ListNode()
        num3 = num1 + num2
        numLen = int(log10(num3)) if num3 else 0
        for i in range(numLen, -1, -1):
            l3.next = ListNode(num3 // 10 ** i)
            l3 = l3.next
            num3 %= 10 ** i
        return l3head.next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        num = []
        curr = head
        while curr:
            num.append(curr.val)
            curr = curr.next
        
        newNum = []
        carry = 0
        while num or carry:
            nextEle = carry
            if num:
                nextEle += num[-1] * 2
                num.pop()
            carry = 0
            if nextEle >= 10:
                carry = 1
                nextEle -= 10
            newNum.append(nextEle)
        newNum.reverse()
        num = newNum
        
        head = curr = ListNode()
        dummy = prev = ListNode(0, head)
        for i in num:
            curr.val = i
            curr.next = ListNode()
            prev = prev.next
            curr = curr.next
        prev.next = None
        return head
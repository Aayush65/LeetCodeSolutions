# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = curr = ListNode()
        heap = []
        nodeValMap = {}
        for i in lists:
            if i:
                heappush(heap, i.val)
                if i.val in nodeValMap:
                    nodeValMap[i.val].append(i)
                else:
                    nodeValMap[i.val] = [i]

        while heap:
            curr.next = nodeValMap[heappop(heap)].pop()
            curr = curr.next
            if curr.next:
                heappush(heap, curr.next.val)
                if curr.next.val in nodeValMap:
                    nodeValMap[curr.next.val].append(curr.next)
                else:
                    nodeValMap[curr.next.val] = [curr.next]
        return dummy.next
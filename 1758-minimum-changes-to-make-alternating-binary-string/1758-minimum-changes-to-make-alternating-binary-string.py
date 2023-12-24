class Solution:
    def minOperations(self, s: str) -> int:
        cost1 = 0
        curr = 0
        for i in s:
            cost1 += int(i) != curr
            curr = 1 - curr
        
        cost2 = 0
        curr = 1
        for i in s:
            cost2 += int(i) != curr
            curr = 1 - curr
        
        return min(cost1, cost2)
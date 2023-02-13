class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        res = 0
        i = 0
        while i <= total:
            res += (total - i) // cost2 + 1
            i += cost1
        return res
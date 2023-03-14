class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        def check(val: int) -> bool:
            i = bisect_left(citations, val)
            return n - i >= val
        
        lo = 0
        hi = n
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if check(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo
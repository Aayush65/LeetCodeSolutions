class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def check(candy: int) -> bool:
            if candy == 0:
                return True
            kids = 0
            for i in candies:
                kids += i // candy
            return kids >= k
        
        hi = max(candies)
        lo = 0
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if check(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo

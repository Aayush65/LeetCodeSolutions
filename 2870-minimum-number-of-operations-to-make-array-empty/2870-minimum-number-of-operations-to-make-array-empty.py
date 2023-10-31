class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = {i: 0 for i in nums}
        for i in nums:
            count[i] += 1
        freq = [count[i] for i in count]
        
        
        @cache
        def dp(n: int) -> int:
            if n == 0:
                return 0
            if abs(n) == 1:
                return float("inf")
            return 1 + min(dp(n - 2), dp(n - 3))
            
        res = 0
        for i in freq:
            ops = dp(i)
            if ops == float("inf"):
                return -1
            res += ops
        return res
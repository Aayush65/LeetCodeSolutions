class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        preSum = [0]
        for i in stones:
            preSum.append(preSum[-1] + i)
            
        @lru_cache(2000)
        def dp(l: int, r: int) -> int:
            if l == r:
                return 0
            total = preSum[r] - preSum[l]
            left = total - stones[l] - dp(l + 1, r)
            right = total - stones[r - 1] - dp(l, r - 1)
            return max(left, right)
    
        return dp(0, len(stones))
class Solution:
    def maxScore(self, nums: List[int]) -> int:
        memo = {}
        n = len(nums)
        
        def dp(bitmask: int) -> int:
            if bitmask in memo:
                return memo[bitmask]
            ops = 0
            for i in range(n):
                if 1 << (n - 1 - i) & bitmask:
                    ops += 1
            ops = ops // 2 + 1
            res = 0
            for i in range(n):
                if 1 << (n - i - 1) & bitmask:
                    continue
                iBitmask = 1 << (n - 1 - i) | bitmask
                for j in range(i + 1, n):
                    if 1 << (n - 1- j) & bitmask:
                        continue
                    jBitmask = 1 << (n - 1- j) | iBitmask
                    res = max(res, ops * gcd(nums[i], nums[j]) + dp(jBitmask))
            memo[bitmask] = res
            return res
                
        
        return dp(0)
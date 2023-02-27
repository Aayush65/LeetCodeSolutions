class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        memo = {}
        def dp(i: int, j: int) -> int:
            if (i, j) in memo:
                return memo[(i, j)]
            if i > j:
                return 0
            res = 0
            prv = 1 if i - 1 < 0 else nums[i - 1]
            nxt = 1 if j + 1 == len(nums) else nums[j + 1]
            for idx in range(i, j + 1):
                score = prv * nums[idx] * nxt
                res = max(res, score + dp(i, idx - 1) + dp(idx + 1, j))
            memo[(i, j)] = res
            return res
            
        return dp(0, len(nums) - 1)